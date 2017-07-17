from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_searches(self):

		#opens homepage
		self.browser.get('http://localhost:8000')

		#Homepage gives explanation about what it does
		self.assertIn('Medication', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Medication', header_text)

		#Search for a drug concept
		inputbox = self.browser.find_element_by_id('med_search')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter medication name'
		)

		#ex Search for alavert
		inputbox.send_keys('alavert')

		#Hit enter to search for similar meds
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_med_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows)
		)
		#Drug concepts will appear on the page

		#Select a particular drug concept to serve as the reference drug ex Select Alavert 10 MG Oral Tablet .

		#Return a list of all generic and branded drugs that contain the same active ingredients as a reference drug

		#List groups in generic and branded

		#Would be great for app to describe what this group of meds does


		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warnings='ignore')