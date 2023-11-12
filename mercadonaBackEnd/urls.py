"""mercadonaBackEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

from mercadonaBackEnd.settings import env

# Creation of API documentation
schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Mercadona API",
        default_version="1.0.0",
        description="Api documentation of Mercadona App"
    ),
    public=True,
    url=env('SWAGGER_URL')

)

# creating main routes for back end application
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/',
         include([
             path('', include('Catalog.urls')),
             path('', include('Accounts.urls')),
             path('auth/', include('dj_rest_auth.urls')),
             path('swagger/schema', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
             path('swagger/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
            ])),
] + static(settings.STATIC_URL,
           document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                        document_root=settings.MEDIA_ROOT)

