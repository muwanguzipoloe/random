from django.shortcuts import render
import pandas as pd
from .models import *

def home(request):
    context = {}
    return render(request, 'grader/home.html', context)

def import_biodata(request):
    col_names = ['regno', 'surname', 'other_name', 'gender',
                 'campus', 'nationality', 'Program', 'intake', 'accyr_of_entry', 'dob']
        
    if request.method == "POST":
        uploaded_file = request.FILES['excel_file']
        upload = pd.read_excel(uploaded_file, names=col_names, header=0)

        for i, row in upload.iterrows():
            choosen_course = Course.objects.get(name=row.Program)
            dob= row.dob.strftime('%Y-%m-%d')
            if Student.objects.filter(regno=row.regno).exists():
                pass
            else:
                bioImport = Student.objects.create(course=choosen_course,regno=row.regno,
                                        surname=row.surname,other_name=row.other_name, gender=row.gender,
                                        campus=row.campus,nationality=row.nationality, intake=row.intake,
                                        accyr_of_entry=row.accyr_of_entry,dob=dob)
                bioImport.save()
    return render(request, 'grader/biodata_import.html')

def import_grades(request):
    if request.method == "POST":
        uploaded_file = request.FILES['excel_file']
        upload = pd.read_excel(uploaded_file,1, na_filter=False) # read excel file and only sheet indexed 1

        df3 = upload.iloc[9:]
        df3 = df3[1:]
        
        for i, row in upload.iterrows():
            print(row)

    return render(request, 'grader/import_grades.html')