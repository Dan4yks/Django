"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpRequest
from app.models import News,Review
from app.forms import UserForm,ReviewForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required



def home(request):
    assert isinstance(request, HttpRequest)#assert - проверка истинности утверждений 
    return render(
        request,
        'app/index.html',
        {
            'title':'Первое приложение',
            'year':datetime.now().year,
        }
    )
@login_required(login_url='/login') #Декоратор для проверки зарегистрирован ли пользователь
def review(request):
    review_form=ReviewForm()
    if request.method == "POST":
        review_form=ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.user_name = request.user.username
            new_review.save()
            return redirect(review)
    SaitReviews=Review.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/review.html',
        {
            'title':'Отзыв',
            'review_form': review_form,
            'SaitReviews':SaitReviews,
            'message':'Если вам понравился сайт вы можете связаться с автором и поблагодарить его.',
            'year':datetime.now().year,
        }
    )
@login_required(login_url='/login') 
def applications(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/applications.html',
        {
            'title':'Приложения',
            'message':'Страница для описания сайта.',
            'year':datetime.now().year,
        }
    )

def homepage(request):
    news=News.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/homepage.html',
        {
            'news':news,
            'title':'Домашняя страница',
            'message':'Страница для описания сайта.',
            'year':datetime.now().year,
        }
    )
def detail(request,news_id):
    news = get_object_or_404(News, id=news_id)
    assert isinstance(request, HttpRequest)
    return render(request, 'app/detail.html',
        {
            'title':'Подробнее',
            'news': news,
            'year':datetime.now().year,
        }
    )
def registration(request):
    user_form=UserForm()
    #Создаем нового пользователя, делаем проверку нет ли уже такого пользователя, автоматически входим на сайт при регитсрации, после регистрации перенаправляем на начальную страницу сайта 
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            ))
            return redirect(home)
    assert isinstance(request, HttpRequest) 
    return render(request, 'app/registration.html',
        {
            'title':'Создай нового пользователя!',
            'user_form': user_form,
            'year':datetime.now().year,
        }
    )