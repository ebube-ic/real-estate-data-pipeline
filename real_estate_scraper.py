import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

all_properties = []
print("Starting Real Estate Data Pipeline...")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

for page_num in range(1, 11):
    url = f"https://www.zameen.com/Homes/Lahore-1-{page_num}.html"
    print(f"Scraping page {page_num}/10: {url}")

    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Warning: Failed. Status Code: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        properties = soup.find_all("li", attrs={"aria-label": "Listing"})

        print(f"Found {len(properties)} properties on page {page_num}")

        for prop in properties:
            title = prop.find("h2")
            price = prop.find("span", attrs={"aria-label": "Price"})
            location = prop.find("div", attrs={"aria-label": "Location"})
            beds = prop.find("span", attrs={"aria-label": "Beds"})
            baths = prop.find("span", attrs={"aria-label": "Baths"})
            area = prop.find("span", attrs={"aria-label": "Area"})

            all_properties.append({
                "Title": title.text.strip() if title else "N/A",
                "Price": price.text.strip() if price else "N/A",
                "Location": location.text.strip() if location else "N/A",
                "Bedrooms": beds.text.strip() if beds else "N/A",
                "Baths" : baths.text.strip() if baths else "N/A",
                "Area": area.text.strip() if area else "N/A",
            })
        time.sleep(1)

    except Exception as e:
        print(f"Error on page {page_num}: {e}")
        continue

def convert_to_lakh(price_str):
    if "Crore" in price_str:
        number = float(price_str.replace("Crore", "").strip())
        return number*100
    elif "Lakh" in price_str:
        number = float(price_str.replace("Lakh", "").strip())
        return number
    else:
        return None

df = pd.DataFrame(all_properties)

df = df[df["Bedrooms"] != "N/A"]
df["Price"] = df["Price"].apply(convert_to_lakh)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Baths"] = pd.to_numeric(df["Baths"], errors="coerce")
df["Bedrooms"] = pd.to_numeric(df["Bedrooms"], errors="coerce")

df.to_csv("real_estate_listings.csv", index=False)
print(f"\nDone! Extracted {len(df)} properties.")
print("Saved as real_estate_listings.csv")