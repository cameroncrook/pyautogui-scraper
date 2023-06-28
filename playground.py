from lib.html_snippets.profile import chases_profile
from scraping.LI_scraping import *
from scraping.scraper_tools  import *
import json

def main():
    profile_data = get_profile_data(chases_profile)

    print(json.dumps(profile_data, indent=4))

    

if __name__ == "__main__":
    main()