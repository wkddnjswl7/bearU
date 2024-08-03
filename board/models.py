from django.db import models
from user.models import User    #이 유저는 user 앱에서 만든 User임

#익명 게시판
class Post(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE) : User가 글 쓴 것이라고 FK로 지정, User가 탈퇴 시 User 정보도 함께 삭제시킨다.
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) : User가 글 쓴 것이라고 FK로 지정, User가 탈퇴하도 글은 삭제하지 않아 값을 Null이 된다.(null값을 허용)
    # post 라는 모델을 설정할 때 굳이 PK를 설정하지 않고 그냥 그대로 두면 Django에서 내부적으로 ID라는 값으로 PK를 하나 만든다.
    # id = models.AutoField(primary_key=1) 기본키로 설정
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField()

    #글이 새로 생성되었을 때 default 값으로 생성됐을 때 당시의 시간을 저장
    reg_date = models.DateTimeField(auto_now_add=True)

    #값이 들어가도되고 안들어가도 된다.
    img_url = models.URLField(null=True)


    class Meta:
        #만약 테이블 이름을 지정하지않으면 app_model이름으로 만들어진다.(Ex, board_post 로 만들어진다.)
        db_table="post"

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
         db_table="db_table"