from django.views.generic import ListView, CreateView
from infoapp import models


class InfoListView(ListView):
	context_object_name = "info"
	template_name = 'infoapp/info_list.html'

	def get_context_data(self, **kwargs):
		context = super(InfoListView, self).get_context_data(**kwargs)
		return context

	def get_queryset(self):
		return models.Info.objects.all()


class InfoCreateView(CreateView):
	template_name = 'infoapp/info_form.html'
	fields = ['name', 'email']
	model = models.Info

	def form_valid(self, form):
		return super(InfoCreateView, self).form_valid(form)