from django.urls import path

from . import views

app_name = 'mkdata'
###urls.pyにもapp_nameをつけてる

urlpatterns = [
    path('<int:pk>/', views.IndexView.as_view(), name='index'),
    path('<int:work_id>/vote/', views.vote, name='vote'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('<int:work_id>/recommend/', views.recommend, name='recommend')
]