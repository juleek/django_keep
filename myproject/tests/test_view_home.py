from django.test import TestCase
from django.test import Client
from django.urls import resolve, reverse
from django.contrib.auth.models import User
import datetime

from ..models import Note
from ..views import NotesListView


class HomePageTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test1', 'lennon@thebeatles.com', 'secret')
        self.note = Note.objects.create(subject='subje58155489klkk;l;ct1',
                                        description='Demlmlkjik9j9jkjjokoct1',
                                        pub_date=datetime.datetime.now(),
                                        created_by=self.user)

    def test_home_view_shows_notes_to_auth_user(self):
        c = Client()
        login_res: bool = c.login(username='test1', password='secret')
        self.assertEquals(login_res, True)
        response = c.get(reverse('home'))
        self.assertTrue(b"subje58155489klkk;l;ct1" in response.content)


    def test_home_view_is_callen_by_url(self):
        # response = resolve('/')
        # self.assertEqual(response.resolver_match.func.__name__,  NotesListView.as_view().__name__)
        view = resolve('/')
        # print(f'view = {view}')
        self.assertEquals(view.func.view_class, NotesListView)

    def test_home_view_if_user_is_not_auth_cause_404_Error(self):
        c = Client()
        response = c.get(reverse('home'))
        # print(f'response_status_code = {response.status_code}')
        self.assertEquals(response.status_code, 404)





class AuthorisedUserHomePageTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test2', 'lennon@thebeatles.com', 'secret2')
        self.note = Note.objects.create(subject='gjgjgiuiugjgui',
                                        description='iyiyiuyiuiuiuy',
                                        pub_date=datetime.datetime.now(),
                                        created_by=self.user)
        self.client.login(username='test2', password='secret2')


    def test_home_view_shows_notes_belong_to_auth_user(self):
        user = User.objects.create_user('test3', 'lennon@thebeatles.com', 'secret3')
        user.save()
        note = Note.objects.create(subject='ouipoipoip',
                                   description='poippoipoi',
                                   pub_date=datetime.datetime.now(),
                                   created_by=user)
        note.save()
        c = Client()
        c.login(username='test3', password='secret3')
        # print(f'Note.objects.all = {Note.objects.all()}')
        # print(f'User.objects.all = {User.objects.all()}')
        response = c.get(reverse('home'))
        # print(f'response = {response.content}')
        self.assertFalse(b'self.note.subject' in response.content)


        # login_res: bool = c.login(username='test_second', password='secret_second')
        # self.assertEquals(login_res, True)
        # response = c.get(reverse('home'))
        # self.assertFalse(self.note.subject in response.content)
