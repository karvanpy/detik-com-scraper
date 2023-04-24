import scrapy


class ByKeywordSpider(scrapy.Spider):
    name = 'by_keyword'
    allowed_domains = ['detik.com']
    # start_urls = ['http://detik.com/']

    def __init__(self, keyword=None, pages=1):
        self.keyword = keyword
        self.pages = pages

    def start_requests(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'http://www.detik.com'
        }

        for i in range(1, int(self.pages)+1):
            yield scrapy.Request(
                f"https://www.detik.com/search/searchall?query={self.keyword}&page={i}",
                headers=self.headers,
            )

    def parse(self, response):
        articles = response.css("article")

        for article in articles:
            url = article.css("a::attr(href)").extract_first()
            yield scrapy.Request(
                url,
                headers=self.headers,
                callback=self.parse_article,
                meta={
                    'title': article.css("h2.title::text").extract_first(),
                    'description': article.css("span.box_text > p::text").extract_first(),
                    'date': article.css("span.date:not(:has(span.category))::text").extract_first(),
                    'url': url})

    def parse_article(self, response):
        yield {
            "title": response.meta.get('title'),
            "description": response.meta.get('description'),
            "date": response.meta.get('date'),
            "url": response.meta.get('url'),
            "content": " ".join(response.css("div.detail__body-text > p::text").extract())
        }
