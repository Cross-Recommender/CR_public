from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import (
    LoginView, LogoutView,
)
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import (
    CreateView, UpdateView,DeleteView,
)

from .mixins import OnlyYouMixin
from .forms import (
    LoginForm, UserCreateForm, UserUpdateForm,
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from mkdata import models as mkdata_models

from django.urls import reverse


UserModel = get_user_model()


class TopView(TemplateView):
    template_name = 'cms/top.html'

class InfomationView(TemplateView):
    template_name = 'cms/infomation.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'cms/login.html'

class Logout(LogoutView):
    template_name = 'cms/top.html'

class UserCreate(CreateView):
    form_class = UserCreateForm
    template_name = 'cms/signup.html'
    success_url = reverse_lazy('cms:top')

    def form_valid(self, form):
        if not self.request.POST.getlist('isOK'):
            return HttpResponseRedirect(reverse('cms:signupagain', ))
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

class UserCreateAgain(CreateView):
    form_class = UserCreateForm
    template_name = 'cms/signupagain.html'
    success_url = reverse_lazy('cms:top')

    def form_valid(self, form):
        if not self.request.POST.getlist('isOK'):
            return HttpResponseRedirect(reverse('cms:signupagain', ))
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

class UserUpdate(OnlyYouMixin, UpdateView):
    model = UserModel
    form_class = UserUpdateForm
    template_name = 'cms/user_update.html'

    def get_success_url(self):
        return resolve_url('cms:user_detail', pk=self.kwargs['pk'])

class UserDetail(DetailView):
    model = UserModel
    template_name = 'cms/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

class UserList(ListView):
    model = UserModel
    template_name = 'cms/user_list.html'

class UserDelete(OnlyYouMixin, DeleteView):
    model = UserModel
    template_name = 'cms/user_delete.html'
    success_url = reverse_lazy('cms:top')

"""
class RecommendView(ListView):
    model = UserModel
    template_name = 'cms/user_recommend.html'

"""
class RecommendView(DetailView):
    model = UserModel
    template_name = 'cms/user_recommend.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        user = context['object']
        context['recommends'] = mkdata_models.mkbaseWorks(user.work_like)
        return context

class WorksView(DetailView): #作品紹介をみるためのページ用
    model = mkdata_models.Work
    template_name = "cms/works.html"

class WorksList(ListView):
    model = mkdata_models.Work
    template_name = "cms/works_list.html"

class TermsView(TemplateView):
    template_name = "cms/terms.html"

class PolicyView(TemplateView):
    template_name = 'cms/policy.html'