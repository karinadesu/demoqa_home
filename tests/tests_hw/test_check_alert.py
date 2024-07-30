from pages.alerts import Alerts
import time


def test_timer_alert(browser):
    alert_page = Alerts(browser)
    alert_page.visit()

    assert alert_page.timerAlertButton.exist()
    alert_page.timerAlertButton.click()
    time.sleep(5)
    assert alert_page.alert().text == 'This alert appeared after 5 seconds'
    alert_page.alert().accept()
    assert not alert_page.alert()