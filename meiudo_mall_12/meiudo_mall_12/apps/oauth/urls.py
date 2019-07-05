from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from oauth import views

urlpatterns = [
    url(r'^qq/authorization/$', views.QQAuthURLView.as_view()),
]
