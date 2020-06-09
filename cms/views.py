from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
)
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import (
    CreateView, UpdateView,DeleteView,
)

from .mixins import OnlyYouMixin
from .forms import (
    LoginForm, UserCreateForm, UserUpdateForm, GuestCreateForm
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from mkdata import models as mkdata_models

from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin


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

def GuestDelete(request):
    user = request.user
    print(user)
    if user.is_authenticated == False:
        return HttpResponseRedirect(reverse('cms:top', ))
    if user.is_guest == True:
        user.delete()
        return HttpResponseRedirect(reverse('cms:top', ))
    else:
        return HttpResponseRedirect(reverse('cms:logout', ))



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

class GuestCreate(CreateView):
    form_class = GuestCreateForm
    template_name = 'cms/guest.html'
    success_url = reverse_lazy('mkdata:start')

    def form_valid(self, form):
        if not self.request.POST.getlist('isOK'):
            return HttpResponseRedirect(reverse('cms:guestagain', ))
        user = form.save()
        login(self.request, user)
        user.is_guest = True
        user.save()
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

class GuestCreateAgain(CreateView):
    form_class = GuestCreateForm
    template_name = 'cms/guestagain.html'
    success_url = reverse_lazy('mkdata:start')

    def form_valid(self, form):
        if not self.request.POST.getlist('isOK'):
            return HttpResponseRedirect(reverse('cms:guestagain', ))
        user = form.save()
        login(self.request, user)
        user.is_guest = True
        user.save()
        self.object = user
        return HttpResponseRedirect(self.get_success_url())

'''
class GuestToRealUser(UpdateView):
    model = UserModel
    form_class = GuestToRealUserForm
    template_name = 'cms/guest_password_change.html'

    def get_success_url(self):
        return resolve_url('cms:user_detail', pk=self.kwargs['pk'])
'''

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    """パスワード変更ビュー"""
    success_url = reverse_lazy('cms:password_change_done')
    template_name = 'cms/password_change.html'
    def form_valid(self, form):
        super(PasswordChange, self).form_valid(form)
        self.request.user.tmppass = None
        self.request.user.is_guest = False
        self.request.user.save()
        return HttpResponseRedirect(self.get_success_url())


class PasswordChangeDone(LoginRequiredMixin,PasswordChangeDoneView):
    """パスワード変更完了"""
    template_name = 'cms/password_change_done.html'


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
