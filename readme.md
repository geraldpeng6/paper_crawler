# 帮助
## 原理
利用typeset.io进行论文爬取，获取标题和摘要

理论上可以获取更多其他信息。
## 使用前
主要使用selenium库进行爬取
使用前需要下载一个chromedriver

chromedriver的版本要和使用者电脑上的chrome浏览器版本对应。
## 使用过程
打开一个typeio.set的网页
在搜索栏输入想要查找的论文，选择筛选条件，获取想要的论文。

输入“启动”开始爬取，内容会自动保存到相对路径下的papers_info.csv文件中