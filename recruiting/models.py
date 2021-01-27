from django.db import models

class Specialty(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    specialty = models.ForeignKey('Specialty', on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} / {self.specialty}'

class Vacancy(models.Model):
    name = models.CharField(max_length = 50)
    specialty = models.ForeignKey('Specialty', on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.specialty})'

class CV(models.Model):
    url = models.CharField(max_length = 50)
    candidate = models.ForeignKey('Candidate', on_delete = models.CASCADE)
    vacancy = models.ForeignKey('Vacancy', on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.candidate} / {self.vacancy} / {self.url}'
