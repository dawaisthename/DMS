from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('upload/<str:pk>/', views.upload, name="upload"),
    path('search',views.search,name='search'),
    path('update/<int:pk>/update/',views.DocUpdateView.as_view(),name='update'),
    path('delete/<str:pk>/', views.delete_doc, name="delete"),
    # path('read/', views.read_doc, name="read")
]