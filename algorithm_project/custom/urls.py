from django.urls import path
from custom.views import (
    login_view, register_view, recoverpw_view, lock_screen_view, starter_view, timeline_view, invoice_view, gallery_view, faqs_view, pricing_view, maintenance_view,
     coming_soon_view, error_404_view, error_404_alt_view, error_500_view )

urlpatterns = [

    #Auth-pages
    path("login", view=login_view, name="login"),
    path("register", view=register_view, name="register"),
    path("recoverpw", view=recoverpw_view, name="recoverpw"),
    path("lock-screen", view=lock_screen_view, name="lock-screen"),

    #Extra-pages
    path("starter", view=starter_view, name="starter"),
    path("timeline", view=timeline_view, name="timeline"),
    path("invoice", view=invoice_view, name="invoice"),
    path("gallery", view=gallery_view, name="gallery"),
    path("faqs", view=faqs_view, name="faqs"),
    path("pricing", view=pricing_view, name="pricing"),
    path("maintenance", view=maintenance_view, name="maintenance"),
    path("coming-soon", view=coming_soon_view, name="coming-soon"),
    path("404", view=error_404_view, name="404"),
    path("404-alt", view=error_404_alt_view, name="404-alt"),
    path("500", view=error_500_view, name="500"),


]