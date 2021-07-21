from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


# 아주 간단한 뷰
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.models import NewModel
from accountapp.templates.accountapp.forms import AccountCreationForm


def hello_world(request):
    if request.user.is_authenticated: # 인증과정 구현
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
    else :
        return HttpResponseRedirect(reverse('accountapp:login')) # 로그인 안되면 로그인하라고


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
    form_class = AccountCreationForm     # 서버단에서 폼을 변경 (* 웹에서 수정은 다양한 변수가 있을 수 있음)
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))


class AccountDeleteView(DeleteView) :
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))