from django.urls import path,include
from .views import (
BillAddView,
BillsHistoryView,
BillEditView,
BillPayView,
BillDetailsView
)
urlpatterns = [
path("add/",BillAddView.as_view(),name='bill-add'),
path("history/",BillsHistoryView,name='bills-history'),
path("edit/<int:pk>",BillEditView.as_view(),name='bill-edit'),
path("pay/<int:pk>",BillPayView,name='bill-pay'),
path("details/<int:pk>",BillDetailsView,name='bill-details'),
]