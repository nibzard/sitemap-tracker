#!/usr/bin/env python3

import requests
import hashlib
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import csv
import os

SITEMAPS = {
    "definitions": "https://www.daytona.io/sitemap-definitions.xml",
    "dotfiles": "https://www.daytona.io/sitemap-dotfiles.xml"
}
CSV_FILE = "data/sitemap_stats.csv"  # Update this with the full path

def fetch_sitemap(url):
    response = requests.get(url)
    return response.text

def parse_sitemap(sitemap_content):
    root = ET.fromstring(sitemap_content)
    urls = [url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url')]
    return urls

def count_new_pages(sitemap_name, current_urls):
    current_hash = hashlib.md5(','.join(sorted(current_urls)).encode()).hexdigest()
    if not os.path.exists(CSV_FILE):
        return len(current_urls)
    with open(CSV_FILE, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        if len(rows) < 2:  # If there's only one or no entries, consider all URLs as new
            return len(current_urls)
        last_entry = next((row for row in reversed(rows) if row[0] == sitemap_name), None)
        if not last_entry or len(last_entry) < 5:
            return len(current_urls)
        last_hash = last_entry[4]
    if current_hash != last_hash:
        return len(current_urls)  # If hashes are different, consider all URLs as new
    return 0  # If hashes are the same, no new URLs

def update_csv(sitemap_name, date, total_count, new_count, urls):
    url_hash = hashlib.md5(','.join(sorted(urls)).encode()).hexdigest()
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
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