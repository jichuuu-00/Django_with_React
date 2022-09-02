from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post

@admin.register(Post) # Wrapping 감싼 대상의 기능을 변강할 수 있음
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message','message_length', 'is_public','create_at','update_at']
    list_display_links = ['message']
    list_filter = ['create_at','is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src= "{post.photo.url}" style="width: 72px;"/>')
        return None

    # 매번 post 객첵가 넘어옴 admin이 알아서 호출
    def message_length(self, post):
        return f"{len(post.message)} 글자"
