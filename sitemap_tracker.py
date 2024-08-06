#!/usr/bin/env python3
import requests
import hashlib
import xml.etree.ElementTree as ET
from datetime import datetime
import csv
import os

SITEMAPS = {
    "definitions": "https://www.daytona.io/sitemap-definitions.xml",
    "dotfiles": "https://www.daytona.io/sitemap-dotfiles.xml"
}
CSV_FILE = "data/sitemap_stats.csv"

def fetch_sitemap(url):
    response = requests.get(url)
    return response.text

def parse_sitemap(sitemap_content):
    root = ET.fromstring(sitemap_content)
    urls = [url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url')]
    return urls

def get_last_entry(sitemap_name):
    if not os.path.exists(CSV_FILE):
        return None
    with open(CSV_FILE, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        if len(rows) < 2:  # If there's only header or no entries
            return None
        for row in reversed(rows):
            if row[0] == sitemap_name:
                return row
    return None

def count_new_pages(sitemap_name, current_urls):
    last_entry = get_last_entry(sitemap_name)
    if not last_entry:
        return len(current_urls)

    last_total = int(last_entry[2])
    current_total = len(current_urls)

    if current_total > last_total:
        return current_total - last_total
    return 0

def update_csv(sitemap_name, date, total_count, new_count, urls):
    url_hash = hashlib.md5(','.join(sorted(urls)).encode()).hexdigest()
    file_exists = os.path.exists(CSV_FILE)

    if file_exists:
        with open(CSV_FILE, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)

        # Check if there's already an entry for this sitemap and date
        for i, row in enumerate(rows):
            if row[0] == sitemap_name and row[1] == date.strftime("%Y-%m-%d"):
                # Update existing entry
                rows[i] = [sitemap_name, date.strftime("%Y-%m-%d"), total_count, new_count, url_hash]
                break
        else:
            # If no existing entry found, append new row
            rows.append([sitemap_name, date.strftime("%Y-%m-%d"), total_count, new_count, url_hash])

        # Write updated data back to CSV
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
    else:
        # If file doesn't exist, create it with header and first entry
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Sitemap", "Date", "Total URLs", "New URLs", "URL Hash"])
            writer.writerow([sitemap_name, date.strftime("%Y-%m-%d"), total_count, new_count, url_hash])

def process_sitemap(sitemap_name, url):
    print(f"Processing {sitemap_name} sitemap at {datetime.now()}")
    sitemap_content = fetch_sitemap(url)
    urls = parse_sitemap(sitemap_content)
    new_count = count_new_pages(sitemap_name, urls)
    total_count = len(urls)
    update_csv(sitemap_name, datetime.now(), total_count, new_count, urls)
    print(f"{sitemap_name} sitemap - Total URLs: {total_count}, New URLs since last run: {new_count}")

def main():
    for sitemap_name, url in SITEMAPS.items():
        process_sitemap(sitemap_name, url)

if __name__ == "__main__":
    main()