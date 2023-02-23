import smtplib
import ssl
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B083GJ5ZKS/ref=va_live_carousel?pf_rd_r=VDWZXFBWBQDAMQJFYWAN&pf_rd_p=11a6ef0e-" \
      "351d-42c4-9265-8ac722f0c9ea&pf_rd_m=ATVPDKIKX0DER&pf_rd_t=HighVelocityEvent&pf_rd_i=deals_1_desktop&pf_rd_" \
      "s=slot-13&linkCode=ilv&tag=onamzalicecla-20&ascsubtag=Morning_Coffee_with_Austin_230222114526&asc_contentid=am" \
      "zn1.amazonlive.broadcast.51e667b7-7267-4314-8904-bec20e1d3e56&pd_rd_i=B083GJ5ZKS&th=1&psc=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())


price = soup.select_one('.a-price-whole').get_text()
price_as_float = int(price.split(".")[0])
print(price_as_float)



title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 80

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

ctx = ssl.create_default_context()
password = "YOUR PASSWORD"  # Your app password goes here
sender = "YOUR GMAIL@gmail.com"  # Your e-mail address
receiver = "YOUR EMAIL@yahoo.com"  # Recipient's address
message = f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)