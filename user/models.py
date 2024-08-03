from django.db import models
from django.contrib.auth.models import AbstractUser

#AbstractBaseUser : django의 최소 user model
#(필드: 비밀번호, 마지막 로그인, 활성여부 3가지만 존재, 최소한의 함수만 존재)
# - 따라서, 로그인 시 필요한 필드 등 많은 부분이 커스텀 가능
# - 하지만, django의 유저 관련 함수 등 많은 부분이 커스텀 가능

#아무것도 작성하지않고 기본 유저 사용
#나만의 필드를 좀 더 추가해서 커스텀한 user model을 사용(사용)
# - django 기본 유저 모델(이것 저것 많이 포함되어있음, 각종 필드, 각종 함수(유저 생성, 유저 인증 등등)

class User(AbstractUser) :
    #테이블 컬럼에 닉네임이라는 필드 생성됨 (최대 길이 30)
    nickname = models.CharField(max_length=30)

    class Meta:
        db_table="user" #테이블 이름
