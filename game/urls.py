from django.conf.urls import patterns, url

from game import views

urlpatterns = patterns('',
    url(r'^index.html$', views.index, name='index'), # JS can't link to url patterns != file name
    url(r'^game.html$', views.game, name='game'),
#    url(r'^$', views.current_datetime, name='now'),
)
