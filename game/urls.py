from django.conf.urls import patterns, url

from game import views

urlpatterns = patterns('',
    url(r'^index$', views.index, name='index'),
    url(r'^game$', views.game, name='game'),
    url(r'^game2$', views.game2, name='game2'),
    url(r'^game-splash$', views.gameSplash, name='game-splash'),
    url(r'^game2-splash$', views.game2Splash, name='game2-splash'),
    url(r'^post$', views.game_submit_task, name='submit'),
    url(r'^post2$', views.game2_submit_task, name='submit2'),
)
