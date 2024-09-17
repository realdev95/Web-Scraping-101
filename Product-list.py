import requests
from bs4 import BeautifulSoup
import csv



url = "https://webscraper.io/test-sites/e-commerce/allinone"
r = requests.get(url)
print(r)

    
    




soup = BeautifulSoup(r.text, "lxml")
    
names = soup.find_all("a", class_="title")
for i in names:
    print(i.text)
desc = soup.find_all("p", class_="description card-text")
for i in desc:
    print(i.text)
price = soup.find_all("h4", class_="price float-end card-title pull-right")
for i in price:
    print(i.text)

filename = "test13.csv"

# Write the scraped data to the CSV file
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Description", "Price"])  # Write headers

    # Write the product name, description, and price to the CSV file
    for name, description, price_tag in zip(names, desc, price):
        writer.writerow([name.text.strip(), description.text.strip(), price_tag.text.strip()])

# Print confirmation message
print(f"Data saved to {filename}")                    