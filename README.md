# 🕸️ Web Scraping Practice (Python)

This repository contains two small projects to practice **web scraping and working with online data using Python**.

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

The notebook scrapes data from a website, extracts a table of information, converts it into a **Pandas DataFrame**, cleans the data, and then exports it into a CSV file.

Example output:
Data.csv


This type of workflow is commonly used in **data collection and data analysis projects**.

---

## ⚙️ Tools Used

- Python
- Requests
- BeautifulSoup
- Pandas
- Jupyter Notebook
- remove.bg API
