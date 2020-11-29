from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    logo = models.URLField(max_length=None, default='https://place-hold.it/100x60')
    description = models.TextField(max_length=200)
    employee_count = models.IntegerField()


class Specialty(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    picture = models.URLField(max_length=None, default='https://place-hold.it/100x60')


class Vacancy(models.Model):
    title = models.CharField(max_length=30)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()