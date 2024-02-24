from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    group_num = models.IntegerField(default=0)
    student_number = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    course = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name


class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patronymic_name = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.last_name

class Subject(models.Model):
    day = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    number_of_class = models.IntegerField(default=0)
    classroom = models.CharField(max_length=255, null=True, blank=True)
    group_num = models.IntegerField(default=0)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    subgroup = models.IntegerField(default=0)

    def __str__(self):
        return self.subject



# CREATE DATABASE Schedule;
#
#
# CREATE TABLE teacher
# (
#     id SERIAL PRIMARY KEY,
#     first_name VARCHAR(258) NOT NULL,
#     last_name VARCHAR(258) NOT NULL,
#     patronymic_name VARCHAR(258) NOT NULL,
#     login VARCHAR(258) NOT NULL UNIQUE ,
#     password VARCHAR(258) NOT NULL
# );
#
#
# CREATE TABLE subjects
# (
#     id SERIAL PRIMARY KEY,
#     day VARCHAR(25) NOT NULL,
#     subject varchar(50) NOT NULL,
#     number_of_class INT not null,
#     teacher INT REFERENCES teacher(id),
#     classroom INT,
#     group_num INT NOT NULL
# );
#
# INSERT INTO student(first_name, last_name, group_num, student_number, login, password, course)
# values ('Артём', 'Колядко','14','2440002','fsc.KolyadkoAN','123123',2),
#        ('test', 'TEST','14','2440003','fsc.testT','123123',2);
#
# INSERT INTO teacher(first_name, last_name, patronymic_name, login, password)
# VALUES ('Лукьянович','Инна','Робертовна','fsc.LukyanovichIR','123123123'),
#        ('Нифагин','Владимир','Александрович','fsc.NifaginVA','123123123123');
# INSERT INTO teacher(first_name, last_name, patronymic_name, login, password)
# VALUES
#     ('Сергеенко','Ольга','Олеговна','fsc.SergeenkoOO','131231');
#
#
#
# INSERT INTO subjects(day, subject, number_of_class, teacher, classroom, group_num)
# VALUES ('Вторник','Web-дизайн',4,1,405,14),
#        ('Вторник','Английский язык',3,3,713,14),
#        ('Вторник','Методы вычислений',5,2,405,14),
#        ('Вторник','Методы вычислений',6,2,405,14);
#
# INSERT INTO subjects(day, subject, number_of_class, teacher, classroom, group_num)
# VALUES ('Среда','Английский язык',3,1,405,14),
#        ('Среда','Английский язык',4,3,713,14);
# INSERT INTO subjects(day,subject,number_of_class, group_num)
# VALUES ('Среда','Физ',5,14);
#
# INSERT INTO subjects(day, subject, number_of_class, teacher, classroom, group_num)
# VALUES ('Четверг','Метод вычисления',4,2,405,14),
#        ('Четверг','Операционные системы',5,5,211,14),
#        ('Четверг','Метод вычисления',6,2,405,14),
#        ('Четверг','Операционные системы',7,5,211,14),
#        ('Пятница','Компьютерная графика и анимация',4,6,803,14),
#        ('Пятница','Компьютерная графика и анимация',5,6,803,14),
#        ('Пятница','Компьютерная графика и анимация',6,6,803,14),
#        ('Пятница','Операционные системы',7,5,211,14),
#        ('Суббота','Компьютерная графика и анимация',1,6,803,14),
#        ('Суббота','Компьютерная графика и анимация',2,6,803,14),
#        ('Суббота','Web-дизайн',3,7,413,14),
#        ('Понедельник','Теория вероятности',4,4,801,14),
#        ('Понедельник','Теория вероятности',5,4,801,14),
#        ('Понедельник','Физ',3,null,null,14);
#
#
#
# INSERT INTO teacher(first_name, last_name, patronymic_name, login, password)
# VALUES
#     ('Кветко','Оксана','Михайловна','fsc.KvetkoOM','KvetkoOM'),
#     ('Пшеничная','Анна','Владимировна','fsc.PshenichnayaAV','PshenichnayaAV'),
#     ('Кульбицкий','Алексей','Евгеньевич','fsc.KulbickiyAE','KulbickiyAE'),
#     ('Кривулько','Диана','Романова','fsc.KrivulkoDR','KrivulkoDR');
#
#
#
# SELECT s.id s_id,
#        s.first_name f_name,
#        s.last_name l_name,
#        s.group_num g_num,
#        s.student_number s_num,
#        s.login log,
#        s.password pas,
#        s.course cour
# FROM student s;
#
# SELECT *
# FROM subjects
# WHERE group_num = 14;
#
#
#
#
# Drop table subjects;