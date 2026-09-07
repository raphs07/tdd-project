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

    def test_can_start_a_list_and_retrieve_it_later(self):

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

        # Ela digita "Estudar testes funcionais"
        inputbox.send_keys('Estudar testes funcionais')

        # Ela aperta Enter
        inputbox.send_keys(Keys.ENTER)

        # Espera a página atualizar
        time.sleep(1)

        # A tarefa deve aparecer na tabela
        table = self.browser.find_element(
            By.ID, 'id_list_table'
        )

        rows = table.find_elements(
            By.TAG_NAME, 'tr'
        )

        self.assertTrue(
            any(
                row.text == '1: Estudar testes funcionais'
                for row in rows
            )
        )


if __name__ == '__main__':
    unittest.main()