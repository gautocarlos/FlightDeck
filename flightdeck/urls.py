from django.conf.urls.defaults import *
from django.views import static
from django.conf import settings   
from django.contrib import admin

from flightdeck.base import views as base_views

admin.autodiscover()

try:
	import grappelli
	urls = [(r'^grappelli/', include('grappelli.urls'))]
except:
	urls = []


urls.extend([
	# Example:
	url(r'^$',base_views.placeholder, name='placeholder'),

	# admin
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/', include(admin.site.urls)),

	# static files
	# this should be used only in development server
	url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

	# Jetpack
	(r'^user/', include('person.urls')),
	(r'^', include('jetpack.urls')),
])
urlpatterns = patterns('', *urls)