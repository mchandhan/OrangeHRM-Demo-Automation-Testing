import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner


def setUpModule():
    print("Setting up module")

def tearDownModule():
    print("Tearing down module")

class PageTitleTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Setting up class")
    
    @classmethod
    def tearDownClass(cls):
        print("Tearing down class")
    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        print("Setup complete")
    
    def tearDown(self):
        m = input("Do you want to quit the driver, enter any key to quit: ")
        self.driver.quit()
        print("Teardown complete")

    def test1_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print("Login page title: " + self.driver.title)
        # Wait for username field to be visible then enter Admin
        self.wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
        # Wait for password field then enter password
        self.wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("admin123")
        # Wait for submit button then click
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        print("Login test completed")
   
if __name__ == '__main__':
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(__import__(__name__))
    
    # Run with HtmlTestRunner for HTML reports
    runner = HtmlTestRunner.HTMLTestRunner(output="test_reports", report_name="OrangeHRM_Functional_Tests", verbosity=2)
    runner.run(suite)