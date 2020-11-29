from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField(max_length=200)
    employee_count = models.IntegerField()

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Specialty(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    picture = models.URLField(default='https://place-hold.it/100x60')

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'


class Vacancy(models.Model):
    title = models.CharField(max_length=30)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies', default=None, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies', default=None, null=True)
    skills = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансия'