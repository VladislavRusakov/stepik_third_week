import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'vacancies.settings'
django.setup()


from VacsApp.models import *
from VacsApp import data


if __name__ == '__main__':
    #  Сначала очищаем базу от тестировочного мусора
    Vacancy.objects.all().delete()
    Company.objects.all().delete()
    Specialty.objects.all().delete()

    for dicts in data.jobs_data:
        title = dicts["title"]
        specialty = dicts["specialty"]
        company = dicts["company"]
        skills = dicts["skills"]
        description = dicts["description"]
        salary_min = dicts["salary_from"]
        salary_max = dicts["salary_to"]
        published_at = dicts["posted"]

        vacancy_instance = Vacancy.objects.create(
            title=title,
            skills=skills,
            description=description,
            salary_min=salary_min,
            salary_max=salary_max,
            published_at=published_at
    )

    for dicts in data.companies_data:
        name = dicts["title"]
        logo = dicts["logo"]
        employee_count = dicts["employee_count"]
        location = dicts["location"]
        description = dicts["description"]

        company_instance = Company.objects.create(
            name=name,
            location=location,
            logo=logo,
            description=description,
            employee_count=employee_count
        )

    for dicts in data.specialties_data:
        code = dicts["code"]
        title = dicts["title"]

        speciality_instance = Specialty.objects.create(
            code=code,
            title=title
        )

