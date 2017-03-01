from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from app01 import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'day13.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #peizhizhengce
    url(r'^index/(\d*)/',views.index),
)
