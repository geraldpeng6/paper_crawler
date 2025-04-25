# Paper Crawler - 论文爬虫工具

## 项目简介
这是一个基于Python的论文爬虫工具，利用typeset.io网站进行学术论文的自动化爬取。该工具可以帮助研究人员、学生和学者快速获取大量论文的标题、摘要等信息，提高文献检索和整理的效率。

## 工作原理
本工具使用Selenium自动化测试框架模拟用户在typeset.io网站上的浏览行为，自动提取论文的标题、URL和摘要信息。爬取的数据将保存为CSV格式，方便后续分析和处理。

理论上，该工具可以根据需求扩展，获取更多论文相关信息，如作者、发表日期、引用次数等。

## 环境要求
- Python 3.9+
- 虚拟环境（推荐使用uv进行管理）
- Chrome浏览器
- ChromeDriver（与Chrome浏览器版本对应）

## 安装步骤

### 1. 克隆仓库
```bash
git clone [仓库地址]
cd paper_crawler
```

### 2. 创建并激活虚拟环境
使用uv创建虚拟环境（推荐）：
```bash
uv venv
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate  # Windows
```

或使用传统方式：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

### 3. 安装依赖
```bash
uv pip install -r requirements.txt
# 或
pip install -r requirements.txt
```

### 4. 下载ChromeDriver
请确保下载的ChromeDriver版本与您的Chrome浏览器版本相匹配。
- 下载地址：https://chromedriver.chromium.org/downloads
- 将下载的ChromeDriver放置在项目根目录下

## 使用指南

### 1. 启动程序
```bash
python main.py
```

### 2. 操作步骤
1. 程序启动后，Chrome浏览器会自动打开并访问typeset.io网站
2. 在网站搜索栏中输入您感兴趣的论文关键词
3. 根据需要设置筛选条件（如发表年份、学科领域等）
4. 当搜索结果显示您需要的论文列表后，返回命令行
5. 在命令行中输入"启动"并按回车，开始自动爬取过程
6. 爬取完成后，结果将保存在项目目录下的CSV文件中（文件名格式：papers_info_年月日_时分秒.csv）

### 3. 数据输出
爬取的数据将包含以下字段：
- 论文标题（Title）
- 论文URL（url）
- 论文摘要（Abstract）

## 注意事项
1. 请确保网络连接稳定，特别是在使用代理的情况下
2. 如需修改代理设置，请编辑main.py文件中的proxy变量
3. 爬取大量数据时，请注意控制频率，避免对目标网站造成过大负担
4. 爬取的数据仅用于学术研究，请遵守相关法律法规和网站使用条款

## 常见问题
1. **ChromeDriver版本不匹配**：请确保下载的ChromeDriver版本与您的Chrome浏览器版本相匹配
2. **网络连接问题**：检查网络连接和代理设置
3. **无法找到元素**：网站结构可能已更新，需要相应调整代码中的XPath选择器

## 贡献指南
欢迎提交问题报告和改进建议。如果您想贡献代码，请遵循以下步骤：
1. Fork本仓库
2. 创建您的特性分支
3. 提交您的更改
4. 推送到您的分支
5. 创建Pull Request

## 许可证
[添加许可证信息]
