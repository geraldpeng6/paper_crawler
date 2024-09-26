from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime

# 设置Chrome驱动路径和代理
chrome_driver_path = 'chromedriver.exe'

# 代理设置，需要自己设置端口
chrome_options = Options()
proxy = 'http://localhost:7890'
chrome_options.add_argument(f'--proxy-server={proxy}')

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打开目标网址
base_url = 'http://typeset.io/'
driver.get(base_url)
input("准备好了请输入启动：")

# 显式等待，等待元素加载
wait = WebDriverWait(driver, 10)  # 等待最多10秒

# 这一步是找论文链接
links = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="text-primary text-base no-underline hover:underline"]')))
print(links)

# 存结果的列表
results = []

for link in links:
    # 获取论文标题
    title = link.find_element(By.TAG_NAME, 'span').text
    print(title)
    # 获取 href 属性并拼接成完整的 URL
    href = link.get_attribute('href')
    print(f'Opening URL: {href}')

    # 在新窗口中打开链接
    driver.execute_script(f'window.open("{href}");')

    # 切换到新窗口
    driver.switch_to.window(driver.window_handles[-1])

    # 等待摘要元素加载
    try:
        abstract_element = wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="text-15"]/span[contains(text(),"Abstract")]/parent::div'))
        )
        abstract = abstract_element.text
        print(abstract)
    except:
        # 有些论文的网页会没有abstract
        abstract = 'Abstract not found'

    results.append({
        'Title': title,
        'url': href,
        'Abstract': abstract
    })

    # 关闭当前窗口并切回原窗口
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
df = pd.DataFrame(results)

# 保存数据到CSV文件
df.to_csv(f'papers_info_{current_time}.csv', index=False)
driver.quit()
