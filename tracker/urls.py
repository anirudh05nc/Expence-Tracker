from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete-transaction/<id>', views.deleteTransaction, name='delete_transaction'),
]