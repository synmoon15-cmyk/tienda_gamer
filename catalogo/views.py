from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView,
)

from .forms import VideojuegoForm
from .models import Videojuego


class VideojuegoListView(ListView):
    model = Videojuego
    template_name = 'catalogo/lista.html'
    context_object_name = 'videojuegos'

    def get_queryset(self):
        # select_related evita el problema N+1: trae la plataforma en un solo JOIN
        return Videojuego.objects.select_related('plataforma')


class VideojuegoDetailView(DetailView):
    model = Videojuego
    template_name = 'catalogo/detalle.html'
    # Si el pk no existe, DetailView responde 404 automaticamente


# MRO: LoginRequiredMixin SIEMPRE primero (a la izquierda)
class VideojuegoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Videojuego
    form_class = VideojuegoForm
    template_name = 'catalogo/form.html'
    success_url = reverse_lazy('lista')
    success_message = 'Videojuego creado correctamente.'


class VideojuegoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Videojuego
    form_class = VideojuegoForm
    template_name = 'catalogo/form.html'
    success_url = reverse_lazy('lista')
    success_message = 'Videojuego actualizado correctamente.'


class VideojuegoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Videojuego
    template_name = 'catalogo/confirmar_eliminar.html'
    success_url = reverse_lazy('lista')
    success_message = 'Videojuego eliminado correctamente.'
