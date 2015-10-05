from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from stream import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^stream/', views.stream)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
