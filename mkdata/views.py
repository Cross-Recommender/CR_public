from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.contrib.auth import get_user_model
from django.contrib.auth.views import (
    LoginView,
)
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView

from .forms import CollectDataForm

from django.shortcuts import resolve_url

'''
from .forms import (
    LoginForm,
)
'''
from .models import Work


class IndexView(DetailView):
    model = Work
    #work = get_object_or_404(Work, pk)
    form_class = CollectDataForm
    template_name = 'mkdata/sampleform.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す

        ###クラス継承 FormViewに含まれるメソッドget_context_dataを呼んでくる
        ###kwargsにはmodelも入ってるっぽい
        ###エラー出たな入ってないんか
        ###self.modelにしたらいけた

        context['name'] = self.model.name
        '''
        context['num_of_data'] = self.model.num_of_data
        context['like'] = self.model.like
        context['joy'] = self.model.joy
        context['anger'] = self.model.anger
        context['sadness'] = self.model.sadness
        context['fun'] = self.model.fun
        context['tech_constitution'] = self.model.tech_constitution
        context['tech_story'] = self.model.tech_story
        context['tech_character'] = self.model.tech_character
        context['tech_speech'] = self.model.tech_speech
        context['tech_picture'] = self.model.tech_picture
        '''

        return context

    #####
    #def get_form_kwargs(self):
    #    kwargs = super(IndexView, self).get_form_kwargs()
    #    kwargs['pk'] = self.model.id
    #    return kwargs
    #####

    '''
    def get_success_url(self):
        return resolve_url('mkdata:vote', work_id=self.kwargs['pk'])


    def form_valid(self, form):
        return super().form_valid(form)
    '''


def vote(request, work_id):
    work = get_object_or_404(Work, pk=work_id)

    work.num_of_data += 1
    work.like += int(request.POST['like'])
    work.joy += int(request.POST["joy"])
    work.anger += int(request.POST["anger"])
    work.sadness += int(request.POST["sadness"])
    work.fun += int(request.POST["fun"])
    work.tech_constitution += int(request.POST["tech_constitution"])
    work.tech_story += int(request.POST["tech_story"])
    work.tech_character += int(request.POST["tech_character"])
    work.tech_speech += int(request.POST["tech_speech"])
    work.tech_picture += int(request.POST["tech_picture"])

    work.save()

    return HttpResponseRedirect(reverse('mkdata:index', args=(work.id + 1,)))
