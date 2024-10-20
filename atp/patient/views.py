from django.shortcuts import render
from django.http import HttpResponse


def patient_list(request):
    return HttpResponse('Список пациентов')


def patient_detail(request, id):
    return HttpResponse(f'Анкета пациента {id}')
