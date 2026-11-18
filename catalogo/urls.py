from django.urls import path
from . import views

urlpatterns = [
    path('', views.VideojuegoListView.as_view(), name='lista'),
    path('juego/<int:pk>/', views.VideojuegoDetailView.as_view(), name='detalle'),
    path('nuevo/', views.VideojuegoCreateView.as_view(), name='crear'),
    path('juego/<int:pk>/editar/', views.VideojuegoUpdateView.as_view(), name='editar'),
    path('juego/<int:pk>/eliminar/', views.VideojuegoDeleteView.as_view(), name='eliminar'),
]
