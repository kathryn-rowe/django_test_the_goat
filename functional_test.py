from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_searches(self):

		#opens homepage
		self.browser.get('http://localhost:8000')

		#Begining tests, starting up Django app
		assert 'Django' in browser.title

		#Homepage gives explanation about what it does
		self.assertIn('Medication', self.browser.title)
		self.fail('Finish the test!')

		#Search for a drug concept ex Search for alavert

		#Drug concepts will appear on the page

		#Select a particular drug concept to serve as the reference drug ex Select Alavert 10 MG Oral Tablet .

		#Return a list of all generic and branded drugs that contain the same active ingredients as a reference drug

		#List groups in generic and branded

		#Would be great for app to describe what this group of meds does


if __name__ == '__main__':
	unittest.main(warnings='ignore')