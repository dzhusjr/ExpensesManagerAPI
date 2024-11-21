from django.db import models
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from expenses.models import Expense
from expenses.serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    # Basic CRUD is handled automatically by ModelViewSet

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category = request.query_params.get('category')

        if not category:
            return Response(
                {'error': 'Category parameter is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            expenses = Expense.objects.filter(category=category)

            page = self.paginate_queryset(expenses)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(expenses, many=True)
            return Response(serializer.data)
        except Expense.DoesNotExist:
            return Response({'error': 'Expense not found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def by_date_range(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not start_date or not end_date:
            return Response(
                {'error': 'Start date and end date are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            expenses = Expense.objects.filter(date__range=[start_date, end_date])

            page = self.paginate_queryset(expenses)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(expenses, many=True)
            return Response(serializer.data)
        except Expense.DoesNotExist:
            return Response({'error': 'Expense not found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def category_summary(self, request):
        user_id = request.query_params.get('user_id')
        month = request.query_params.get('month')

        if not user_id or not month:
            return Response(
                {'error': 'User ID and month are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        expenses = Expense.objects.filter(user_id=user_id, date__month=month)
        summary = expenses.values('category').annotate(total_amount=models.Sum('amount'))

        return Response(summary, status=status.HTTP_200_OK)
