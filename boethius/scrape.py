"""Scrape every page for models.
"""

#from . import models
import models
import yaml
import pdb

def main():
    with open("config.yaml") as f:
        config = yaml.load(f)

    #pdb.set_trace()
    for source in config["sources"]:
        print source

if __name__ == "__main__":
    main()

