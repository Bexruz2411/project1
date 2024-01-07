from django.shortcuts import render
from .models import *

def main(request):
    titles = Title.objects.all()
    text = Text.objects.all()
    headerText = HeaderText.objects.all()
    headerImg = HeaderImg.objects.all()
    about = About.objects.all()
    services = Services.objects.all()
    portfolio = Portfolio.objects.all()
    price = Price.objects.all()

    context = {
        'titles': titles,
        'text': text,
        'headerText': headerText,
        'headerImg': headerImg,
        'about': about,
        'services': services,
        'portfolio': portfolio,
        'price': price
    }
    return render(request, 'index.html', context)