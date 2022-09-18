from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list,) # 함수 그 자체를 넘기는 것으로 호출 안되게 해야함
    path('<int:pk>', views.post_detail),
]