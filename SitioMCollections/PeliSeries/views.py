from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from .forms import FormPeliserie,FormCarrousel,FormConsulta
from .models import Categoria,Peliserie,Carousel,Usuario,Consulta
from django.http import request,JsonResponse
from .TheMovieDBAPI import MovieDB

# Create your views here.
def indexInicio(request): 
    return render(request, 'PeliSeries/index.html')


def peliculas(request):
    pelis = Peliserie.objects.filter(categoria=1)
    return render(request, 'PeliSeries/peliculas.html', {'pelis':pelis})

def series(request):
    series = Peliserie.objects.filter(categoria=2)
    return render(request, 'PeliSeries/series.html', {'series':series})

def apiMovies(request):
    return render(request, 'PeliSeries/API_MOVIES.html')


def detailPeliserie(request,pk):
    peliserie=get_object_or_404(Peliserie, pk=pk)
    similar =Peliserie.objects.exclude(pk=pk)
    return render(request, 'PeliSeries/detallePeliserie.html', {'peliserie': peliserie,'similar':similar})


    
#region views_dont_used
def indexConsultas(request):
    if request.method == 'POST':
        form = FormConsulta(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            form = FormConsulta()
            return render(request, 'PeliSeries/indexConsultas.html', {'form': form})
    else:
        form  = FormConsulta()   
        return render(request, 'PeliSeries/indexConsultas.html', {'form': form})
    
def EliminarConsulta(request,pk):
    consulta=Consulta.objects.get(pk=pk)
    consulta.delete()
    consulta=Consulta.objects.all()
    peliserie=Peliserie.objects.all()
    carrous=Carousel.objects.all()
    return render(request, 'PeliSeries/mantenedor.html', {'peliserie':peliserie,"carrousel":carrous,"consulta":consulta}) 

def mantenedor(request):
    peliserie=Peliserie.objects.all()
    carrous=Carousel.objects.all()
    consulta=Consulta.objects.all()
    return render(request, 'PeliSeries/mantenedor.html', {'peliserie':peliserie,"carrousel":carrous,"consulta":consulta})    

# crud peliserie
def CrearPeliserie(request):
    if request.method == "POST":
        form = FormPeliserie(request.POST,files=request.FILES)
        if form.is_valid(): 
            post = form.save(commit=False) 
            post.admin = request.user 
            post.published_date = timezone.now() 
            post.save() 
            return redirect('mantenedor') 
    else: 
        form = FormPeliserie() 
    return render(request, 'PeliSeries/peliserie_edit.html', {'form': form})

def EditarPeliserie(request, pk):
    post = get_object_or_404(Peliserie, pk=pk) 
    if request.method == "POST": 
        form = FormPeliserie(request.POST,instance=post,files=request.FILES) 
        if form.is_valid():     
            post = form.save(commit=False) 
            post.admin = request.user
            post.save() 
            return redirect('mantenedor') 
    else: 
        form = FormPeliserie(instance=post) 
    return render(request, 'PeliSeries/peliserie_edit.html', {'form': form})

def EliminarPeliserie(request,pk):
    peliserie=Peliserie.objects.get(pk=pk)
    peliserie.delete()
    peliserie=Peliserie.objects.all()
    carrous=Carousel.objects.all()
    consulta=Consulta.objects.all()
    return render(request, 'PeliSeries/mantenedor.html', {'peliserie':peliserie,"carrousel":carrous,"consulta":consulta}) 

# crud carousel
def CrearCarousel(request):
    if request.method == "POST":
        form = FormCarrousel(request.POST,files=request.FILES)
        if form.is_valid(): 
            post = form.save(commit=False) 
            post.fecha_public = timezone.now() 
            post.save() 
            return redirect('mantenedor') 
    else: 
        form = FormCarrousel() 
    return render(request, 'PeliSeries/carousel_edit.html', {'form': form})

def EditarCarousel(request, pk):
    post = get_object_or_404(Carousel, pk=pk) 
    if request.method == "POST": 
        form = FormCarrousel(request.POST, instance=post,files=request.FILES) 
        if form.is_valid(): 
            post = form.save(commit=False) 
            post.save() 
            return redirect('mantenedor') 
    else: 
        form = FormCarrousel(instance=post) 
    return render(request, 'PeliSeries/carousel_edit.html', {'form': form})

def EliminarCarousel(request,pk):
    carousel=Carousel.objects.get(pk=pk)
    carousel.delete()
    carousel=Carousel.objects.all()
    peliserie=Peliserie.objects.all()
    consulta=Consulta.objects.all()
    return render(request, 'PeliSeries/mantenedor.html', {"carrousel":carousel,'peliserie':peliserie,'consulta':consulta})     

def register(request): 
    form=UserCreationForm()
    return render(request, 'PeliSeries/register.html', {'form':form})

def login(request): 
    return render(request, 'PeliSeries/login.html', {})
#endregion views_dont_used

movieDB = MovieDB("8f56a9bedde7f726d2cd993b3971efe3", "https://api.themoviedb.org/3")

def get_genres(request):
    genres = movieDB.search_genres()
    return JsonResponse(genres)

def get_movies(request):
    query = request.GET.get('query',None)
    movies = movieDB.search_multi(query)
    return JsonResponse(movies)    

def get_top_movies(request):
    movies = movieDB.search_top_rated()
    return JsonResponse(movies)    