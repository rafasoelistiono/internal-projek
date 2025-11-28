from django.shortcuts import render

def show_main(request):
    return render(request, 'main.html')

def show_halamansatu(request):
    return render(request, 'satupage.html')

def show_halamandua(request):
    return render(request, 'duapage.html')

def show_halamantiga(request):
    return render(request, 'tigapage.html')

def show_halamanempat(request):
    return render(request, 'empatpage.html')