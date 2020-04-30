from django.contrib import admin
from django.urls import path,include
from . import  views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('login/', views.loginFn,name="login"),
    path('register/', views.registerFn,name="register"),
    path('logout/', views.logoutFn,name="logout"),
    path('post/<int:id>/', views.post),
    path('posts/', views.mypost),
    path('delete/<int:id>/', views.deletePost),
    path('like/<int:id>/', views.likePost),
    path('comment/<int:id>/', views.addComment),
    path('delete/<int:pid>/<int:cid>/', views.deleteComment),
    path("search/",views.searchFn),
    path("search/<int:id>/<int:userid>/",views.followingFN),
    path('', views.homeFn,name="home"),
    path('account/settings/',views.settingsFn,name='settings'),
    path('account/edit/',views.updateFn,name='edit'),
    path('account/password_change/', views.change_password, name='password_change'),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name = 'account/password_reset_form.html',subject_template_name = 'registration/password_reset_subject.txt'), name='password_reset'),
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(template_name = 'account/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name = 'account/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(template_name = 'account/password_reset_complete.html'), name='password_reset_complete'),
    path('account/delete/',views.deleteAccFn),
    path('<str:user>/profile/',views.myProfileFn),
    path('<str:username>/posts/',views.hispost),
    path('inbox/',views.messageList),
    path('inbox/<int:id>/',views.msgDelete),
    path('msg/<int:id>/',views.msgs),
    path('chat/<int:id>/',views.chat),



]



