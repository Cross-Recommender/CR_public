from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
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

from cms.models import User

'''
from .forms import (
    LoginForm,
)
'''
from .models import Work


class IndexView(DetailView):
    model = Work
    ###
    #model2 = User
    ###
    #work = get_object_or_404(Work, pk)
    form_class = CollectDataForm
    template_name = 'mkdata/sampleform.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す

        context['name'] = self.model.name
        #context['username'] = self.model2.username
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

class ThanksView(TemplateView):
    template_name = "mkdata/thanks.html"

def vote(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    user = request.user

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

    obj = user.work_like
    '''
    #少し間違いがありそうなので, もし戻すときは注意
    if len(obj) < 2*work.id:
        obj = obj[:len(obj) - 1]
        while len(obj) < 2*(work.id-1):
            obj.append('0,')
        obj.append(',')
        obj.append(request.POST['like'])
        obj.append('}')
    else:
        obj[2*work.id-1] = request.POST['like']
    '''
    if len(obj) != 200:
        obj = "".join(['0']*200)

    obj = list(obj)
    obj[work_id-1] = request.POST['like']

    user.work_like = "".join(obj)

    user.save()

    if work.id >= Work.objects.count():
        return HttpResponseRedirect(reverse('mkdata:thanks',))
    else:
        return HttpResponseRedirect(reverse('mkdata:index', args=(work.id + 1,)))
