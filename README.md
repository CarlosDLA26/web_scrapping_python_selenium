# Web Scrapping Python Selenium
Example of web scrapping with Python-Selenium for E-Commerce Page.

The code `web_scrapping.py` perform data extraction (product name and product price) at next E-commerce:

Image:

![](Web_scrapping/img_readme/madison_island.JPG)

* Download Chrome driver in next [link](https://chromedriver.chromium.org/) and put in main folder project.

* Change file `words_search.txt` with words that you want to search in E Commerce.

* Run code `web_scrapping.py` .
* Verify file `jsoon_files/test.json` with results of web scrapping.

## Example
### txt file
Put the products that we want to search in `words_search.txt`
```
cd
pen
tie
pants
sock
```
When run code, it will generate the next json file in `jsoon_files/test.json`:
```
{
    "cd": {
        "MP3 PLAYER WITH AUDIO": "$185.00",
        "MADISON 8GB DIGITAL MEDIA PLAYER": "$275.00"
    },
    "pen": {
        "KHAKI BOWERY CHINO PANTS": "$140.00",
        "A TALE OF TWO CITIES": "$10.00",
        "ESSEX PENCIL SKIRT": "$185.00",
        "THE ESSENTIAL BOOT CUT JEAN": "$140.00",
        "BOWERY CHINO PANTS": "$140.00"
    },
    "tie": {
        "BLACK NOLITA CAMI": "$150.00",
        "SWING TIME EARRINGS": "$75.00",
        "A TALE OF TWO CITIES": "$10.00",
        "NOLITA CAMI": "$150.00"
    },
    "pants": {
        "KHAKI BOWERY CHINO PANTS": "$140.00",
        "PARK AVENUE PLEAT FRONT TROUSERS": "$245.00",
        "FLAT FRONT TROUSER": "$195.00",
        "BOWERY CHINO PANTS": "$140.00"
    },
    "sock": {}
}
```

**IMPORTANT:** Install library Selenium for python.
