from django.conf.urls import patterns, include, url
from django.contrib import admin
from lms.views import Home, ClassDetail

urlpatterns = patterns('',

    url(regex=r'^$',
        view=Home.as_view(),
        name='home_view'),

    url(regex=r'^class/(?P<slug>\w+)/$',
        view=ClassDetail.as_view(),
        name='class_view'),

    url(r'^admin/', include(admin.site.urls)),
)
