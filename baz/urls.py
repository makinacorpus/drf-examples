from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import MyWebView
from .viewsets import BazViewSet

router = DefaultRouter()
router.register('api/bar', BazViewSet)

urlpatterns = [
    url(r'^web/baz/mywebview/$', MyWebView.as_view(), name='mywebview'),
]
urlpatterns += router.urls
