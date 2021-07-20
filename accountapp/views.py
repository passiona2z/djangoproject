from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


# 아주 간단한 뷰
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accountapp.models import NewModel


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        model_instance = NewModel()       # 저장하는 과정
        model_instance.text = temp
        model_instance.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))


    else :
        data_list = NewModel.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'data_list': data_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html' # 나중에 만들것 : 이렇게 로직이 완성되었다.


class AccountDetailView(DetailView) :
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView) :
    model = User
    form_class = UserCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hell5o_world')
    template_name = 'accountapp/update.html'