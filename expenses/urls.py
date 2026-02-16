from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),

    path('expenses/', ListExpenseView.as_view()),
    path('expenses/add/', AddExpenseView.as_view()),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view()),

    path('expenses/summary/monthly/', MonthlySummaryView.as_view()),
    path('expenses/summary/category/', CategorySummaryView.as_view()),
]
