from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import CreateView ,ListView
from .models import Transfere
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import CreateTransfereForm
'''
class TransfereCreateView(LoginRequiredMixin, CreateView):
	model = Transfere
	fields = ['ammount', 'receiver']
	form.instance.sender = request.user

'''
def TransfereCreateView(request):
	#this True for valid user 
	if request.user.is_authenticated and True:
		if request.method=='POST':
			form=CreateTransfereForm(request.POST)
			form.instance.sender=request.user
			try:
				form.save()
				messages.success(request, 'Transfere completed successfuly')
				return redirect('my-trans-history')
			except Exception as e:
				messages.error(request, 'sender balance is not enough')
				return redirect("new-trans")
		else:
			form= CreateTransfereForm()
			return render(request,"transfere_form.html",{'form':form})
	else:
		return HttpResponse(status=403)

class TransfereListView(LoginRequiredMixin,ListView):
	model = Transfere
	template_name = 'transferes/user_transferes.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'transferes'
	paginate_by = 5

	def get_queryset(self):
		user = self.request.user
		return Transfere.objects.filter(Q(sender=user)|Q(receiver=user)).order_by('-create_date')