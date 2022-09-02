from django.db import models

class Post(models.Model):
    # blank와 null default 값 false
    # 메세지라는 값이 없다면(빈 문자열을 지정한다면), 모델과 연동된 장고 Form에서 유효성 검사를 수행하는데 실패하게 됨
    # Form을 사용하지 않고 모델만 활용해서 저장하면 유효성 검사 로직을 타지 않음
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # Java의 toString과 유사
    def __str__(self):
        # return "Custom Post object ({})".format(self.id)
        # return f"Custom Post object ({self.id})"
        return self.message

    # def message_length(self):
    #     return len(self.message)
    # # 이름 변경
    # message_length.short_description ="메세지 글자수"
