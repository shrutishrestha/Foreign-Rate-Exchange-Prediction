
from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static


from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^prediction/', include('prediction.urls')),
<<<<<<< HEAD
    url(r'^tech/', include('tech.urls')),
=======
    url(r'^backpropagation/', include('backpropagation.urls')),
>>>>>>> 78fd1182ea3d7aa4d4e2e74025f0d9df075fc991

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
