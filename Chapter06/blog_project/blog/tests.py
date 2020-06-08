from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post


class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='test_user',
            password='testuser',
            email='test@gmail.com'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='A nice body content.',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='A Post')
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.body}', 'A nice body content.')
        self.assertEqual(f'{self.post.author}', 'test_user')

    def test_body_content(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('home.html')
        self.assertContains(response, 'A nice body content.')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'post_detail.html')
        self.assertContains(response, 'A nice body content.')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)
