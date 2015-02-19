from django.db import models


class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    notes = models.CharField(max_length=30)
    date_added = models.DateField()

    def __str__(self):
        return self.first_name+" "+self.second_name


class Subject(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    notes = models.CharField(max_length=30)
    date_added = models.DateField()

    def __str__(self):
        return self.name


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    notes = models.CharField(max_length=30)
    date_added = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.student_id)


class Class(models.Model):
    class_id = models.IntegerField(primary_key=True)
    subject_id = models.ForeignKey(Subject)
    teacher_id = models.ForeignKey(Teacher)
    inscribed_students = models.ManyToManyField(Student, through='InscriptionDetail')
    code = models.IntegerField()
    title = models.CharField(max_length=30)
    class_room = models.CharField(max_length=30)
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    notes = models.CharField(max_length=30)
    date_added = models.DateField()

    class Meta:
        verbose_name_plural = "Classes"

    def __str__(self):
        return str(self.code)


class InscriptionDetail(models.Model):
    inscription_detail_id = models.IntegerField(primary_key=True)
    student_id = models.ForeignKey(Student)
    class_id = models.ForeignKey(Class)
    notes = models.CharField(max_length=30)
    date_added = models.DateField()

    def __str__(self):
        return str(self.inscription_detail_id)


