from django.views.generic.base import TemplateView

class LayoutView(TemplateView):
    pass

# Layouts
layout_compact_view = LayoutView.as_view(template_name="custom/layouts/layout-compact-view.html")
layout_hidden_view = LayoutView.as_view(template_name="custom/layouts/layout-hidden.html")
layout_hover_view = LayoutView.as_view(template_name="custom/layouts/layout-hover-view.html")
layout_icon_view = LayoutView.as_view(template_name="custom/layouts/layout-icon-view.html")
layout_mobile_view = LayoutView.as_view(template_name="custom/layouts/layout-mobile-view.html")
