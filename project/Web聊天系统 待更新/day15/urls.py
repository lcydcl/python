from django.conf.urls import patterns, include, url
from app01 import  views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'day15.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^$',views.index),
    url(r'^login/$',views.login),
    url('^index/$',views.index),
    url(r'^room/(\d+)/$',views.room), 
    
)
