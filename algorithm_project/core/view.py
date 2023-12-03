from django.views.generic.base import TemplateView


class DashboardView(TemplateView):
     pass
index_view = DashboardView.as_view(template_name="index.html")

