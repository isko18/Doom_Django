from django.shortcuts import render,redirect
from .models import Socialnetworks
from apps.home.models import Settings
from apps.telegram.views import get_text

# Create your views here.
def contacts(request):
    socialnetworks =  Socialnetworks.objects.latest("id")
    settings =  Settings.objects.latest("id")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        subject = request.POST.get("subject")
        
        review = Socialnetworks.objects.create(name = name, email = email, message = message, subject = subject)

        get_text(f""" Оставлен отзыв 
Имя пользователя: {review.name}
Адрес(email): {review.email}
Тема сообщения: {review.subject}
Текст: {review.message}
""")

        
    context ={
        'settings':settings,
        'socialnetworks':socialnetworks,
    }
    return render(request, 'contact.html',context)