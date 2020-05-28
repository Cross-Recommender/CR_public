from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth import get_user_model
from django.contrib.auth.views import (
    LoginView,
)
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from .forms import CollectDataForm, AddWorkForm

from django.shortcuts import resolve_url

from cms.models import User

from .models import Work, mkbaseWorks, AddedWork

from .recommend import recommendsort


def IndexView(request, work_id):
    user = request.user

    '''
    # if user.work_read[work_id - 1] != "2":
    if int(user.work_read[work_id - 1]) <= 1:
        return HttpResponseRedirect(reverse('mkdata:index', args=(work_id + 1,)))

    try:
        work = Work.objects.get(pk=work_id)
    except:
        return HttpResponseRedirect(reverse('mkdata:index', args=(work_id + 1,)))
    '''

    work = Work.objects.get(pk=work_id)

    template = loader.get_template('mkdata/sampleform.html')

    # isLast = (work_id == Work.objects.all().order_by("-id")[0].id)
    isLast = (user.work_read[work_id - 1] == "3")

    context = {
        'work': work,
        'isLast': isLast,
        'user': user,
    }

    return HttpResponse(template.render(context, request))

###入力でエラーが出た時用, 汎用ビューとかをうまく使えば要らなくなるかも
def IndexAgainView(request, work_id):
    user = request.user

    '''
    # if user.work_read[work_id - 1] != "2":
    if int(user.work_read[work_id - 1]) <= 1:
        return HttpResponseRedirect(reverse('mkdata:index', args=(work_id + 1,)))

    try:
        work = Work.objects.get(pk=work_id)
    except:
        return HttpResponseRedirect(reverse('mkdata:index', args=(work_id + 1,)))
    '''

    work = Work.objects.get(pk=work_id)

    template = loader.get_template('mkdata/againform.html')

    # isLast = (work_id == Work.objects.all().order_by("-id")[0].id)
    isLast = (user.work_read[work_id - 1] == "3")

    context = {
        'work': work,
        'isLast': isLast,
        'user': user,
    }

    return HttpResponse(template.render(context, request))

'''汎用ビュー上では難しいか
class IndexView(DetailView):
    model = Work
    #model2 = User
    #work = get_object_or_404(Work, pk)
    form_class = CollectDataForm
    template_name = 'mkdata/sampleform.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す

        context['name'] = self.model.name
        #context['num_of_data'] = self.model.num_of_data
        #context['like'] = self.model.like
        #context['joy'] = self.model.joy
        #context['anger'] = self.model.anger
        #context['sadness'] = self.model.sadness
        #context['fun'] = self.model.fun
        #context['tech_constitution'] = self.model.tech_constitution
        #context['tech_story'] = self.model.tech_story
        #context['tech_character'] = self.model.tech_character
        #context['tech_speech'] = self.model.tech_speech
        #context['tech_picture'] = self.model.tech_picture

        return context

    #####
    #def get_form_kwargs(self):
    #    kwargs = super(IndexView, self).get_form_kwargs()
    #    kwargs['pk'] = self.model.id
    #    return kwargs
    #####


    #def get_success_url(self):
    #    return resolve_url('mkdata:vote', work_id=self.kwargs['pk'])


    #def form_valid(self, form):
    #    return super().form_valid(form)

'''


class ThanksView(TemplateView):
    template_name = "mkdata/thanks.html"


def vote(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    user = request.user
    try:
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

    except:
        return HttpResponseRedirect(reverse('mkdata:index_again', args=(work_id,)))

    work.save()

    obj = user.work_like

    if len(obj) != 100000:
        obj = "".join(['0'] * 100000)

    obj = list(obj)
    obj[work_id - 1] = request.POST['like']

    user.work_like = "".join(obj)

    user.save()

    # if work.id >= Work.objects.all().order_by("-id")[0].id:
    if user.work_read[work_id - 1] == "3":
        user.data_entered = True
        user.save()
        return HttpResponseRedirect(reverse('mkdata:recommend', ))
    else:
        next = work.id + 1
        while next <= Work.objects.all().order_by("-id")[0].id:
            try:
                x = Work.objects.get(id=next)
            except:
                next += 1
            else:
                if int(user.work_read[next-1])  >= 2:
                    break
                else:
                    next += 1

        return HttpResponseRedirect(reverse('mkdata:index_again', args=(next,)))


class AddWorkView(CreateView):
    # print("1")
    # model = AddedWork
    # modelはAddWorkFormで指定しているのでいらない
    form_class = AddWorkForm
    template_name = 'mkdata/addwork.html'
    success_url = reverse_lazy('mkdata:thanks')

    def form_valid(self, form):
        '''
        #createviewの場合オブジェクトの保存は自動で行われる。
        work = form.save()
        self.object = work
        追記
        super().form_valid(form)
        について理解しましたがuseridを追加する方法がわからずこちらの方法にしました。
        '''
        self.object = form.save()
        self.object.userid = self.request.user.id
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


'''
def recommend(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    works = work.recommendsort(5)
    return render(request, 'mkdata/recommend.html', {'works': works})
'''


###フォーム入力後にすぐにオススメ5作品のページへ飛べるよう改良
def recommend(request):
    user = request.user
    if user.data_entered is None:
        user.data_entered = False
        user.save()

    OrderedWork = mkbaseWorks(user.work_like)[:4]
    #print(user.work_like[:10])
    #print(OrderedWork)
    if OrderedWork is None:
        OrderedWork = AddedWork.objects.filter(userid=user.id).order_by('-like')[0:3]
    #print(OrderedWork)
    if OrderedWork is None:
        return render(request, 'mkdata/no_recommendation.html')
    works = []
    for work in OrderedWork:
        #print(len(works))#なぜか作品が6つ以上表示された時のバグ確認用
        cand_works = recommendsort(work, 5)
        # print(OrderedWork[num], cand_works)
        for i in range(4):
            # print((cand_works[i] in works) == False,user.work_like[cand_works[i].id-1] == '0')
            if (cand_works[i] in works) == False and user.work_like[cand_works[i].id-1] == '0':
                ###work_readは一時的な記録に過ぎないため, ユーザが読んだかどうかの判定は
                ###user.work_like[cand_works[i].id-1] == '0'で行う
                works.append(cand_works[i])
            if len(works) >= 5:
                break
        if len(works) >= 5:
            break

    return render(request, 'mkdata/recommend.html', {'works': works, 'user': user})


def StartView(request):
    works = Work.objects.all()
    user = request.user
    return render(request, 'mkdata/start_mkdata.html', {'works': works, 'user': user, })


def UserRead(request):
    user = request.user
    works = Work.objects.all()

    if user.work_read is None:
        X = ['0'] * 100000
    else:
        X = list(user.work_read)

    for work in works:
        X[work.id - 1] = "1"

    isRead = request.POST.getlist('isRead')

    if isRead == []:
        user.data_entered = True
        user.save()
        return HttpResponseRedirect(reverse('mkdata:recommend', ))

    for num in isRead:
        print(num)
        X[int(num) - 1] = "2"
    X[max(map(int, isRead)) - 1] = "3"  # isLastに使いたい

    user.work_read = "".join(X)
    user.save()

    first = 1
    while first <= Work.objects.all().order_by("-id")[0].id:
        try:
            x = Work.objects.get(id=first)
        except:
            first += 1
        else:
            if int(user.work_read[first-1]) >= 2:
                break
            else:
                first += 1
    return HttpResponseRedirect(reverse('mkdata:index', args=(first,)))
