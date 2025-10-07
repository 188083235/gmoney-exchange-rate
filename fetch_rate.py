import requests, re, json, datetime

# 汇率 API/网页
url = "https://mapi.gmoneytrans.net/exratenew1/Default.asp?country=china"

try:
    res = requests.get(url, timeout=10)
    res.encoding = "utf-8"
    html = res.text

    # 正则匹配 Exchange Rate
    match = re.search(r"1\s*KRW\s*=\s*([\d\.]+)\s*CNY", html)
    if match:
        rate = float(match.group(1))
        updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        rate = 无
        updated = "N/A"

except Exception as e:
    print("⚠️ 请求失败:", e)
    rate = 无
    updated = "N/A"

# 输出到 rate.json
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
    print("⚠️ 未获取到汇率，请检查网页或接口")
