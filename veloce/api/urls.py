from api import views
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

description = """
Rin's commands API completely rebuilt using Django Rest Framework

This API is public, and is built on DRF. Unlike the other one, which is built on FastAPI, this API almost does the exact same thing

Fun fact: Veloce means "fast" in Italian.

GitHub:

- [Rin](https://github.com/No767/Rin)
- [Veloce](https://github.com/No767/Veloce)
"""
schema_view = get_schema_view(
    openapi.Info(
        title="Veloce",
        default_version="v0",
        description=description,
        contact=openapi.Contact(name="No767"),
        license=openapi.License(name="GPL-3.0"),
    ),
    public=True,
)

urlpatterns = [
    re_path(
        r"^docs/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("commands/all", views.GetAllCommands.as_view()),
    path("commands/module/<str:cog>", views.GetModuleCommands.as_view()),
    path("modules/all", views.GetAllModules.as_view()),
]
