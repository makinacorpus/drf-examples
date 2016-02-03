from django.conf.urls import include, url

urlpatterns = [
    # Some Web views
    url(r'^foo/', include('foo.urls', namespace='foo')),
    url(r'^bar/', include('bar.urls', namespace='bar')),
    url(r'^baz/', include('baz.urls', namespace='baz')),
    # API views
    url(r'^api/v1/', include('example.v1_urls', namespace='v1')),
    url(r'^api/v2/', include('example.v2_urls', namespace='v2')),
    url(r'^api/v3/', include('example.v3_urls', namespace='v3')),
]
