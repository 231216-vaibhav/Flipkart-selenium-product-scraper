# Flipkart Laptop Scraper

A Python web scraping project that collects laptop listings from Flipkart and converts them into a structured dataset.

The scraper uses **Selenium** to load dynamic pages and **BeautifulSoup** to extract product data. The extracted information is cleaned and exported into a CSV file using **Pandas**.

This project demonstrates practical skills in **web scraping, HTML parsing, and data processing using Python**.

---

## Features

* Scrapes laptop product listings from Flipkart
* Extracts important product information:

  * Product Title
  * Price
  * Product Link
* Saves raw HTML pages for parsing
* Converts scraped data into a structured CSV dataset
* Clean project structure for easy understanding and maintenance

---

## Project Structure

```
flipkart-selenium-product-scraper
│
├── scraper
│   ├── collect.py        # Collects laptop product HTML pages
│   ├── main1.py          # Parses HTML files and creates dataset
│
├── output
│   ├── data              # Stored HTML files from scraped pages
│   └── products.csv      # Final dataset
│
├── docs
│   ├── Features Section.txt
│   ├── Libraries.txt
│   ├── Sample Output.txt
│   ├── how to run.txt
│   └── installation_structure.txt
│
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/231216-vaibhav/Flipkart-selenium-product-scraper.git
```

Move into the project directory:

```
cd Flipkart-selenium-product-scraper
```

Create a virtual environment:

```
python -m venv .venv
```

Activate the virtual environment (Windows):

```
.venv\Scripts\activate
```

Install dependencies:

```
pip install selenium beautifulsoup4 pandas
```

---

## How to Run

Step 1 – Collect product HTML pages

```
python scraper/collect.py
```

Step 2 – Extract data and generate dataset

```
python scraper/main1.py
```

After running the scripts, the final dataset will appear here:

```
output/products.csv
```

---

## Example Dataset Output

```
title,price,link
Samsung Galaxy Book4 Intel Core i5,49790,https://www.flipkart.com/...
HP 15s Intel Core i3,36999,https://www.flipkart.com/...
Lenovo IdeaPad Slim 3 Ryzen 5,42990,https://www.flipkart.com/...
```

---

## Technologies Used

* Python
* Selenium
* BeautifulSoup
* Pandas
* Chrome WebDriver

---

## Disclaimer

This project is intended for **educational purposes only**.
Please respect website terms of service and robots.txt rules when scraping data.

---

## Author

**Vaibhav Kumar Gupta**
