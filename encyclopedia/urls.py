from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.ency, name = 'ency'),
    path('search/<str:name>', views.search, name = 'search'),
    path('create/', views.create, name = 'create'), 
    path('<str:name>/edit', views.edit, name = 'edit'), 
    path("", views.new_page, name = "new")
]
