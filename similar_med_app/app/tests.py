from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from app.views import home_page


class HomePageTest(TestCase):

	def test_home_page_returns_correct_html(self):
		
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

	def test_home_page_returns_POST_html(self):

		response = self.client.post('/', data={'item_text': 'A new list item'})
		self.assertIn('A new list item', response.content.decode())
		self.assertTemplateUsed(response, 'home.html')
		