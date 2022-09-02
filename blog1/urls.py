from django.urls import path

from .import views

urlpatterns = [
    # 함수를 넘기는 거
    path('', views.post_list, name="post_list"),

]