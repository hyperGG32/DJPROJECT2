from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

import faculty
from faculty.models import Department, Specialty, FacultyInformation


def main_page(request):
    fac = FacultyInformation.objects.first()
    return render(request, "faculty/main.html", {"faculty": fac})


def programs(request):
    specialties = Specialty.objects.all()
    return render(request, "faculty/specialties.html", {"specialties": specialties})


def departments(request):
    departs = Department.objects.all()
    return render(request, "faculty/departments.html", {"departments": departs})


def ind_department(request, dep_id):
    depart = get_object_or_404(Department, id=dep_id)
    return render(request, "faculty/ind_department.html", {"department" : depart})


def ind_specialty(request, spec_id):
    specialty = get_object_or_404(Specialty, id=spec_id)
    return render(request, "faculty/ind_specialty.html", {"specialty": specialty})
