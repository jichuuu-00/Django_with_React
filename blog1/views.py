from django.shortcuts import render
from .models import Post

def post_list(request):
    # 데이터베이스로부터 모든 posting을 가져올 예정
    qs = Post.objects.all() #QuerySet
    # 그 목록을 넘겨줌
    return render(request, 'blog1/post_list.html', {
        'post_list' : qs,
    })