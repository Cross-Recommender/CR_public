from django.urls import path

from . import views

app_name = 'mkdata'
###urls.pyにもapp_nameをつけてる

urlpatterns = [
    #path('<int:pk>/', views.IndexView.as_view(), name='index'),
    path('<int:work_id>/', views.IndexView, name='index'),
    path('<int:work_id>/again/', views.IndexAgainView, name='index_again'),
    path('<int:work_id>/vote/', views.vote, name='vote'),
    path('freevote/', views.AddWorkView.as_view(), name='freevote'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    #path('<int:work_id>/recommend/', views.recommend, name='recommend'),
    path('recommend/', views.recommend, name='recommend'),
    #path('detail/', views.detail,name='detail'),
    path('start/',views.StartView, name='start'),
    path('userread/',views.UserRead, name='userread'),
]