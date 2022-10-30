from api import views
from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path(
        "openapi",
        get_schema_view(
            title="Veloce",
            description="Rin's Commands API rebuilt with Django Rest Framework",
            version="0.1.0",
        ),
        name="openapi-schema",
    ),
    path(
        "redoc/",
        TemplateView.as_view(
            template_name="redoc.html", extra_context={"schema_url": "openapi-schema"}
        ),
        name="redoc",
    ),
    path("commands/all", views.GetAllCommands.as_view()),
    path("commands/module/<str:cog>", views.GetModuleCommands.as_view()),
    path("modules/all", views.GetAllModules.as_view()),
]
