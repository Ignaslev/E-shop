from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hwstore/', include('hwstore.urls')),
    path('', RedirectView.as_view(url='hwstore/', permanent=True)),
]
