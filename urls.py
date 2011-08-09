from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog.models import Artigo
from blog.feeds import UltimosArtigos

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog_django.views.home', name='home'),
    # url(r'^blog_django/', include('blog_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^$', 'django.views.generic.date_based.archive_index', 
	    {'queryset': Artigo.objects.all(), 'date_field': 'publicacao'}),

    (r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
	    {'feed_dict': {'ultimos': UltimosArtigos }}),

    (r'^artigo/(?P<artigo_id>\d+)/$', 'blog.views.artigo'),

    (r'^contato/$', 'views.contato'),

    (r'^comments/', include('django.contrib.comments.urls')),
)

if settings.LOCAL:
	urlpatterns += patterns('',
			(r'^media/(.*)$', 'django.views.static.serve',
				{'document_root': settings.MEDIA_ROOT}),
			)
