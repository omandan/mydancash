from django.shortcuts import render,redirect,reverse,get_object_or_404
from .forms import SignupForm,EmailAddForm,UserEditForm,PersonalEditForm
from django.contrib import messages
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Account,Email,Phone,ConfirmEmail
def UserCreate(request):
	if request.user.is_authenticated:
		messages.info(request, f'You have been loged in ! \n you can`t create new account now')
		return redirect('index')
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}! you can login now')
			return redirect('login')
	form = SignupForm()
	return render(request, 'registration/user_form.html', {'form': form})

@login_required
def AccountPublicView(request,pk):
	emails=Email.objects.filter(oner=pk,vsbilty=True)
	phones=Phone.objects.filter(oner=pk,vsbilty=True)
	user_account=User.objects.get(id=pk)
	context={'emails':emails,'phones' :phones ,'user_account':user_account}
	return render(request,'accounts/account_public.html',context)

#in next commit will use conection confirm func in cash2
'''
@login_required
def EmailAddView(request):
	if request.method == 'POST':
		form = EmailAddForm(request.POST)
		form.instance.oner=request.user
		if form.is_valid():
			form.save()
			return redirect('index')#should return sucsess send email view
	form = EmailAddForm()
	return render(request, 'accounts/email_form.html', {'form': form})
'''

class EmailAddView(LoginRequiredMixin,CreateView):
	model=Email
	fields=['value','vsbilty']
	template_name = 'accounts/email_form.html'
	def get_success_url(self):
		return reverse('account-conection')
	def form_valid(self, form):
		form.instance.oner = self.request.user
		return super().form_valid(form)
	#try to add email that create before for diffrent user or same user and shoud return error

class EmailEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	def get_success_url(self):
		return reverse('account-conection')
	model = Email
	fields = ['value', 'vsbilty']
	template_name ='accounts/email_form.html'
	def test_func(self):
		value = self.get_object()
		if self.request.user == value.oner:
			return True
		return False

@login_required
def AccountConectionView(request):
	emails=Email.objects.filter(oner=request.user)
	phones=Phone.objects.filter(oner=request.user)
	context={'emails':emails,'phones' :phones }
	return render(request,'accounts/account_conection.html',context)

@login_required
def AccountPersonalView(request):
	return render(request,'accounts/account_personal.html')

@login_required
def AccountPersonalEditView(request):
    if request.method == 'POST':
        u_form = UserEditForm(request.POST, instance=request.user)
        a_form = PersonalEditForm(request.POST,
                                   request.FILES,
                                   instance=request.user.account)
        if u_form.is_valid() and a_form.is_valid():
            u_form.save()
            a_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('account-personal')

    else:
        u_form = UserEditForm(instance=request.user)
        a_form = PersonalEditForm(instance=request.user.account)

    context = {
        'u_form': u_form,
        'a_form': a_form
    }
    return render(request, 'accounts/account_personal_edit.html', context)

def ConfirmEmailReport(request,pk):
	confirm_email=get_object_or_404(ConfirmEmail,id=pk)
	if request.user==confirm_email.email.oner :
		context={'confirm_email':confirm_email}
		return render(request, 'accounts/email_confirm_report.html',context)
	else:
		return HttpResponse(status=403)