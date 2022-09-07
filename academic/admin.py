from django.contrib import admin
from .models import Department, Program, Student, Lecturer, School, RegisteredUnits, Unit


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'program', 'adm_number',"phone_number", 'adm_date']
    
    def name(self, student):
        if student.middle_name:
            return f"{student.first_name} {student.middle_name} {student.last_name}"
        else:
            return f"{student.first_name} {student.last_name}"

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'code','school']

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'code','department','duration']

@admin.register(RegisteredUnits)
class RegisteredUnitsAdmin(admin.ModelAdmin):
    list_display = ['student', 'unit', 'semester_code']

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'description']

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ['salutation','name', 'phone_number', 'school', 'email']
    def name(self, student):
        if student.middle_name:
            return f"{student.first_name} {student.middle_name} {student.last_name}"
        else:
            return f"{student.first_name} {student.last_name}"