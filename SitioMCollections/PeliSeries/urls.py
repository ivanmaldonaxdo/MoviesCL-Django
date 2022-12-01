from django.conf.urls import include, url 
from . import views
urlpatterns = [ 
    url(r'^$', views.indexInicio,name='home'),
    url(r'^Register/$', views.register, name="register"),
    url(r'^Login/$', views.login, name="login"),
    url(r'^Peliculas/$', views.peliculas, name="peliculas"),
    url(r'^Series/$', views.series, name="series"), 
    url(r'^apiMovies/$', views.apiMovies, name="apiMovies"), 

    url(r'^detail/(?P<pk>[0-9]+)/$', views.detailPeliserie, name='detailPS'),
    url(r'^Mantenedor/$', views.mantenedor, name="mantenedor"), 
    url(r'^PeliSerie/new/$', views.CrearPeliserie, name='new_peliserie'),
    url(r'^PeliSerie/(?P<pk>[0-9]+)/edit/$', views.EditarPeliserie, name='edit_peliserie'),
    url(r'^PeliSerie/(?P<pk>[0-9]+)/delete/$', views.EliminarPeliserie, name='delete_peliserie'),
    url(r'^Carousel/new/$', views.CrearCarousel, name='new_carousel'),
    url(r'^Carousel/(?P<pk>[0-9]+)/edit/$', views.EditarCarousel, name='edit_carousel'),
    url(r'^Carousel/(?P<pk>[0-9]+)/delete/$', views.EliminarCarousel, name='delete_carousel'),
    url(r'^Consultas/$', views.indexConsultas, name='consultas'),
    url(r'^Consultas/(?P<pk>[0-9]+)/delete/$', views.EliminarConsulta, name='delete_consulta'),
    url(r'^get_genres/$', views.get_genres, name='get_genres'),
    url(r'^get_movies/$', views.get_movies, name='get_movies'),
    url(r'^get_top_movies/$', views.get_top_movies, name='get_top_movies'),



]