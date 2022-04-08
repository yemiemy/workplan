from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='WorkPlan API Documentation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("core.urls")),
    path('docs/', include_docs_urls(title="WorkPlan API Documentation")),
    # path('', get_schema_view(
    #     title="WorkPlan API Documentation",
    #     description="Detailed documentation of the API schema",
    #     version="1.0.0"
    # ), name="schema")
    path('', schema_view),

    path('api-auth/', include("rest_framework.urls"))
]
