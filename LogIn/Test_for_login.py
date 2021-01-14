import unittest
from selenium import webdriver
from time import sleep
from ddt import file_data, ddt, data
@ddt
class UnitForTest(unittest.TestCase):
    # 前置条件
    def setUp(self) -> None:
        self.wd = webdriver.Chrome()
        self.wd.get("https://www.jiandaoyun.com/signin")
        self.wd.maximize_window()
        self.wd.implicitly_wait(5)
    # 登录
    @file_data('user.yaml')
    def test_1(self, **user):
        name = user.get('user')
        pwd = user.get('pwd')
        # print(name)
        # print(pwd)
        self.wd.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/input').send_keys(name)
        sleep(3)
        self.wd.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/input').send_keys(pwd)
        sleep(3)
        self.wd.find_element_by_class_name('login-btn').click()
        sleep(5)
        text = self.wd.find_element_by_xpath('//*[@id="header"]/div/div[2]/div[3]/div/span').text
        sleep(5)
        # self.we.quit()
        self.assertEqual('工作台', text, msg='登录失败')
    def test_2(self):
        print("test2")
    # 后置条件
    def tearDown(self) -> None:
        self.wd.quit()
if __name__=="__main__":
    unittest.main()


