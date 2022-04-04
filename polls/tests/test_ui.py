from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class UITests(StaticLiveServerTestCase):
    selenium = None
    fixtures = ['questions.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_poll_link(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/polls/'))
        links = self.selenium.find_elements(by='name', value='li')
        print(links)
