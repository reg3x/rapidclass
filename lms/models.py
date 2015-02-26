from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse


class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    notes = models.CharField(max_length=30, null=True, blank=True)
    date_added = models.DateField()

    def __str__(self):
        return self.first_name+" "+self.second_name


class Subject(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=30)
    notes = models.CharField(max_length=30, null=True, blank=True)
    date_added = models.DateField()

    def __str__(self):
        return self.name


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    notes = models.CharField(max_length=30, null=True, blank=True)
    date_added = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.student_id)


class Class(models.Model):
    class_id = models.IntegerField(primary_key=True)
    subject_id = models.ForeignKey(Subject)
    teacher_id = models.ForeignKey(Teacher)
    inscribed_students = models.ManyToManyField(Student, through='InscriptionDetail')
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=30, unique=True)
    class_room = models.CharField(max_length=30)
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    notes = models.CharField(max_length=30, null=True, blank=True)
    date_added = models.DateField()
    slug = models.SlugField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "Classes"

    def __str__(self):
        return str(self.code)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unicode(self.name))
        super(Class, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('home_view', args=[str(self.slug)])


class Evaluation(models.Model):
    evaluation_id = models.IntegerField(primary_key=True)
    number_eval = models.IntegerField(max_length=2)
    class_id = models.ForeignKey(Class)

    def __str__(self):
        return str(self.evaluation_id)

class File(models.Model):
    file_id = models.IntegerField(primary_key=True)
    evaluation_id = models.ForeignKey(Evaluation)
    doc_file = models.FileField(upload_to='documents/')

    def __str__(self):
        return str(self.doc_file.name)

class InscriptionDetail(models.Model):
    inscription_detail_id = models.IntegerField(primary_key=True)
    student_id = models.ForeignKey(Student)
    class_id = models.ForeignKey(Class)
    notes = models.CharField(max_length=30, null=True, blank=True)
    date_added = models.DateField()

    def __str__(self):
        return str(self.inscription_detail_id)


