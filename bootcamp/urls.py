from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bootcamp.feeds.views.feeds', name='feeds'),
    url(r'^post/$', 'bootcamp.feeds.views.post', name='post'),
    url(r'^questions/$', 'bootcamp.questions.views.questions', name='questions'),
    url(r'^questions/(\d+)/$', 'bootcamp.questions.views.question', name='question'),
    url(r'^questions/answered/$', 'bootcamp.questions.views.answered', name='answered'),
    url(r'^questions/unanswered/$', 'bootcamp.questions.views.unanswered', name='unanswered'),
    url(r'^questions/ask/$', 'bootcamp.questions.views.ask', name='ask'),
    url(r'^questions/answer/$', 'bootcamp.questions.views.answer', name='answer'),
    url(r'^questions/answer/accept/$', 'bootcamp.questions.views.accept', name='accept'),
    url(r'^questions/answer/vote/$', 'bootcamp.questions.views.vote', name='vote'),
    url(r'^admin/', include(admin.site.urls)),
)