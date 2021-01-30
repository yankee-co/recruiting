from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

from .models import CV, Specialty, Candidate, Vacancy

class DashboardView(TemplateView):

    def get(self, *args, **kwargs):
        candidates = Candidate.objects.all()
        cvs = CV.objects.all()

        num = 0
        data = []

        for candidate in candidates:
            num += 1
            for cv in cvs:
                if cv.candidate == candidate:
                    dicted = {
                    'num' : num,
                    'name' : f'{candidate.first_name} {candidate.last_name}',
                    'vacancy' : cv.vacancy.name,
                    'specialty' : candidate.specialty.name,
                    'url' : cv.url,
                    }
            data.append(dicted)
        return render(
            request = self.request,
            template_name = 'dashboard.html',
            context = {
            'data' : data,
            }
        )
