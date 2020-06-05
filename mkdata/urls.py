from django.urls import path

from . import views

app_name = 'mkdata'
###urls.pyにもapp_nameをつけてる

urlpatterns = [
    #path('<int:pk>/', views.IndexView.as_view(), name='index'),
    path('<int:work_id>/', views.IndexView, name='index'),
    path('<int:work_id>/again/', views.IndexAgainView, name='index_again'),
    path('<int:work_id>/vote/', views.vote, name='vote'),
    #path('selectgenre/', views.SelectGenreView, name='selectgenre'),
    path('startfreevote/', views.StartFreevoteView.as_view(), name='startfreevote'),
    path('mkaddwork/', views.mkaddwork, name='mkaddwork'),
    path('freevote/<int:pk>/', views.AddWorkView.as_view(), name='freevote'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    #path('<int:work_id>/recommend/', views.recommend, name='recommend'),
    path('recommend/', views.recommend, name='recommend'),
    #path('detail/', views.detail,name='detail'),
    path('start/',views.StartView, name='start'),
    path('userread/',views.UserRead, name='userread'),
    path('selectfavorite/', views.SelectFavoriteView, name='selectfavorite'),
    path('selectfavoriteagain/', views.SelectFavoriteAgainView, name='selectfavoriteagain'),
    path('userselected/', views.UserSelected, name='userselected'),
    path('startSurvey/', views.StartSurveyView, name="startSurvey"),
    #path('usersee/', views.UserSee, name='usersee')
    #path('upload/', views.upload, name='upload'),
]