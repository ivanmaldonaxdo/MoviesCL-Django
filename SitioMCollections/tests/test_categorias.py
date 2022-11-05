import pytest 
from PeliSeries.models import Peliserie,Categoria

# @pytest.mark.django_db
# def test_categ_create():
#     Categoria().objects.create(1,"Podcast")
#     count = Categoria().objects.count()
#     assert count == 1

# # @pytest.fixture

# def Categoria_1(db):
#     return 

# #DEFINICION DE FUNCIONES

# # @pytest.mark.xfail
# @pytest.mark.django_db
def test_peliserie_create():
    contenido = Peliserie.objects.create(
        titulo="En busca de la felicidad",
        autor = "Will Smith",
        reparto= "Will Smith ,Jaden Smith",
        descripcion="",
        genero="",
        year_estreno= 1998,
        admin=1,
        categoria=1,

    )
    assert contenido.autor == "Will Smith"

# @pytest.mark.skip
# @pytest.mark.django_db
# def test_peliserie_create_without_autor():
#     contenido = Peliserie.objects.create(
#         titulo="En busca de la felicidad",
#         autor = "Will Smith",
#         reparto= "Will Smith ,Jaden Smith",
#         descripcion="",
#         genero="",
#         year_estreno= 1998,
#         admin=1,
#         categoria=1,

#     )
#     assert contenido.autor == "Will Smith"
#referencias 
#https://www.youtube.com/watch?v=P_hXyudB8zc