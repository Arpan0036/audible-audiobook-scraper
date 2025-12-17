# Audible Audiobook Data Extraction (Selenium + Python)

This project demonstrates a Python Selenium automation script that extracts audiobook information from a publicly available, paginated listing page and stores the data in an Excel file using Pandas.

The goal of this project is to practice real-world web automation concepts such as pagination handling, structured data extraction, and basic data cleaning.

---

## 🔍 Features

- URL-based pagination handling
- Extraction of multiple audiobook attributes:
  - Audiobook title
  - Author name
  - Audio length
  - Release date
  - Customer ratings
  - Price
- Basic text cleaning for rating data
- Exporting structured data to Excel (`.xlsx`) using Pandas

---

## 🛠️ Tech Stack

- Python
- Selenium WebDriver
- Pandas
- ChromeDriver

---

## ⚙️ How It Works

1. The script iterates through multiple paginated pages using the `page` query parameter.
2. For each page, Selenium locates and extracts audiobook details using XPath.
3. Extracted data is stored in Python lists.
4. The collected data is converted into a Pandas DataFrame.
5. The final dataset is exported to an Excel file.

---
