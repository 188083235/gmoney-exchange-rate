import requests, re, json, datetime

url = "https://mapi.gmoneytrans.net/exratenew1/Default.asp?country=china"

# 先定义默认值
rate = 0
updated = datetime.datetime。now().strftime("%Y-%m-%d %H:%M:%S")

try:
    res = requests.get(url, timeout=10)
    res.encoding = "utf-8"
    html = res.text

    match = re.search(r"1\s*KRW\s*=\s*([\d\.]+)\s*CNY", html, re.IGNORECASE)
    if match:
        rate = float(match.group(1))

except Exception as e:
    print("⚠️ 请求失败或解析失败:", e)

# 无论成功失败，都写入 rate.json
data = {
    "source": url,
    "rate": rate,
    "updated": updated
}

with open("rate.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

if rate:
    print(f"✅ KRW → CNY Exchange Rate: 1 KRW = {rate} CNY")
else:
    print(f"⚠️ 未获取到汇率，已写入默认值 rate=0，updated={updated}")
