import requests, re, json, datetime

# 汇率网页
url = "https://mapi.gmoneytrans.net/exratenew1/Default.asp?country=china"

# 请求网页
res = requests.get(url)
res.encoding = "utf-8"

# 正则匹配 1 KRW = ? CNY
match = re.search(r"Exchange Rate\s*:\s*1\s*KRW\s*=\s*([\d\.]+)\s*CNY", res.text, re.IGNORECASE)
rate = float(match.group(1)) if match else None

# 构建输出数据
data = {
    "source": url,
    "rate": rate,
    "updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# 写入 rate.json
with open("rate.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

if rate:
    print("✅ Updated exchange rate:", data)
else:
    print("⚠️ 未获取到汇率，请检查网页结构或网络连接")
