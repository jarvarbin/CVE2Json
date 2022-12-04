# Import the necessary modules
import json
import requests
from bs4 import BeautifulSoup


# Set the year to get the CVEs for
year = 2020

# Set the URL for the NVD website
nvd_url = f"https://nvd.nist.gov/vuln/full-listing/{year}"

# Send a GET request to the NVD website
response = requests.get(nvd_url)

# Parse the HTML response
soup = BeautifulSoup(response.text, "html.parser")

# Get the table with the CVEs
cve_table = soup.find("table", id="vuln-list-table")

# Initialize a list for the CVEs
cves = []

# Iterate over the rows in the table
for row in cve_table.find_all("tr"):
    # Get the columns in the row
    columns = row.find_all("td")

    # Skip rows without enough columns
    if len(columns) < 5:
        continue

    # Get the CVE ID and description
    cve_id = columns[0].text
    description = columns[4].text

    # Append the CVE to the list
    cves.append({"cve_id": cve_id, "description": description})

# Save the CVEs to a JSON file
with open("cves.json", "w") as f:
    json.dump(cves, f)
