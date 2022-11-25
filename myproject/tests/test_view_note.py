from django.test import TestCase
from django.test import Client
from django.urls import resolve, reverse
from django.contrib.auth.models import User
import datetime

from ..models import Note
from ..views import NotesListView


class NotePageTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test1', 'lennon@thebeatles.com', 'secret')
        self.client.login(username='test1', password='secret')

    def test_view_new_note_contains_valid_data(self):
        data = {'subject': 'Subject12345', 'description': 'Description12345'}
        url = reverse('new_note')
        self.client.post(url, data)
        # print(f'notes = {Note.objects.all()}')
        self.assertTrue(Note.objects.exists())

    def test_view_new_note_not_add_to_db_if_subject_is_empty(self):
        data = {'subject': '', 'description': 'Description12345'}
        url = reverse('new_note')
        self.client.post(url, data)
        # print(f'notes = {Note.objects.all()}')
        self.assertFalse(Note.objects.exists())

    def test_view_note_has_link_to_edit_note(self):
        note = Note.objects.create(subject='ouipoipoip',
                                   description='poippoipoi',
                                   pub_date=datetime.datetime.now(),
                                   created_by=self.user)
        note.save()
        response = self.client.get(reverse('home'))
        self.assertContains(response, f'<a href="/{note.pk}/edit/">'.encode())

    # def test_view_new_note_if_user_is_not_auth_cause_404_Error(self):


    # def test_home_view_contains_link_to_topics_page(self):
    #     board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
    #     self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
