from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r"^/?$", views.NotesListView.as_view(), name='home'),
    re_path(r"new_note/$", views.new_note, name='new_note'),
    re_path(r"(?P<note_pk>\d+)/edit/$", views.NoteUpdateView.as_view(), name='edit_note'),
    re_path(r"(?P<note_pk>\d+)/delete/$", views.NoteDeleteView.as_view(), name='delete'),

]
