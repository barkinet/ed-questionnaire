# vim: set fileencoding=utf-8

from django.conf.urls import *
from views import *


urlpatterns = patterns(
    '',
    url(r'^$',
        questionnaire, name='questionnaire_noargs'),
    url(r'^csv/(?P<qid>\d+)/$',
        export_csv, name='export_csv'),
    url(r'^(?P<runcode>[^/]+)/progress/$',
        get_async_progress, name='progress'),
)

if not use_session:
    urlpatterns += patterns(
        '',
        url(r'^(?P<runcode>[^/]+)/(?P<qs>[-]{0,1}\d+)/$',
            questionnaire, name='questionset'),
        url(r'^(?P<runcode>[^/]+)/$',
            questionnaire, name='questionnaire'),
        url(r'^(?P<runcode>[^/]+)/(?P<qs>[-]{0,1}\d+)/prev/$',
            redirect_to_prev_questionnaire,
            name='redirect_to_prev_questionnaire'),
    )
else:
    urlpatterns += patterns(
        '',
        url(r'^$',
            questionnaire, name='questionnaire'),
        url(r'^prev/$',
            redirect_to_prev_questionnaire,
            name='redirect_to_prev_questionnaire')
    )
