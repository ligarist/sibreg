from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "Cook"
urlpatterns = [
    url(r'^recipes/$', views.CookList, name='CookList'),
    url(r'^recipes/(?P<category_slug>[-\w]+)/$', views.CookList, name='CookListByCategory'),
    url(r'^recipes/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.CookDetail, name='CookDetail'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)