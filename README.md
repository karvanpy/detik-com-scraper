# DETIK-NEWS-SCRAPER

Scraping website detik.com by keyword and total pages using Python and scrapy framework.

This project still on progress to make it available for web (but, works fine in CLI)

## How to run
Clone this repo.
```
git clone https://github.com/karvanpy/detik-com-scraper
```

Access the dir
```
cd detik-com-scraper/detikcom
```

Crawl
```
scrapy crawl by_keyword -a keyword="pemerintah" -a pages=10
```
*You can edit value of **keyword** and **pages** parameter.*

## Export to CSV
The command same as before, just need to add "-O filename.csv" at the end.
```
scrapy crawl by_keyword -a keyword="pemerintah" -a pages=10 -O result.csv
```
