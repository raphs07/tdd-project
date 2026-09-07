from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # restante do teste...

        # Maria decidiu utilizar o novo app TODO.
        # Ela entra em sua página principal:
        self.browser.get('http://localhost:8000')

        # Ela nota que o título da página menciona TODO
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element(
            By.TAG_NAME, 'h1'
        ).text

        self.assertIn('To-Do', header_text)

        # Ela é convidada a entrar com um item TODO imediatamente
        inputbox = self.browser.find_element(
            By.ID, 'id_new_item'
        )

        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Estudar testes de unidade')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')

        self.check_for_row_in_list_table(
            '1: Estudar testes funcionais'
        )

        self.check_for_row_in_list_table(
            '2: Estudar testes de unidade'
        )


if __name__ == '__main__':
    unittest.main()