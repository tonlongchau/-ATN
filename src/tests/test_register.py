
from src.tests.base_test import BaseTest
from src.utility import xlReader
from selenium.webdriver.common.by import By


class TestRegister(BaseTest):

    def test_register(self):
        xlReader.load_excel()
        lastname = xlReader.get_cell_data(10, 3)
        firstname = xlReader.get_cell_data(11, 3)
        gender = xlReader.get_cell_data(12, 3)
        birthday = xlReader.get_cell_data(13, 3)
        email = xlReader.get_cell_data(14, 3)
        password = xlReader.get_cell_data(15, 3)

        self.registerPage.register(
            lastname, firstname, gender, birthday, email, password)
        assert self.registerPage.verifyRegister()

    def test_validate_email(self):
        xlReader.load_excel()
        lastname = xlReader.get_cell_data(10, 3)
        firstname = xlReader.get_cell_data(11, 3)
        gender = xlReader.get_cell_data(12, 3)
        birthday = xlReader.get_cell_data(13, 3)
        email = xlReader.get_cell_data(14, 3)
        password = xlReader.get_cell_data(15, 3)
        # launch url
        self.registerPage.register(
            lastname, firstname, gender, birthday, email, password)

        assert "Email đã tồn tại. Nếu bạn quên mật khẩu, bạn có thể thiết lập lại mật khẩu tại đây."\
            in self.registerPage.get_error_text()

    def test_validate_birthday(self):
        xlReader.load_excel()
        lastname = xlReader.get_cell_data(10, 3)
        firstname = xlReader.get_cell_data(11, 3)
        gender = xlReader.get_cell_data(12, 3)
        birthday = xlReader.get_cell_data(21, 3)
        email = xlReader.get_cell_data(15, 3)
        password = xlReader.get_cell_data(15, 3)
        # launch url
        self.registerPage.register(
            lastname, firstname, gender, birthday, email, password)
        assert "Ngày sinh không hợp lệ"\
            in self.registerPage.get_error_text()

    def test_validate_password(self):
        xlReader.load_excel()
        lastname = xlReader.get_cell_data(10, 3)
        firstname = xlReader.get_cell_data(11, 3)
        gender = xlReader.get_cell_data(12, 3)
        birthday = xlReader.get_cell_data(13, 3)
        email = xlReader.get_cell_data(16, 3)
        password = xlReader.get_cell_data(20, 3)
        # launch url
        self.registerPage.register(
            lastname, firstname, gender, birthday, email, password)
        assert "Mật khẩu quá ngắn (tối thiểu 5 ký tự)."\
            in self.registerPage.get_error_text()
