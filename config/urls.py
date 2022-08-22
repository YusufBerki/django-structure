from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Pages
    path('user/', include('apps.user.pages.urls')),

    # API's
    path('api/user/', include('apps.user.api.urls')),

]
