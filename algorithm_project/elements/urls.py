from django.urls import path
from elements.views import (
    accordions_view,
    alerts_view,
    avatars_view,
    buttons_view,
    badges_view,
    breadcrumbs_view,
    cards_view,
    collapse_view,
    dismissible_view,
    dropdowns_view,
    progress_view,
    skeleton_view,
    spinners_view,
    list_group_view,
    ratio_view,
    tabs_view,
    modals_view,
    offcanvas_view,
    popovers_view,
    tooltips_view,
    typography_view,
    swiper_view,
    nestable_view,
    ratings_view,
    animation_view,
    player_view,
    scrollbar_view,
    sweet_alert_view,
    tour_view,
    tippy_tooltips_view,
    lightbox_view,
    elements_view,
    select_view,
    range_view,
    pickers_view,
    masks_view,
    editor_view,
    file_uploads_view,
    validation_view,
    layout_view,
    basic_view,
    datatables_view,
    mingcute_view,
    feather_view,
    material_symbols_view,
    charts_view,
    vector_view,
    google_view
    
    

)

urlpatterns = [

    #Components
    path("accordions", view=accordions_view, name="accordions"),
    path("alerts", view=alerts_view, name="alerts"),
    path("avatars", view=avatars_view, name="avatars"),
    path("buttons", view=buttons_view, name="buttons"),
    path("badges", view=badges_view, name="badges"),
    path("breadcrumbs", view=breadcrumbs_view, name="breadcrumbs"),
    path("cards", view=cards_view, name="cards"),
    path("collapse", view=collapse_view, name="collapse"),
    path("dismissible", view=dismissible_view, name="dismissible"),
    path("dropdowns", view=dropdowns_view, name="dropdowns"),
    path("progress", view=progress_view, name="progress"),
    path("skeleton", view=skeleton_view, name="skeleton"),
    path("spinners", view=spinners_view, name="spinners"),
    path("list-group", view=list_group_view, name="list-group"),
    path("ratio", view=ratio_view, name="ratio"),
    path("tabs", view=tabs_view, name="tabs"),
    path("modals", view=modals_view, name="modals"),
    path("offcanvas", view=offcanvas_view, name="offcanvas"),
    path("popovers", view=popovers_view, name="popovers"),
    path("tooltips", view=tooltips_view, name="tooltips"),
    path("typography", view=typography_view, name="typography"),

    #Extended
    path("swiper", view=swiper_view, name="swiper"),
    path("nestable", view=nestable_view, name="nestable"),
    path("ratings", view=ratings_view, name="ratings"),
    path("animation", view=animation_view, name="animation"),
    path("player", view=player_view, name="player"),
    path("scrollbar", view=scrollbar_view, name="scrollbar"),
    path("sweet-alert", view=sweet_alert_view, name="sweet-alert"),
    path("tour", view=tour_view, name="tour"),
    path("tippy-tooltips", view=tippy_tooltips_view, name="tippy-tooltips"),
    path("lightbox", view=lightbox_view, name="lightbox"),

    #Forms
    path("elements", view=elements_view, name="elements"),
    path("select", view=select_view, name="select"),
    path("range", view=range_view, name="range"),
    path("pickers", view=pickers_view, name="pickers"),
    path("masks", view=masks_view, name="masks"),
    path("editor", view=editor_view, name="editor"),
    path("file-uploads", view=file_uploads_view, name="file-uploads"),
    path("validation", view=validation_view, name="validation"),
    path("layout", view=layout_view, name="layout"),

    #Tables
    path("basic", view=basic_view, name="basic"),
    path("datatables", view=datatables_view, name="datatables"),

    #Icons
    path("mingcute", view=mingcute_view, name="mingcute"),
    path("feather", view=feather_view, name="feather"),
    path("material-symbols", view=material_symbols_view, name="material-symbols"),

    #Charts
    path("charts", view=charts_view, name="charts"),

    #Maps
    path("vector", view=vector_view, name="vector"),
    path("google", view=google_view, name="google")


]