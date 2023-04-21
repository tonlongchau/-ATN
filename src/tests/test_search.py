from src.tests.base_test import BaseTest
from src.utility import xlReader

class TestSearch(BaseTest):

    def test_search(self):
        xlReader.load_excel()
        searchname = xlReader.get_cell_data(20, 3)
        self.searchPage.search(searchname)
        self.searchPage.product_result()
        
    def test_search_not_found(self):
        xlReader.load_excel()
        searchname = xlReader.get_cell_data(21, 3)
        self.searchPage.search(searchname)
        assert "Không tìm thấy nội dung bạn yêu cầu"\
        in self.searchPage.get_error()