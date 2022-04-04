from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


class UITests(StaticLiveServerTestCase):
    selenium = None
    fixtures = ['questions.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.headless = True
        cls.selenium = WebDriver(options=options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_poll_links(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/polls/'))
        links = self.selenium.find_elements(by='tag name', value='li')
        self.assertEqual(len(links), 2)
