from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('import_biodata', import_biodata, name="import_biodata"),
    path('import_grades', import_grades, name="import_grades"),

]
