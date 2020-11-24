import unittest
from common import HTMLTestRunner_cn

casePath = r"C:\xyauto\case"
rule = "test*.py"

discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

reportPath = r"C:\xyauto\report"+"report.html"
fp = open(reportPath,"wb")
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title="woshititiel",description="sdadawdawdadawda")
runner.run(discover)