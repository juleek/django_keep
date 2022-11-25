from django.shortcuts import render

# class Note(models.Model):
#     description = models.CharField(max_length=1000)
#     pub_date = models.DateTimeField('date published')
#     subject = models.CharField(max_length=200)
#     created_by = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)

# Create your views here.

from django.http import HttpResponse
import django.shortcuts as helpers
from .forms import NoteForm
from . import models as mdl
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from accounts import base_template_params as base_templ

class NotesListView(LoginRequiredMixin, ListView):
    model = mdl.Note
    context_object_name = 'notes'
    template_name = 'home.html'
    # paginate_by = 4

    def get_queryset(self):
        user = helpers.get_object_or_404(mdl.User, pk=self.request.user.pk)
        return user.note_set.all()



@login_required
def new_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note: mdl.Note = form.save(commit=False)
            note.created_by = request.user
            note.pub_date = timezone.now()
            note.save()
            return helpers.redirect('home')
    else:
        form = NoteForm()
    return helpers.render(request, 'new_note.html', {'form': form} | base_templ.get_all_params(request))


class NoteDeleteView(DeleteView):
    model = mdl.Note
    pk_url_kwarg = "note_pk"
    template_name = "note_confirm_delete.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context | base_templ.get_all_params(self.request)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = mdl.Note
    fields = ['subject', 'description']
    template_name = 'edit_note.html'
    pk_url_kwarg = 'note_pk'
    context_object_name = 'note'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        note = form.save(commit=False)
        note.updated_by = self.request.user
        note.save()
        return helpers.redirect('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context | base_templ.get_all_params(self.request)

