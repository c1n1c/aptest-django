# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from django.conf import settings
from django.contrib import admin

from views import *


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^~admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^~admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^~upload/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns('',
    url(r'^(?P<path>%s)?add/$' % settings.PAGE_PATH_RE, PageAddView.as_view(), name='page-add'),
    url(r'^(?P<path>%s)edit/$' % settings.PAGE_PATH_RE, PageEditView.as_view(), name='page-edit'),
    url(r'^(?P<path>%s)$' % settings.PAGE_PATH_RE, PageView.as_view(), name='page'),
)
