from django.shortcuts import render
from django.views.generic.base import TemplateView

class ElementsView(TemplateView):
     pass

#Components
accordions_view = ElementsView.as_view(template_name="elements/components/accordions.html")
alerts_view = ElementsView.as_view(template_name="elements/components/alerts.html")
avatars_view = ElementsView.as_view(template_name="elements/components/avatars.html")
buttons_view = ElementsView.as_view(template_name="elements/components/buttons.html")
badges_view = ElementsView.as_view(template_name="elements/components/badges.html")
breadcrumbs_view = ElementsView.as_view(template_name="elements/components/breadcrumbs.html")
cards_view = ElementsView.as_view(template_name="elements/components/cards.html")
collapse_view = ElementsView.as_view(template_name="elements/components/collapse.html")
dismissible_view = ElementsView.as_view(template_name="elements/components/dismissible.html")
dropdowns_view = ElementsView.as_view(template_name="elements/components/dropdowns.html")
progress_view = ElementsView.as_view(template_name="elements/components/progress.html")
skeleton_view = ElementsView.as_view(template_name="elements/components/skeleton.html")
spinners_view = ElementsView.as_view(template_name="elements/components/spinners.html")
list_group_view = ElementsView.as_view(template_name="elements/components/list-group.html")
ratio_view = ElementsView.as_view(template_name="elements/components/ratio.html")
tabs_view = ElementsView.as_view(template_name="elements/components/tabs.html")
modals_view = ElementsView.as_view(template_name="elements/components/modals.html")
offcanvas_view = ElementsView.as_view(template_name="elements/components/offcanvas.html")
popovers_view = ElementsView.as_view(template_name="elements/components/popovers.html")
tooltips_view = ElementsView.as_view(template_name="elements/components/tooltips.html")
typography_view = ElementsView.as_view(template_name="elements/components/typography.html")

#Extended
swiper_view = ElementsView.as_view(template_name="elements/extended/swiper.html")
nestable_view = ElementsView.as_view(template_name="elements/extended/nestable.html")
ratings_view = ElementsView.as_view(template_name="elements/extended/ratings.html")
animation_view = ElementsView.as_view(template_name="elements/extended/animation.html")
player_view = ElementsView.as_view(template_name="elements/extended/player.html")
scrollbar_view = ElementsView.as_view(template_name="elements/extended/scrollbar.html")
sweet_alert_view= ElementsView.as_view(template_name="elements/extended/sweet-alert.html")
tour_view =ElementsView.as_view(template_name="elements/extended/tour.html")
tippy_tooltips_view = ElementsView.as_view(template_name="elements/extended/tippy-tooltips.html")
lightbox_view = ElementsView.as_view(template_name="elements/extended/lightbox.html")


#Forms
elements_view = ElementsView.as_view(template_name="elements/forms/elements.html")
select_view = ElementsView.as_view(template_name="elements/forms/select.html")
range_view= ElementsView.as_view(template_name="elements/forms/range.html")
pickers_view = ElementsView.as_view(template_name="elements/forms/pickers.html")
masks_view = ElementsView.as_view(template_name="elements/forms/masks.html")
editor_view = ElementsView.as_view(template_name="elements/forms/editor.html")
file_uploads_view = ElementsView.as_view(template_name="elements/forms/file-uploads.html")
validation_view = ElementsView.as_view(template_name="elements/forms/validation.html")
layout_view = ElementsView.as_view(template_name="elements/forms/layout.html")

#Tables
basic_view = ElementsView.as_view(template_name="elements/tables/basic.html")
datatables_view = ElementsView.as_view(template_name="elements/tables/datatables.html")

#Icons
mingcute_view = ElementsView.as_view(template_name="elements/icons/mingcute.html")
feather_view = ElementsView.as_view(template_name="elements/icons/feather.html")
material_symbols_view = ElementsView.as_view(template_name="elements/icons/material-symbols.html")

#Charts
charts_view = ElementsView.as_view(template_name="elements/charts/charts.html")

#Maps
vector_view = ElementsView.as_view(template_name="elements/maps/vector.html")
google_view = ElementsView.as_view(template_name="elements/maps/google.html")