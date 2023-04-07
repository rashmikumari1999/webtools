from django.urls import path, include
from . import views
urlpatterns = [
   path('', views.index, name='index'),
    path('analyzed', views.analyzed, name='analyzed' ),
    path('analyze', views.analyze, name='analyze'),
    path('translator', views.translator, name='translator'),
    path('translated', views.translated, name='translated'),
    path('base', views.base, name='base'),
   path('counter', views.counter, name='counter'),
   path('home', views.home, name='home'),
    path('ss', views.some, name='some'),
path('short', views.short, name='short'),
path('create', views.create, name='create'),
    path('<str:pk>', views.go, name='go'),
     path('scrab/', views.scrab, name='scrab'),
     # path('tgt', views.tgt, name='tgt'),
    #path('ss/', views.some, name='some'),


]