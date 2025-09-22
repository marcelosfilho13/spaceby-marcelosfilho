from django.urls import path
from gallery.views import index, image

#! é possíel identificar uma url por um atributo "name", uma boa prática
#* o "name", é adicionado no atributo "href" da tag html
urlpatterns = [
  path('', index, name='index'),
  path('image/', image, name='imagem'),
]