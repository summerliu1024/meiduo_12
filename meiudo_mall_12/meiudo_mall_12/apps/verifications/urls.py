from django.conf.urls import url

from verifications import views

urlpatterns = [
    url('^image_codes/(?P<image_code_id>[\w-]+)/$', views.ImageCodeView.as_view()),
]
