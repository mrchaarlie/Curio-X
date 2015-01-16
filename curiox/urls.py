from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'curiox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^game/', include('game.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
