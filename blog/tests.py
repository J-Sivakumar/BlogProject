from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username= 'testuser',
            email= 'test@gmail.com',
            password= '........'
        )

        self.post = Post.objects.create(
            title = 'New post title',
            body = 'New post body',
            author = self.user

        )
    
    def test_str_representation(self):
        post = Post(title = 'Sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'New post title' )
        self.assertEqual(f'{self.post.author}', 'testuser' )
        self.assertEqual(f'{self.post.body}', 'New post body' )
    
    def test_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'New post body')
    
    def test_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'New post title')
        self.assertTemplateUsed(response, 'blog_details.html')
    
    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_create_view(self):
        response = self.client.post(reverse('new_blog'),
                                    {
                                        'title': "New title",
                                        'body': "New body",
                                        'author':self.user
                                    })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New body')
        
    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'),
                                    {
                                        'title': "Updated title",
                                        'body': "Updated body",
                                    })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.get(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 200)  