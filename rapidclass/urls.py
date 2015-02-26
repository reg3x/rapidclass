from django.conf.urls import patterns, include, url
from django.contrib import admin
from lms.views import Home, ClassDetail

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Home.as_view()),
    url(regex=r'^class/(?P<slug>\w+)/$',
        view=ClassDetail.as_view(),
        name='home_view'),

    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
