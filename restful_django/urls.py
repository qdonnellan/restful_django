from django.conf.urls import patterns, include, url
from main_app.views import ExampleView
from restful_api.routers import router as api_router
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', ExampleView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api_router.urls)),
)

