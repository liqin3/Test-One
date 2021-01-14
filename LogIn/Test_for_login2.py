import unittest
import os

from HTMLTestRunner import HTMLTestRunner

# 添加测试用例
test_dir = './'
discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='Test_for_login.py')
# 集成测试报告
report_name = '测试报告名称'
report_title = '测试报告标题'
report_desc = '测试报告描述'
report_path = './report/'
# 测试报告的完整路径
report_file = report_path+'report.html'
# 判断文件是否存在
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass
# HTMLTestRunner的使用
with open(report_file, 'wb') as report:
    # suite.addTests(cases)
    runner = HTMLTestRunner(stream=report, title=report_title, description=report_desc)
    runner.run(discover)