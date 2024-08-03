from django.urls import path # type: ignore
from board.views import board
from user.views import signin

urlpatterns = [
    path("", board, name="board"),
    path("user/signin", signin, name="signin")
]
