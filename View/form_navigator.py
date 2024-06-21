class FormNavigator:
    def __init__(self):
        self.login_form = None
        self.registration_form = None
        self.main_window = None

    def open_login_form(self):
        from login_form import LoginRegistrationForm
        self.login_form = LoginRegistrationForm(self)
        self.login_form.show()
        if self.registration_form:
            self.registration_form.close()
        if self.main_window:
            self.main_window.close()

    def open_registration_form(self):
        from registration_form import RegistrationForm
        self.registration_form = RegistrationForm(self)
        self.registration_form.show()
        if self.login_form:
            self.login_form.close()

    def open_main_window(self, role):
        from main_window import MainWindow
        self.main_window = MainWindow(role)
        self.main_window.show()
        if self.login_form:
            self.login_form.close()
        if self.registration_form:
            self.registration_form.close()
