from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import CV, Specialty, Candidate, Vacancy

class DashboardView(TemplateView):

    def get(self, *args, **kwargs):
        return render(
            request = self.request,
            template_name = 'dashboard.html',
            context = {
            'candidates' : Candidate.objects.all(),
            'cvs' : cvs = CV.objects.all(),
            'vacs' : Vacancy.objects.all(),
            }
        )
