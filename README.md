

# Mike Create Application for MN-furniture and Web-Scraper

Python 3.8 in Program for create Guibill with python
```
pip install virtualenv
pip install virtualwrapper
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
```markdown
Python Program_python\Guibill\Guibill_run.py
Python Program_python\Addwatermark\AddPaid.py


Python 3.8 in Image-Scraper

```
cd Program_python\Image-scraper
chmod +x run.sh
./run.sh
```
## Fields

The scraper will extract the following fields

-   Product Name
-   Price Range
-   Product Image
-   Link to Product
-   Minimum Order
-   Seller Name
-   Seller Response Rate
-   Number of years as a seller on Alibaba

## Requirements

-   Python 3
-   Scrapy
-   Selectorlib

## Running the Scraper

1.  Add search keyword to [keywords.csv](https://github.com/pection/MNfurniture/tree/master/Program_python/Image-scraper/scrapy_image/resources/keywords.csv)
2.  Modify max_pages variable from [alibaba_crawler.py](Image-scraper/spiders/alibaba_crawler.py), to the maximum number of pages to scrape data from. The default is 5 pages.
3.  Run command `scrapy crawl alibaba_crawler -o out.csv -t csv` to get data as CSV into a file called out.csv or `scrapy crawl alibaba_crawler -o out.json -t json` to get data as JSON File.

## Learn more about the scraper

You can read more on how this scraper was built here <https://www.scrapehero.com/scrape-alibaba-using-scrapy/>

```
Python 3.8 , Django2.0 in mn_ecommerce

```
cd mn_ecommerce
pip install -r requierment.txt
```

```markdown
pip install django
pip install virtualenv
pip install virtualwrapper
virtualenv env
soruce /env/bin/activate
```

This repositories just example for more details ask [Mike](https://wwww.facebook.com/pections).
