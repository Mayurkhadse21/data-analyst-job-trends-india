#PHASE 1: SCRAPE JOB POSTINGS

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_job_listings(query, location, pages=2):
    job_list = []

    for page in range(pages):
        url = f"https://www.indeed.com/jobs?q={query}&l={location}&start={page*10}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("div", class_="job_seen_beacon")

        for job in jobs:
            title = job.find("h2", class_="jobTitle")
            company = job.find("span", class_="companyName")
            location = job.find("div", class_="companyLocation")
            summary = job.find("div", class_="job-snippet")
            date = job.find("span", class_="date")
            link = job.find("a", href=True)

            job_list.append({
                "Job Title": title.text.strip() if title else None,
                "Company": company.text.strip() if company else None,
                "Location": location.text.strip() if location else None,
                "Summary": summary.text.strip().replace("\n", " ") if summary else None,
                "Date Posted": date.text.strip() if date else None,
                "Link": "https://www.indeed.com" + link["href"] if link else None
            })

        time.sleep(2)  # Sleep to avoid blocking

    return pd.DataFrame(job_list)
