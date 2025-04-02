import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QShortcut, QLineEdit
from PyQt5.QtGui import QIntValidator, QKeySequence
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate

class FormValidation(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("form_validation.ui", self)

        self.age.setValidator(QIntValidator(1, 120, self))

        shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        shortcut.activated.connect(self.close)

        self.number.setText("+62 ")  
        self.number.textChanged.connect(self.format_phone_number)
        self.number.setMaxLength(17)  

        self.save.clicked.connect(self.validate_form)
        self.clear.clicked.connect(self.confirm_clear_fields)

        self.dob.dateChanged.connect(self.update_age_from_dob)

    def format_phone_number(self):
        text = self.number.text()
        if not text.startswith("+62 "):
            self.number.setText("+62 ")
        
        numbers = re.sub(r'[^0-9]', '', text.replace("+62", ""))  
        numbers = numbers[:11]  
        
        formatted = "+62 "
        if len(numbers) > 3:
            formatted += numbers[:3] + "-"
            numbers = numbers[3:]
        if len(numbers) > 4:
            formatted += numbers[:4] + "-"
            numbers = numbers[4:]
        formatted += numbers
        
        self.number.setText(formatted)
        self.number.setCursorPosition(len(formatted))

    def update_age_from_dob(self):
        dob_date = self.dob.date()
        if dob_date.isValid():
            today = QDate.currentDate()
            age = today.year() - dob_date.year()

            if today.month() < dob_date.month() or (today.month() == dob_date.month() and today.day() < dob_date.day()):
                age -= 1 

            self.age.setText(str(age))

    def validate_form(self):
        self.reset_field_styles()
        errors = []

        if not self.validate_name():
            errors.append("❌ Invalid name!")
        if not self.validate_email():
            errors.append("❌ Use the right email address! (example@gmail.com)")
        if not self.validate_age():
            errors.append("❌ Age must be a number!")
        if not self.validate_phone():
            errors.append("❌ Phone number must be 13 digits!")
        if not self.validate_address():
            errors.append("❌ Address cannot be empty!")
        if not self.validate_gender():
            errors.append("❌ Please select your gender!")
        if not self.validate_education():
            errors.append("❌ Please select your last education!")
        if not self.validate_dob():  
            errors.append("❌ Date of birth is not valid!")
        if not self.validate_dob_and_age():  
            errors.append("❌ Age and Date of Birth do not match!")

        if errors:
            self.show_warning("\n".join(errors))
            return

        QMessageBox.information(self, "✅ Success", "Your data has been successfully saved!")
        self.clear_fields()

    def validate_name(self):
        name = self.name.text().strip()
        if not name or len(name) < 3 or any(char.isdigit() for char in name):
            self.set_error_style(self.name)
            return False
        return True

    def validate_email(self):
        email = self.email.text().strip()
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_pattern, email):
            self.set_error_style(self.email)
            return False
        return True

    def validate_age(self):
        age = self.age.text().strip()
        if not age.isdigit():
            self.set_error_style(self.age)
            return False
        return True

    def validate_phone(self):
        number_digits = re.sub(r'[^0-9]', '', self.number.text().replace("+62", ""))
        if len(number_digits) != 11:
            self.set_error_style(self.number)
            return False
        return True

    def validate_address(self):
        address = self.address.toPlainText().strip()
        if not address:
            self.set_error_style(self.address)
            return False
        return True

    def validate_gender(self):
        gender = self.gender.currentText()
        if gender == "":
            self.set_error_style(self.gender)
            return False
        return True

    def validate_education(self):
        education = self.edu.currentText()
        if education == "":
            self.set_error_style(self.edu)
            return False
        return True

    def validate_dob(self):
        dob_date = self.dob.date()  
        if dob_date.isValid():
            today = QDate.currentDate()
            age = today.year() - dob_date.year()
            
            if today.month() < dob_date.month() or (today.month() == dob_date.month() and today.day() < dob_date.day()):
                age -= 1

            if age < 1 or age > 120:
                self.set_error_style(self.dob)
                return False
        else:
            self.set_error_style(self.dob)
            return False
        return True

    def validate_dob_and_age(self):
        age_input = self.age.text().strip()
        if age_input.isdigit():
            age_input = int(age_input)
            dob_date = self.dob.date()

            today = QDate.currentDate()
            calculated_age = today.year() - dob_date.year()
            
            if today.month() < dob_date.month() or (today.month() == dob_date.month() and today.day() < dob_date.day()):
                calculated_age -= 1

            if age_input != calculated_age:
                self.set_error_style(self.age)
                self.set_error_style(self.dob)
                return False

        elif self.dob.date().isValid():
            dob_date = self.dob.date()
            today = QDate.currentDate()
            calculated_age = today.year() - dob_date.year()
            
            if today.month() < dob_date.month() or (today.month() == dob_date.month() and today.day() < dob_date.day()):
                calculated_age -= 1

            if age_input and int(age_input) != calculated_age:
                self.set_error_style(self.age)
                self.set_error_style(self.dob)
                return False

        return True

    def confirm_clear_fields(self):
        reply = QMessageBox.question(self, "Confirmation", "Are you sure you want to clear all data?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.clear_fields()

    def clear_fields(self):
        try:
            self.name.clear()
            self.email.clear()
            self.age.clear()
            self.number.setText("+62 ")  
            self.address.clear()
            self.gender.setCurrentIndex(0)
            self.edu.setCurrentIndex(0)
            self.dob.setDate(QDate())  
            self.reset_field_styles()
        except Exception as e:
            print(f"Error while clearing fields: {e}")


    def show_warning(self, message):
        QMessageBox.warning(self, "⚠️ Warning", message)

    def set_error_style(self, widget):
        widget.setStyleSheet("border: 2px solid red;")

    def reset_field_styles(self):
        default_style = "border: 1px solid gray; border-radius: 4px; padding: 2px;"
        self.name.setStyleSheet(default_style)
        self.email.setStyleSheet(default_style)
        self.age.setStyleSheet(default_style)
        self.number.setStyleSheet(default_style)
        self.address.setStyleSheet(default_style)
        self.gender.setStyleSheet(default_style)
        self.edu.setStyleSheet(default_style)
        self.dob.setStyleSheet(default_style)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormValidation()
    window.show()
    sys.exit(app.exec_())
