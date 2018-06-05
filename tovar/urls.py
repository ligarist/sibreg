from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import e_handler404, e_handler500

app_name = 'tovar'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^catalog/$', views.ProductList, name='ProductList'),
    url(r'^catalog/(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^catalog/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
    url(r'^recipes/', include('cook.urls', namespace="Сook")),
    url(r'^contact/$', views.Price.as_view(), name='contact'),
    url(r'^about/$', views.about, name='about'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = e_handler404
handler500 = e_handler500