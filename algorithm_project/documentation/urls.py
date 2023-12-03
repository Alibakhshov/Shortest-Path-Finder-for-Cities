from django.urls import path
from documentation.views import (
   introduction_view,
   installation_view,
   customization_view,
   changelog_view
)

urlpatterns = [
    path("introduction", view=introduction_view, name="introduction"),
    path("installation", view=installation_view, name="installation"),
    path("customization", view=customization_view, name="customization"),
    path("changelog", view=changelog_view, name="changelog")
]