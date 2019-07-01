from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView

# url('^image_codes/(?P<image_code_id>[\w-]+)/$', views.ImageCodeView.as_view()),
class ImageCodeView(APIView):
    """
    图片验证码
    """
    pass
