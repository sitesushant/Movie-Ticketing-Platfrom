from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout_view', views.logout_view, name='logout'),
    path('register/', views.register, name="register"),
    path('index/', views.index, name='index'),
    path('movie/<str:movieName>', views.moviePage, name="moviePage"),
    path('book_tickets/<str:movieName>', views.bookTicket, name="book_seat"),
    path('search/', views.search, name='search'),
    path('results/<str:query>', views.results, name='results'),
    path('error/', views.error, name="error"),
    path('shows/<str:movie>/<str:city>/<str:day>/<str:hall>', views.shows, name="shows"),
    path('seats/<int:show>', views.seats, name="seats"),
    path('ticket', views.ticket, name="ticket"),
    path('tickets', views.allTickets, name="allTickets"),
    path('movies', views.allMovies, name="allMovies"),
    
    path('search/<str:query>/<str:model_type>/', views.search_results, name='search_results'),
   
    path('ott/<str:ott_name>/', views.ott_page, name='ott_page'),
    path('ott/', views.ott_view, name='ott_view'),
    path('error/', views.error_page, name='error_page'),
]
""" path('OTT/', views.OTTView, name="allOTT"),
    path('ott/<str:OTTName>/', views.OTTPage, name="OTTPage"),
    path('results/<str:query>/', views.results, name="results"), """ 
""" path('movie/<str:movie_name>/', views.movie_page, name='movie_page'), """ 