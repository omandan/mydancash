from django.urls import path,include
from .views import (
	UserCreate , 
	AccountPublicView , 
	EmailAddView ,
	EmailEditView ,
	AccountPersonalView,
	AccountConectionView ,
	AccountPersonalEditView,
	ConfirmEmailReport
	)
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/',UserCreate,name='signup'),
    path('account/personal/',AccountPersonalView,name='account-personal'),
    path('account/personal/edit',AccountPersonalEditView,name='account-personal-edit'),
    path('account/public/<int:pk>',AccountPublicView,name='account-public'),
    path('account/conection/',AccountConectionView,name='account-conection'),
    path('account/email/add',EmailAddView.as_view(),name='email-add'),
    path('account/email/edit/<int:pk>',EmailEditView.as_view(),name='email-edit'),
    path('account/email/validation-report/<int:pk>',ConfirmEmailReport,name='email-validation-report')
    ]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
