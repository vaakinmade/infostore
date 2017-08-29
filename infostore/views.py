from django.views.generic import TemplateView
from infoapp import models

class HomeView(TemplateView):
	template_name = 'home.html'
	