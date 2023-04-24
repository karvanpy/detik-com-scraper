import streamlit as st
from twisted.internet import reactor
import pandas as pd
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from detikcom.spiders.by_keyword import ByKeywordSpider
    
# Streamlit app
st.title("Search Detik.com")

# User input
keyword = st.text_input("Enter keyword to search:")
pages = st.number_input("Enter number of pages:", min_value=1, max_value=100)

def notThreadSafe(x):
    """do something that isn't thread-safe"""
    pass

if st.button("search"):
    # process = CrawlerProcess(settings={
    #         'FEED_FORMAT': 'json',
    #         'FEED_URI': 'scraped_data.json'
    #     })
    # process.crawl(ByKeywordSpider, keyword=keyword, pages=pages)
    # process.start()

    runner = CrawlerRunner(settings={
            'FEED_FORMAT': 'csv',
            'FEED_URI': 'scraped_data.csv'
        })
    runner.crawl(ByKeywordSpider, keyword=keyword, pages=pages)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.callFromThread(notThreadSafe, 3)
    reactor.run() #it will run both crawlers and code inside the function

    st.success("Data scraped successfully!")
    st.json('scraped_data.csv')

data = pd.read_csv('scraped_data.csv')
data = data.loc[:, ['title', 'description', 'date', 'url']]
data.index += 1
st.table(data)
