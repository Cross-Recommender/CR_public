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

'''
from .forms import (
    LoginForm,
)
'''
from .models import Work


class IndexView(TemplateView):
    #form_class = LoginForm
    model = Work
    template_name = 'mkdata/sampleform.html'

def vote(request, work_id):
    work = get_object_or_404(Work, pk=work_id)

    '''
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    '''
    #return HttpResponseRedirect(reverse('mkdata:index', args=(work.id+1,)))
    return HttpResponseRedirect(reverse('mkdata:index'))