import csv
import hashlib
from datetime import datetime, timedelta
import random

def generate_url_hash(url_part):
    return hashlib.md5(url_part.encode()).hexdigest()

def generate_dummy_data(start_date, weeks=4):
    data = [
        ["definitions", "2024-08-06", 105, 2, "8d319cac47c21a349be4c2d34b034f69"],
        ["dotfiles", "2024-08-06", 155, 8, "6390ecf9a35f79f37e950411334aa911"],
        ["definitions", "2024-08-13", 108, 3, "5c25127c25fec7b735b24ed646bebc16"],
        ["dotfiles", "2024-08-13", 164, 9, "b9b5992749a9d1b6ed2149bf8f8cee8f"]
    ]

    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    sitemap_info = {
        "definitions": {"total": 108, "new": 3},
        "dotfiles": {"total": 164, "new": 9}
    }

    for week in range(weeks):  # Generate data for the specified number of weeks
        current_date += timedelta(days=7)

        for sitemap in sitemap_info:
            # Generate a new random number of URLs for this week
            new_urls = random.randint(0, 10)

            # Increment the count of total and new URLs
            sitemap_info[sitemap]["new"] = new_urls
            sitemap_info[sitemap]["total"] += new_urls

            # Create a new row with updated data
            new_date = current_date.strftime("%Y-%m-%d")
            new_row = [
                sitemap,
                new_date,
                sitemap_info[sitemap]["total"],
                sitemap_info[sitemap]["new"],
                generate_url_hash(sitemap + new_date)
            ]
            data.append(new_row)

    return data

# Generate dummy data for an additional 4 weeks (you can adjust this as needed)
dummy_data = generate_dummy_data("2024-08-13", weeks=20)

# Save to CSV file
with open('dummy_sitemap_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Sitemap", "Date", "Total URLs", "New URLs", "URL Hash"])
    writer.writerows(dummy_data)