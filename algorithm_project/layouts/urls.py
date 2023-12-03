from django.urls import path
from layouts.views import layout_compact_view, layout_hidden_view, layout_hover_view, layout_icon_view, \
    layout_mobile_view

urlpatterns = [

    # Layouts
    path("compact", view=layout_compact_view, name="compact-view"),
    path("hidden", view=layout_hidden_view, name="hidden-view"),
    path("hover", view=layout_hover_view, name="hover-view"),
    path("icon", view=layout_icon_view, name="icon-view"),
    path("mobile", view=layout_mobile_view, name="mobile-view"),
]
