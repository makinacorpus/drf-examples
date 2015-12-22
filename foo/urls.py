from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^mywebview/$', views.MyWebView.as_view(), name='mywebview'),
]
