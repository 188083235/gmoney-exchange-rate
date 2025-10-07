import requests, re, json, datetime

url = "https://mapi.gmoneytrans.net/exratenew1/Default.asp?country=china"

try:
    res = requests.get(url, timeout=10)
    res.encoding = "utf-8"
    html = res.text

    match = re.search(r"1\s*KRW\s*=\s*([\d\.]+)\s*CNY", html)
    rate = float(match.group(1)) if match else 0  # 未抓到就用 0
    updated = datetime.datetime.当前()。strftime("%Y-%m-%d %H:%M:%S")

except Exception as e:
    print("⚠️ 请求失败:", e)
    rate = 0
    updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
    print("⚠️ 未获取到汇率，已写入 rate.json，rate=0")
