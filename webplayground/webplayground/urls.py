from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from pages.urls import page_patterns

urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include(page_patterns)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
