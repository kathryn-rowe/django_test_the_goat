from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):

		table = self.browser.find_element_by_id('id_med_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):

		#opens homepage
		self.browser.get(self.live_server_url)

		#Homepage allows user to search for drug type
		self.assertIn('Medication', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Medication', header_text)

		#Search for a drug concept
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter medication name'
		)

		#ex Search for alavert
		inputbox.send_keys('Alavert')

		#Hit enter to search for similar meds, the page updates, and now the page lists
		#'1. Alavert' as a similar medication
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		self.check_for_row_in_list_table('1: Alavert')

		#There is still a text box to search another medication.
		#Enter 'Advil' and search
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Advil')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		#Page updates again, showing complete list
		self.check_for_row_in_list_table('1: Alavert')
		self.check_for_row_in_list_table('2: Advil')

		#Drug concepts will appear on the page
		#Homepage gives explanation about what it does
		#Select a particular drug concept to serve as the reference drug ex Select Alavert 10 MG Oral Tablet .

		#Return a list of all generic and branded drugs that contain the same active ingredients as a reference drug

		#List groups in generic and branded

		#Would be great for app to describe what this group of meds does


		self.fail('Finish the test!')

# if __name__ == '__main__':
# 	unittest.main(warnings='ignore')