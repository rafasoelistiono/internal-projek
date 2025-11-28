from django.urls import path
from main.views import show_main, show_halamandua, show_halamanempat, show_halamansatu, show_halamantiga

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('satu', show_halamansatu, name='show_halamansatu'),
    path('dua', show_halamandua, name='show_halamandua'),
    path('tiga', show_halamantiga, name='show_halamantiga'),
    path('empat', show_halamanempat, name='show_halamanempat'),
]
