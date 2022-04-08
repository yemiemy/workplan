from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="WorkPlan API Documentation",
      default_version='v1',
      description="Detailed documentation of the API schema",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="rasholayemi@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("core.urls")),
    path('docs/', include_docs_urls(title="WorkPlan API Documentation")),
    path('api-auth/', include("rest_framework.urls")),



    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]
