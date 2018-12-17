from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContentsPageView(TemplateView):
    template_name = 'contents.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'
