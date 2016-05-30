from django.conf.urls import url
from django.conf import settings
from django.views.generic import TemplateView
from pastebin.views import index, paste_details, plain, html

urlpatterns = [
    url(r'^$', index, name='djpaste_index'),
    url(r'^help/$', TemplateView.as_view(template_name='djpaste/help.html')),
    url(r'^paste/(?P<id>\d+)/$', paste_details, name='djpaste_paste_details'),
    url(r'^plain/(?P<id>\d+)/$', plain, name='djpaste_plain'),
    url(r'^html/(?P<id>\d+)/$', html, name='djpaste_html'),
]

urlpatterns += [
    url(r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
]
