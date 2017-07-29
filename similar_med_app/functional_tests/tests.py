from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import unittest

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def wait_for_row_in_list_table(self, row_text):
		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('id_med_table')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time() - start_time > MAX_WAIT:
					raise e
				time.sleep(0.5)

	def test_can_start_a_list_for_one_user(self):

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


		self.wait_for_row_in_list_table('1: Alavert')

		#There is still a text box to search another medication.
		#Enter 'Advil' and search
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Advil')
		inputbox.send_keys(Keys.ENTER)

		#Page updates again, showing complete list
		self.wait_for_row_in_list_table('1: Alavert')
		self.wait_for_row_in_list_table('2: Advil')

	def test_multiple_users_can_start_lists_at_different_urls(self):
		#User starts new search
		self.browser.get(self.live_server_url)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Alavert')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Alavert')

		#This search as a unique url
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/app/.+')

		#New User comes along
		self.browser.quit()
		self.browser = webdriver.Firefox()

		#New user visits the home page. There is not sign of previous user
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Alavert', page_text)
		self.assertNotIn('Advil', page_text)

		#User starts a new list by entering a new item.
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Neproxin')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Neproxin')

		#New user gets new unique URL
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/app/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)

		#No trace of Edith's list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Alavert', page_text)
		self.assertIn('Neproxin', page_text)

		#Drug concepts will appear on the page
		#Homepage gives explanation about what it does
		#Select a particular drug concept to serve as the reference drug ex Select Alavert 10 MG Oral Tablet .

		#Return a list of all generic and branded drugs that contain the same active ingredients as a reference drug

		#List groups in generic and branded

		#Would be great for app to describe what this group of meds does


		self.fail('Finish the test!')

# if __name__ == '__main__':
# 	unittest.main(warnings='ignore')