from django.shortcuts import render


def main_view(request):
    return render(request, 'index.html')


def vacancies_list_view(request):
    return render(request, 'vacancies.html')


def exact_vac_view(request, id):
    return render(request, 'vacancy.html')


def spec_view(request, category, spec):
    return render(request, 'vacancy.html')


def comp_view(request, id):
    return render(request, 'company.html')


def not_found_handler(request, exception):
    return render(request, '404.html')


def internal_server_error_handler(request):
    return render(request, '500.html')


