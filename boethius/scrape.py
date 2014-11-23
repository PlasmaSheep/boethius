"""Scrape every page for models.
"""

#from . import models
import models
import yaml
import pdb
import urllib
from bs4 import BeautifulSoup

def scrape(url):
    """Scrape the given url for classes.
    """
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page)

    group = soup.find_all("tr", class_="SAHeaderYellowBar")[0].get_text().strip()
    print "Found group: " + group

    subgroup = soup.find_all("tr", class_="SAHeaderGreenBar")[0].get_text().strip()
    print " Found subgroup: " + subgroup

    classes = soup.find_all("tr", class_="SAHeaderDarkGreenBar")

    for class_element in classes:
        print "  Found class: " + class_element.get_text().strip()

def main():
    with open("config.yaml") as f:
        config = yaml.load(f)

    #pdb.set_trace()
    for source in config["sources"]:
        scrape(source)

if __name__ == "__main__":
    main()

