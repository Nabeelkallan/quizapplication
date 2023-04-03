from django.urls import path
from quizweb import views
from django.views.generic import TemplateView

urlpatterns=[
    path("register",views.SignUpView.as_view(),name="signup"),
    path("login",views.SignInView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="home"),
    path("quizes",views.QuizHomeView.as_view(),name="quiz_home"),
    path("questions/all/<str:cat>/<str:mode>",views.QuestionListView.as_view(),name="question_list"),
    path("quiz/record",views.QuizLIstView.as_view(),name="quiz_record")

]