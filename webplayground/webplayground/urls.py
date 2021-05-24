from django.contrib import admin
from django.urls import path, include

from pages.urls import page_patterns

urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include(page_patterns)),
    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
]
