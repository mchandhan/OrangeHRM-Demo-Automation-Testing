
```
# OrangeHRM Functional Tests

This project contains automated functional tests for the [OrangeHRM demo site](https://opensource-demo.orangehrmlive.com/) using **Python**, **Selenium WebDriver**, and **unittest**.  
Test execution reports are generated with **HtmlTestRunner**.

---

## Project Structure

```
.
├── test_reports/              # Generated HTML reports
├── test_orangehrm.py          # Main test script
└── README.md                  # Project documentation
```

---

## Prerequisites

- Python 3.8+
- Google Chrome browser
- ChromeDriver (automatically managed via `webdriver-manager`)

Install required dependencies:

```bash
pip install selenium webdriver-manager html-testRunner
```

---

## Running the Tests

Execute the test suite with:

```bash
python test_orangehrm.py
```

Reports will be generated inside the `test_reports/` directory with the name **OrangeHRM_Functional_Tests.html**.

---

## Test Flow

1. **Setup**
   - Initializes Chrome WebDriver using `webdriver-manager`.
   - Sets implicit and explicit waits.

2. **Test Case: Login**
   - Navigates to OrangeHRM login page.
   - Enters username (`Admin`) and password (`admin123`).
   - Clicks the login button.
   - Prints page title and confirms login attempt.

3. **Teardown**
   - Prompts user input before quitting the driver.
   - Closes browser session.

---

## 📊 Reports

- After execution, HTML reports are available in `test_reports/`.
- Reports include:
  - Test case results (pass/fail)
  - Execution logs
  - Screenshots (if implemented)

---

## Notes

- `setUpModule` and `tearDownModule` run once per module.
- `setUpClass` and `tearDownClass` run once per test class.
- `setUp` and `tearDown` run before and after each test method.
- You can extend this framework by adding more test cases for different OrangeHRM modules (e.g., PIM, Leave, Recruitment).

---

## Example Output

```
Setting up module
Setting up class
Setup complete
Login page title: OrangeHRM
Login test completed
Do you want to quit the driver, enter any key to quit:
Teardown complete
Tearing down class
Tearing down module
```

---

## Future Enhancements

- Add screenshot capture on test failure.
- Parameterize credentials using environment variables.
- Integrate with CI/CD pipelines (GitHub Actions, Jenkins).
```

Would you like me to also add a **CI/CD pipeline example (GitHub Actions YAML)** so these tests run automatically on every push?
