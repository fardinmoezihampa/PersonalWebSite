from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from PesonalWebSite import settings

urlpatterns = [
    path('', include('Home.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
