from django.conf.urls import url

from . import views

app_name = "sprinkler"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^submit$', views.submit, name="submit"),
    url(r'^(?P<sprinkler_id>[0-9]+)$', views.act, name="act"),
    url(r'^error$', views.error, name="error"),
    url(r'^temp$', views.temp, name="temp"),
    url(r'^get_temp', views.get_temp, name="get_temp"),
    url(r'^lights$', views.lights, name="lights")
]