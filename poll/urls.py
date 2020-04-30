from .views      import QuestionView, ResultView, PingView
from django.urls import path

urlpatterns = [
    path('/question', QuestionView.as_view()),
    path('/result', ResultView.as_view()),
]
