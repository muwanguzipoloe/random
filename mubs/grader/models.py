from django.db import models

class AcademicYear(models.Model):
    name = models.CharField(max_length=4500, null=False)
    last_updated = models.DateTimeField(blank=True, null=True, auto_now=True)
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=4500, null=False)
    years = models.PositiveIntegerField(null=False)
    last_updated = models.DateTimeField(blank=True, null=True, auto_now=True)
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    regno = models.CharField(max_length=255, null=False)
    surname = models.CharField(max_length=255, null=False)
    other_name = models.CharField(max_length=255, null=False)
    gender = models.CharField(max_length=6, choices=GENDER, null=False)
    campus = models.CharField(max_length=45, null=False)
    nationality = models.CharField(max_length=45, null=False)
    intake = models.CharField(max_length=45, null=False)
    accyr_of_entry = models.CharField(max_length=45, null=False)
    dob = models.DateField(null=False)
    last_updated = models.DateTimeField(blank=True, null=True, auto_now=True)
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.surname +' '+self.other_name

class StudentYear(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=4500, null=False)
    last_updated = models.DateTimeField(blank=True, null=True, auto_now=True)
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.name

class Semester(models.Model):
    year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    name = models.CharField(max_length=4500, null=False)
    last_updated = models.DateTimeField(blank=True, null=True, auto_now=True)
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True)


    def __str__(self):
        return self.name

class CourseUnit(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    name = models.CharField(max_length=4500, null=False)
    code = models.CharField(max_length=4500, null=False)
    credit_unit = models.CharField(max_length=4500, null=False)
    last_updated = models.DateTimeField(blank=True, null=True, auto_now=True)
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.name

class CourseGrade(models.Model):
    name = models.CharField(max_length=4500, null=False)
    last_updated = models.DateTimeField(blank=True, null=True, auto_now=True)
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.name