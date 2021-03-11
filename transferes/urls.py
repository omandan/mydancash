from django.urls import path,include
from .views import TransfereCreateView,TransfereListView
urlpatterns = [
	path('history/',TransfereListView.as_view(),name='my-trans-history'),
    path('new/',TransfereCreateView,name='new-trans')
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
