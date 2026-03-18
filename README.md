# 🕸️ Web Scraping Practice (Python)

This repository contains multiple small projects to practice **Python basics and web scraping with online data**.

---

## 📘 Project 1 — BeautifulSoup Tutorial

File: `BeautifulSoup_Tuti.ipynb`

This notebook was mainly a **tutorial to learn BeautifulSoup**, a Python library used for web scraping.

In this notebook I practiced:
- Sending HTTP requests using `requests`
- Parsing HTML pages using `BeautifulSoup`
- Extracting links and images from websites

I also tried using an **external API (remove.bg)** to remove the background from an image.
The API sends an image and returns a new image without the background.

---

## 🌍 Project 2 — Web Scraping Real Data

File: `Web_Scrape.ipynb`

This notebook applies the same web scraping idea but on **real data from the internet**.

The notebook:
- Scrapes data from a website
- Extracts tables and useful information
- Converts data into a **Pandas DataFrame**
- Cleans the data
- Exports it into a CSV file

Example output:
`Data.csv`

This workflow is commonly used in **data collection and analysis projects**.

---

## 🤖 Project 3 — Selenium Automation

File: `seleniumTUT.py`

This project uses **Selenium** to automate browser actions and scrape images from Google.

In this script I practiced:
- Automating browser using Selenium WebDriver
- Searching on Google automatically
- Navigating to the Images section
- Scrolling the page to load more results
- Extracting image URLs
- Saving the results into a CSV file using Pandas

Example output:
`images_google.csv`

---

## ⚙️ Tools Used

- Python
- Requests
- BeautifulSoup
- Selenium
- Pandas
- Jupyter Notebook
- remove.bg API
