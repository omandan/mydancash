from django.shortcuts import render,reverse,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.edit import CreateView,UpdateView
from .models import Bill
from django.contrib.auth.decorators import login_required
from .forms import BillPayForm
from transferes.models import Transfere
from django.utils import timezone
from django.contrib import messages

def status(bill):
		repayment=0
		repayment_trans=repayments(bill)

		for trans in repayment_trans:
			repayment+=trans.ammount
			
			if (repayment>=bill.ammount):
				return "payed"
			elif (bill.exp_date<timezone.now()):
				return "exp"
		return "wating"

def repayments(bill):
		return Transfere.objects.filter(bill=bill,create_date__lte=bill.exp_date)

def repayments_sum(bill):
	sum=0
	repayment=repayments(bill)
	for trans in repayment:
		sum += trans.ammount
	return sum

# Create your views here.
class BillAddView(LoginRequiredMixin,CreateView):
	model=Bill
	fields=['exp_date','vsbilty','ammount']
	template_name = 'bills/bill_form.html'
	def get_success_url(self):
		return reverse('bills-history')
	def form_valid(self, form):
		form.instance.source = self.request.user
		return super().form_valid(form)
	def get_form(self):
		form = super(BillAddView, self).get_form()
		form.fields['exp_date'].widget.attrs.update({'class' : 'datetimepicker'})
		return form

class BillEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	def get_success_url(self):
		return reverse('bills-history')
	model = Bill
	fields = ['exp_date','vsbilty','ammount']
	template_name ='bills/bill_form.html'
	def test_func(self):
		value = self.get_object()
		if self.request.user == value.source:
			return True
		return False

@login_required
def BillsHistoryView(request):
	Bills=Bill.objects.filter(source=request.user)
	
	context={'bills':Bills}
	return render(request,'bills/bills-list.html',context)

@login_required
def BillPayView(request,pk):
	bill=Bill.objects.get(pk=pk)
	if request.method=="POST" :
		form=BillPayForm(request.POST)
		form.instance.sender=request.user
		form.instance.receiver=bill.source
		form.instance.bill=bill
		if form.is_valid():
			
			form.save()
			messages.success(request, f'You Pay {form.instance.ammount}/{bill.ammount} for bill ID:{bill.id}')
			return redirect('bills-history')

	form=BillPayForm()
	form.fields['ammount'].widget.attrs.update({'value' : bill.ammount})
	return render(request,'bills/bill-pay.html',context={'form':form ,'bill':bill ,'status':status(bill) ,'repayment':repayments_sum(bill)})

@login_required
def BillDetailsView(request,pk):
	bill=Bill.objects.get(pk=pk)
	if request.method=='GET':
		if request.user==bill.source or bill.vsbilty==True:#or request.user in bill.pointer.reciver
			return render(request,'bills/bill-details.html'
				,context={'bill':bill ,'status':status(bill) ,'repayments_sum':repayments_sum(bill) ,'repayments':repayments(bill)})
	raise Http403("accies denay")

