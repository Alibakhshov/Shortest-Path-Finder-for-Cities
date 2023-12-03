from django.urls import path
from apps.views import calendar_view , tickets_view , file_manager_view , kanban_view , list_view , detail_view , create_view

urlpatterns = [

    #calendar
    path("calendar", view=calendar_view, name="calendar"),
    path("tickets", view=tickets_view, name="tickets"),
    path("file-manager", view=file_manager_view, name="file-manager"),
    path("kanban", view=kanban_view, name="kanban"),

    #Project
    path("list", view=list_view, name="list"),
    path("detail", view=detail_view, name="detail"),
    path("create", view=create_view, name="create"),


]