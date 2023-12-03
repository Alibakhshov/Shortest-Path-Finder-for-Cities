from django.views.generic.base import TemplateView

class AppsView(TemplateView):
    pass


# Calendar
calendar_view = AppsView.as_view(template_name="apps/calendar.html")

#Tickets
tickets_view = AppsView.as_view(template_name="apps/tickets.html")

#File
file_manager_view = AppsView.as_view(template_name="apps/file-manager.html")

#Kanabn
kanban_view = AppsView.as_view(template_name="apps/kanban.html")

#Project
list_view = AppsView.as_view(template_name="apps/project/list.html")
detail_view = AppsView.as_view(template_name="apps/project/detail.html")
create_view = AppsView.as_view(template_name="apps/project/create.html")