from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mainapp.urls', namespace='main')),

    path('admin/', admin.site.urls),
    path('accounts/',
         include(('django.contrib.auth.urls', 'auth'), namespace='auth')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
