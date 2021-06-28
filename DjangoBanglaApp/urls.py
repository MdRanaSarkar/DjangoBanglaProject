from django.urls import path

from .views import QuestionClass,SingleQuestion,choice_view,results_showing,vote
app_name="DjangoBanglaApp"
urlpatterns=[
path("",QuestionClass.as_view(),name="qeustion"),
path("<int:pk>/",SingleQuestion.as_view(),name="idshow"),
path("allchoice/",choice_view,name="choice_view"),
path('<int:question_id>/result/',results_showing,name="result"),
path("<int:question_id>/vote/",vote,name="vote")


]