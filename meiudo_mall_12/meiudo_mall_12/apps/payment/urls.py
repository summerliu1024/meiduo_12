from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    url(r'^orders/(?P<order_id>\d+)/payment/$', views.PaymentView.as_view()),
    url(r'^payment/status/$', views.PaymentStatusView.as_view()),

]
