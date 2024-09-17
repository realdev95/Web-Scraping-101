import requests
from bs4 import BeautifulSoup
import csv

def scrape_flipkart(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return "Error fetching the page"

        soup = BeautifulSoup(r.text, "lxml")

        # Find the correct class for reviews (replace with the actual class from the website)
        rev_desc = soup.find_all("div", class_="_16PBlm")  # Update the class name based on Flipkart's structure

        if not rev_desc:
            return "No reviews found"

        # Extract product name from URL (this is just an example; modify according to your need)
        product_name = url.split('/')[3]  # Example logic to extract product name

        # Prepare CSV filename based on product name and page
        filename = f"flipkart_{product_name}_page.csv"
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Reviews"])

            for review in rev_desc:
                writer.writerow([review.text.strip()])

        return filename

    except Exception as e:
        return str(e)


def scrape_amazon(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return "Error fetching the page"

        soup = BeautifulSoup(r.text, "lxml")

        # Find the correct class for reviews (replace with the actual class from the website)
        rev_desc = soup.find_all("span", class_="a-size-base review-text review-text-content")  # Update the class name

        if not rev_desc:
            return "No reviews found"

        # Extract product name from URL (this is just an example; modify according to your need)
        product_name = url.split('/')[3]  # Example logic to extract product name

        # Prepare CSV filename based on product name and page
        filename = f"amazon_{product_name}_page.csv"
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Reviews"])

            for review in rev_desc:
                writer.writerow([review.text.strip()])

        return filename

    except Exception as e:
        return str(e)
class Scraper:
    def __init__(self, platform, scrape_option, url):
        self.platform = platform
        self.scrape_option = scrape_option
        self.url = url

    # Flipkart Catalogue Scraping
    def scrape_flipkart_catalog(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "lxml")

        # Extract data for Flipkart product catalogue
        desc = soup.find_all("a", class_="wjcEIp")
        for i in desc:
            print(i.text)
        catg = soup.find_all("div", class_="NqpwHC")
        for i in catg:
            print(i.text)
        ratings = soup.find_all("div", class_="XQDdHH")
        for i in ratings:
            print(i.text)
        price = soup.find_all("div", class_="Nx9bqj")
        for i in price:
            print(i.text)

        product_name = self.url.split('/')[3]  # Example logic for product name
        filename = f"flipkart_{product_name}_catalog.csv"

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Category", "Ratings", "Price"])
            for description, category, rating, price_tag in zip(desc, catg, ratings, price):
                writer.writerow([description.text.strip(), category.text.strip(), rating.text.strip(), price_tag.text.strip()])

        return filename

    # Amazon Catalogue Scraping
    def scrape_amazon_catalog(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "lxml")

        # Extract data for Amazon product catalogue
        desc = soup.find_all("span", class_="a-size-medium a-color-base a-text-normal")
        for i in desc:
            print(i.text)
        ratings = soup.find_all("span", class_="a-icon-alt")
        for i in ratings:
            print(i.text)
        price = soup.find_all("span", class_="a-price-whole")
        for i in price:
            print(i.text)

        product_name = self.url.split('/')[3]  # Example logic for product name
        filename = f"amazon_{product_name}_catalog.csv"

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Ratings", "Price"])
            for description, rating, price_tag in zip(desc, ratings, price):
                writer.writerow([description.text.strip(), rating.text.strip(), price_tag.text.strip()])

        return filename