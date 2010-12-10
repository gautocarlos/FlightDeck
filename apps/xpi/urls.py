" XPI URL definitions "

from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('xpi.views',
    # test Add-on's PackageRevision
    url(r'^prepare_test/(?P<id_number>[-\w]+)/revision/(?P<revision_number>\d+)/$',
        'prepare_test', name='jp_addon_revision_test'),
    url(r'^prepare_download/(?P<id_number>[-\w]+)/revision/(?P<revision_number>\d+)/$',
        'prepare_download', name='jp_addon_revision_xpi'),

    # get and remove created XPI
    url(r'^test/(?P<sdk_name>.*)/(?P<pkg_name>.*)/(?P<filename>.*)/$',
        'get_test', name='jp_test_xpi'),
    url(r'^download/(?P<sdk_name>.*)/(?P<pkg_name>.*)/(?P<filename>.*)/$',
        'get_download', name='jp_download_xpi'),
    url(r'^remove/(?P<sdk_name>.*)/$', 'clean', name='jp_rm_xpi'),
)