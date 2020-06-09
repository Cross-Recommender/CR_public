from django.urls import path

from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    ###試しにBeforeTopViewを実装しました。必要ならすぐ消します
    #path('genuine/', views.TopView.as_view(), name='genuine_top'),
    #path('', views.BeforeTopView, name='top'),
    ###
    path('infomation/', views.InfomationView.as_view(), name='infomation'),
    path('terms/', views.TermsView.as_view(), name='terms'),
    path('policy/', views.PolicyView.as_view(), name='policy'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('guestdelete/', views.GuestDelete, name='guestdelete'),
    path('signup/', views.UserCreate.as_view(), name='signup'),
    path('signupagain/', views.UserCreateAgain.as_view(), name='signupagain'),
    path('guest/', views.GuestCreate.as_view(), name='guest'),
    path('guestagain/', views.GuestCreateAgain.as_view(), name='guestagain'),
    #path('guesttorealuser/', views.GuestToRealUser.as_view(), name='guestupdate'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'), #追加
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'), #追加
    path('user/<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    #path('user/', views.UserList.as_view(), name='user_list'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='user_delete'),
    #path('user/<int:pk>/recommend/', views.RecommendView.as_view(), name='user_recommend'),
    #path('works/<int:pk>/', views.WorksView.as_view(), name='works'),
    #path('works/', views.WorksList.as_view(), name='works_list'),
]
