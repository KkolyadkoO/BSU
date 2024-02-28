from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Subject, Teacher
from django.http import Http404
from django.contrib.auth.decorators import login_required


@login_required
def schedule(request, login):
    try:
        current_student = Student.objects.get(login=login)
    except Student.DoesNotExist:
        raise Http404("Студент не найден")

    last_name = request.GET.get('last_name')
    first_name = request.GET.get('first_name')
    group_num = request.GET.get('group_num')

    subjects = Subject.objects.filter(group_num=current_student.group_num)

    first = []
    second = []
    third = []
    fourth = []
    fifth = []
    sixth = []
    seventh = []
    eighth = []
    first = postsort(subjects, 1)
    second = postsort(subjects, 2)
    third = postsort(subjects, 3)
    fourth = postsort(subjects, 4)
    fifth = postsort(subjects, 5)
    sixth = postsort(subjects, 6)
    seventh = postsort(subjects, 7)
    eighth = postsort(subjects, 8)

    return render(request, 'schedule.html',
                  {'current_student': current_student, 'last_name': last_name, 'first_name': first_name,
                   'group_num': group_num,
                   'first': first, 'second': second, 'third': third,
                   'fourth': fourth, 'fifth': fifth, 'sixth': sixth, 'seventh': seventh, 'eighth': eighth})


def check_student(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        try:
            student = Student.objects.get(login=login, password=password)
            request.session['student'] = {
                'login': student.login,
                'first_name': student.first_name,
                'last_name': student.last_name,
                'group_num': student.group_num,
                # Другие поля студента, если есть
            }
            return redirect('schedule', login=login)  # Передача аргумента login
        except Student.DoesNotExist:
            try:
                current_teachers = Teacher.objects.get(login=login, password=password)
                return redirect('view_teacher', last_name=current_teachers.last_name)
            except Teacher.DoesNotExist:
                error = 'Неверный логин или пароль.'
                return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')


def teachers_search(request):
    if request.method == 'POST':
        last_name = request.POST.get('last_name')

        try:
            teacher = Teacher.objects.get(last_name=last_name)
            if last_name == teacher.last_name:
                return redirect('view_teachers', last_name=teacher.last_name)
            else:
                return render(request, 'search_teachers.html', {'error': 'Преподаватель не найден'})
        except Teacher.DoesNotExist:
            return render(request, 'search_teachers.html', {'error': 'Преподаватель не найден'})
    return render(request, 'search_teachers.html')


def view_teachers(request, last_name):
    try:
        current_teachers = Teacher.objects.get(last_name=last_name)
    except Teacher.DoesNotExist:
        raise Http404("Преподаватель не найден")

    # Assuming you have a way to determine the current student
    # Replace the following line with your logic to get the current student
    current_student = Student.objects.get(login=request.session['student']['login'])

    last_namee = current_teachers.last_name
    first_namee = current_teachers.first_name

    # Retrieve subjects for the current teacher
    subjects = Subject.objects.filter(teacher=current_teachers)

    # Sort subjects based on pairs
    first = postsort(subjects, 1)
    second = postsort(subjects, 2)
    third = postsort(subjects, 3)
    fourth = postsort(subjects, 4)
    fifth = postsort(subjects, 5)
    sixth = postsort(subjects, 6)
    seventh = postsort(subjects, 7)
    eighth = postsort(subjects, 8)

    return render(request, 'view_teacher.html', {
        'current_student': current_student,
        'current_teachers': current_teachers,
        'last_name': last_namee,
        'first_name': first_namee,
        'first': first,
        'second': second,
        'third': third,
        'fourth': fourth,
        'fifth': fifth,
        'sixth': sixth,
        'seventh': seventh,
        'eighth': eighth,
    })


def view_teacher(request, last_name):
    try:
        current_teachers = Teacher.objects.get(last_name=last_name)
    except Teacher.DoesNotExist:
        raise Http404("Преподаватель не найден")

    # Assuming you have a way to determine the current student
    # Replace the following line with your logic to get the current student

    last_namee = current_teachers.last_name
    first_namee = current_teachers.first_name

    # Retrieve subjects for the current teacher
    subjects = Subject.objects.filter(teacher=current_teachers)

    # Sort subjects based on pairs
    first = postsort(subjects, 1)
    second = postsort(subjects, 2)
    third = postsort(subjects, 3)
    fourth = postsort(subjects, 4)
    fifth = postsort(subjects, 5)
    sixth = postsort(subjects, 6)
    seventh = postsort(subjects, 7)
    eighth = postsort(subjects, 8)

    return render(request, 'Schedule_teacher.html', {
        'current_teachers': current_teachers,
        'last_name': last_namee,
        'first_name': first_namee,
        'first': first,
        'second': second,
        'third': third,
        'fourth': fourth,
        'fifth': fifth,
        'sixth': sixth,
        'seventh': seventh,
        'eighth': eighth,
    })


def sort(day, pair, subjects):
    res = []
    for subject in subjects:
        if subject.day == day and subject.number_of_class == pair:
            res.append(subject)

    if not res:
        res.append(None)
    return res


def postsort(subjects, pair):
    res = []
    res.extend(sort("Понедельник", pair, subjects))
    res.extend(sort("Вторник", pair, subjects))
    res.extend(sort("Среда", pair, subjects))
    res.extend(sort("Четверг", pair, subjects))
    res.extend(sort("Пятница", pair, subjects))
    res.extend(sort("Суббота", pair, subjects))
    return res
