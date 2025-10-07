from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json, datetime
import time

url = "https://mapi.gmoneytrans.net/exratenew1/Default.asp?country=china"

# Chrome 无头模式
options = 选项()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 启动浏览器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

# 等待页面 JS 渲染
time.sleep(3)  # 根据需要调整等待时间

# 直接通过 id 获取元素
rate_text = driver.find_element("id", "rate").text

# 解析汇率数字，例如 "1 KRW = 0.005023 CNY"
rate = float(rate_text.split('=')[1].split()[0])

updated = datetime.datetime.当前()。strftime("%Y-%m-%d %H:%M:%S")

data = {
    "source": url,
    "rate": rate,
    "updated": updated
}

with open("rate.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ KRW → CNY Exchange Rate: 1 KRW = {rate} CNY")

driver.quit()
