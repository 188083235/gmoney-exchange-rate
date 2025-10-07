import requests, re, json, datetime

url = "https://mapi.gmoneytrans.net/exratenew1/Default.asp?country=china"
res = requests.get(url)
res.encoding = "utf-8"

match = re.search(r"Exchange Rate\s*:\s*1\s*KRW\s*=\s*([\d\.]+)\s*CNY", res.text)
rate = float(match.group(1)) if match else None

data = {
    "source": url,
    "rate": rate,
    "updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

with open("rate.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Updated exchange rate:", data)
