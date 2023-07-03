from lib.html_snippets.SalesNav import results_html
from scraping.salesNav_scraping import *
from scraping.scraper_tools  import *
import json

def main():
    result_data = get_lead_data(results_html)

    print(len(result_data))

    

if __name__ == "__main__":
    main()