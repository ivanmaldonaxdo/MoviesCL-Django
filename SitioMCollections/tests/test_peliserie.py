import pytest 
from PeliSeries.models import Peliserie
#DEFINICION DE FUNCIONES


# def test_peliserie_create():
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

@pytest.mark.django_db
def test_peliserie_create_without_autor():
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
#referencias 
#https://www.youtube.com/watch?v=P_hXyudB8zc