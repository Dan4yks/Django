"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpRequest
from app.models import News,Review,Weather
from app.forms import UserForm,ReviewForm,WeatherForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound,HttpResponseRedirect
import requests



def home(request):
    assert isinstance(request, HttpRequest)#assert - проверка истинности утверждений 
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
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
            'message':'Если вам понравился сайт, вы можете оставить свой отзыв о проделанной мною работе',
            'year':datetime.now().year,
        }
    )


@login_required(login_url='/login') 
def applications(request):
    key = 'fdd843b3da461e71c8c9445379bb286f' 
    cities = Weather.objects.all()
    cities_for_user = []
    # Проверяю есть ли у пользователя список городов (чтоб каждому пользователю выводить только те города которыми он интересовался)   
    for city in cities:
        if city.user_name == request.user.username :
            cities_for_user.append(city)
    all_cities = []
    for city in cities_for_user:
        url = 'https://api.openweathermap.org/data/2.5/weather?q='+city.name+'&units=metric&appid='+key
        resp = requests.get(url).json()
        city_info={
            'city': city.name,
            'temp': round(resp['main']['temp']),
            'icon': resp['weather'][0]['icon'],
            'wind': resp['wind']['speed'],
            'humidity': resp['main']['humidity'],
        }
        all_cities.append(city_info)
    weather_form=WeatherForm()
    if request.method == "POST":
        weather_form=WeatherForm(request.POST)
        print(weather_form)
        if weather_form.is_valid():
            new_weather = weather_form.save(commit=False)
            new_weather.user_name = request.user.username
            new_weather.save()
            return redirect(applications)

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/applications.html',
        {
            'title':'Приложения',
            'message':'Страница для описания сайта.',
            'year':datetime.now().year,
            'city_info':all_cities,
            'weather_form': weather_form,
            'cities_for_user':cities_for_user,
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
            'title':'Отчеты',
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
            'title':'Создайте нового пользователя!',
            'user_form': user_form,
            'year':datetime.now().year,
        }
    )


@login_required(login_url='/login')     
def delete(request,id):
    weather = Weather.objects.get(id=id)
    weather.delete()
    return redirect(applications)
