import allure
from selene import have, by


@allure.title("Successful fill form")
def test_successful(setup_browser):
    browser = setup_browser
    first_name = "Evgeniy"
    last_name = "Lukyanov"

    with allure.step("Open registrations form"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Fill form"):
        browser.element("#firstName").set_value(first_name)
        browser.element("#lastName").set_value(last_name)
        browser.element("#userEmail").type('evgeniy@gmail.qa')
        browser.element("#genterWrapper").element(by.text("Other")).click()
        browser.element("#userNumber").set_value("1231231230")
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").click().element('[value="1990"]').click()
        browser.element(".react-datepicker__month-select").click().element('[value="4"]').click()
        browser.element(".react-datepicker__day react-datepicker__day--004").click()
        browser.element("#subjectsInput").send_keys("Maths")
        browser.element("#subjectsInput").press_enter()
        browser.element("#hobbiesWrapper").element(by.text("Sports")).click()
        # browser.element("#uploadPicture").uploadFromClasspath("img/1.png")
        browser.element("#currentAddress").set_value("Russia\nSaint-P\nMoskovskaya\n20")
        browser.element("#state").click()
        browser.element("#stateCity-wrapper").element(by.text("NCR")).click()
        browser.element("#city").click()
        browser.element("#stateCity-wrapper").element(by.text("Delhi")).click()
        browser.element("#submit").click()

    with allure.step("Check form results"):
        browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))