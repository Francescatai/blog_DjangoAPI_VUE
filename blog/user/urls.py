from django.urls import path
import views

urlpatterns = [
    path('<str:username>', views.UserViews.as_view()),
    path('<str:username>/avatar', views.user_avatar)
]