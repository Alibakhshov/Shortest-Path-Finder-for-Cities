from django.views.generic.base import TemplateView

class CustomView(TemplateView):
    pass

#Auth-pages
login_view = CustomView.as_view(template_name="custom/auth-pages/login.html")
register_view = CustomView.as_view(template_name="custom/auth-pages/register.html")
recoverpw_view = CustomView.as_view(template_name="custom/auth-pages/recoverpw.html")
lock_screen_view = CustomView.as_view(template_name="custom/auth-pages/lock-screen.html")
starter_view = CustomView.as_view(template_name="custom/extra-pages/starter.html")
timeline_view = CustomView.as_view(template_name="custom/extra-pages/timeline.html")
invoice_view = CustomView.as_view(template_name="custom/extra-pages/invoice.html")
gallery_view = CustomView.as_view(template_name="custom/extra-pages/gallery.html")
faqs_view = CustomView.as_view(template_name="custom/extra-pages/faqs.html")
pricing_view = CustomView.as_view(template_name="custom/extra-pages/pricing.html")
maintenance_view = CustomView.as_view(template_name="custom/extra-pages/maintenance.html")
coming_soon_view = CustomView.as_view(template_name="custom/extra-pages/coming-soon.html")
error_404_view = CustomView.as_view(template_name="custom/extra-pages/error-404.html")
error_404_alt_view = CustomView.as_view(template_name="custom/extra-pages/error-404-alt.html")
error_500_view = CustomView.as_view(template_name="custom/extra-pages/error-500.html")