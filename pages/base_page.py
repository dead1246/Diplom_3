from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = self.wait.until(ec.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator)).is_displayed()

    def is_absent(self, locator):
        return not self.driver.find_elements(*locator)

    def wait_url_contains(self, url_part):
        self.wait.until(ec.url_contains(url_part))

    def wait_text_present(self, locator, text):
        self.wait.until(ec.text_to_be_present_in_element(locator, text))

    def wait_invisible(self, locator):
        self.wait.until(ec.invisibility_of_element_located(locator))

    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(ec.visibility_of_element_located(source_locator))
        target = self.wait.until(ec.visibility_of_element_located(target_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", source)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)
        if self.driver.capabilities.get("browserName") == "firefox":
            self.driver.execute_script(
                """
                const source = arguments[0];
                const target = arguments[1];
                const dataTransfer = new DataTransfer();
                ['dragstart', 'dragenter', 'dragover', 'drop', 'dragend'].forEach((type) => {
                    const event = new DragEvent(type, {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer,
                    });
                    (type === 'dragstart' || type === 'dragend' ? source : target).dispatchEvent(event);
                });
                """,
                source,
                target,
            )
            return

        ActionChains(self.driver).drag_and_drop(source, target).perform()
