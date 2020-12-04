from django.shortcuts import render

from VacsApp.models import Specialty, Company


def main_view(request):
    context = {"vacancies_title_id": {}, "companies_name_id": {}}

    for element in range(Specialty.objects.count()):
        context["vacancies_title_id"][Specialty.objects.all()[element].title] = Specialty.objects.all()[element].id

    for element in range(Company.objects.count()):
        context["companies_name_id"][Company.objects.all()[element].name.upper()] = Company.objects.all()[element].id

    return render(request, 'index.html', context=context)


def vacancies_list_view(request):
    return render(request, 'vacancies.html')


def exact_vac_view(request, id):
    return render(request, 'vacancy.html')


def spec_view(request, spec):
    return render(request, 'vacancies.html')


def comp_view(request, id):
    return render(request, 'company.html')


def not_found_handler(request, exception):
    return render(request, '404.html')


def internal_server_error_handler(request):
    return render(request, '500.html')


