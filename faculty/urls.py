from django.urls import path

from faculty import views

app_name = "faculty"
urlpatterns = [
    path("programs/<int:spec_id>/", views.ind_specialty, name="ind_specialty"),
    path("departments/<int:dep_id>/", views.ind_department, name="ind_department"),
    path("departments/", views.departments, name="departments"),
    path("programs/", views.programs, name="programs"),
    path("", views.main_page, name="main_page"),
]
