from django.contrib import admin
from .models import CV, Vacancy, Specialty, Candidate

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    pass

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    pass

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    pass
