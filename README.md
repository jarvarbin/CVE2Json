# CVE2Json


Sets the year to get the CVEs for, and sets the URL for the NVD website to the year specified. It then sends a GET request to the NVD website and parses the HTML response using the BeautifulSoup library. It then gets the table element with the id of "vuln-list-table", which contains the list of CVEs.

The script then iterates over the rows in the table and gets the columns in each row. It skips rows that don't have at least 5 columns, as these rows don't contain the necessary information for a CVE. For each valid row, it gets the CVE ID and description from the first and fifth columns, respectively, and appends this information to the cves list.

After the loop, the script saves the cves list to a JSON file called cves.json using the json.dump function. This will create a JSON file with a list of objects, where each object contains the cve_id and description for a single CVE.



