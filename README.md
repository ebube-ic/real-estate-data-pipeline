# Real Estate Data Pipeline

A Python web scraper that extracts 239 real estate listings from 
Zameen.com and visualizes the data in Tableau.

## Tools Used
- Python (requests, BeautifulSoup, pandas)
- Tableau Public

## What it does
- Scrapes 10 pages of real estate listings from Zameen.com
- Extracts property title, price, location, bedrooms, baths and area
- Converts mixed price units (Crore/Lakh) into a single numeric scale
- Filters out incomplete listings for clean data
- Exports to CSV and visualizes in Tableau

## Key Concepts Demonstrated
- Anti-bot bypassing with User-Agent headers
- Targeting stable aria-label attributes over dynamic class names
- Conditional data extraction to handle missing fields
- Unit conversion and data cleaning with pandas

## Dashboard
[View live on Tableau Public](https://public.tableau.com/app/profile/ebube.amadi6368/viz/RealEstateListingsDashboard_17817367026080/RealEstateListingsDashboard)

## Files
- `real_estate_scraper.py` — the scraper script
- `real_estate_listings.csv` — the cleaned dataset
