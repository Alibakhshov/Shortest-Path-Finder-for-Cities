from django.shortcuts import render
from django.views.generic.base import TemplateView


class DocsView(TemplateView):
     pass


#Docs
introduction_view = DocsView.as_view(template_name="documentation/introduction.html")
installation_view = DocsView.as_view(template_name="documentation/installation.html")
customization_view = DocsView.as_view(template_name="documentation/customization.html")
changelog_view = DocsView.as_view(template_name="documentation/changelog.html")