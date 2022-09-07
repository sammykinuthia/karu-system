from django.db import models

class School(models.Model):
    SCHOOLS = [
        ("SPAS",'School of Pure and Applied Sciences'),
        ('SAB','School of Agriculture and Biotechnology'),
        ('SOB','School of Business'),
        ('SESS','School of Education and Social Sciences'),
        ('SNRE','School of Natural Resources and Environmental Studies'),
        ('SN','School of Business'),

    ]
    name = models.CharField(max_length=4, choices=SCHOOLS, unique=True)
    def __str__(self) -> str:
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=4)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    def __str__(self) -> str:
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    duration = models.IntegerField()
    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, default=None)
    last_name = models.CharField(max_length=200)
    adm_number = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    program = models.ForeignKey(Program, on_delete=models.PROTECT)
    adm_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Lecturer(models.Model):
    SALUTATIONS = [
        ('Mr','Mr'),
        ("Mrs", "Mrs"),
        ("Miss","Miss"),
        ("Dr",'Dr'),
        ('Prof',"Prof"),
    ]
    salutation = models.CharField(max_length=4, choices=SALUTATIONS)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, default=None)
    last_name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    adm_date = models.DateTimeField(auto_now_add=True)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Unit(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    description = models.TextField()
    def __str__(self) -> str:
        return self.code



class RegisteredUnits(models.Model):
    SEMCODE = [
        ('y1s1','y1s1'),
        ('y1s2','y1s2'),
        ('y1s3','y1s3'),
        ('y2s1','y2s1'),
        ('y2s2','y2s2'),
        ('y2s3','y2s3'),
        ('y3s1','y3s1'),
        ('y3s2','y3s2'),
        ('y3s3','y3s3'),
        ('y4s1','y4s1'),
        ('y4s2','y4s2'),
        ('y4s3','y4s3'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    semester_code = models.CharField(max_length=4, choices=SEMCODE)
    def __str__(self) -> str:
        return f"{self.student} {self.semester_code}"
