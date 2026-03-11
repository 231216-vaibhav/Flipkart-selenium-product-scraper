from bs4 import BeautifulSoup
import os
import pandas as pd

data = []

for file in os.listdir("data"):

    if not file.endswith(".html"):
        continue

    with open(f"data/{file}", "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    title_tag = soup.find("div", class_="RG5Slk")
    price_tag = soup.find("div", class_="hZ3P6w")
    link_tag = soup.find("a", class_="k7wcnx")

    if not title_tag or not price_tag or not link_tag:
        continue

    title = title_tag.get_text(strip=True)

    price = price_tag.get_text(strip=True)
    price = price.replace("â‚¹", "₹")

    link = "https://www.flipkart.com" + link_tag["href"]

    data.append({
        "title": title,
        "price": price,
        "link": link
    })

df = pd.DataFrame(data)

df.to_csv("products.csv", index=False, encoding="utf-8")

print("CSV created successfully")