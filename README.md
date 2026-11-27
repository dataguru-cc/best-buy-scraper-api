# Best Buy Scraper API

Scrape Best Buy with a JSON API. This repo has working Python examples for DataGuru's Best Buy scraper API: Best Buy Product Details.

[DataGuru](https://dataguru.cc) runs the scraping, proxies, retries and parsing, and returns clean JSON. You pay only for successful requests, from $0.02 per request, out of a prepaid balance: no subscription. New accounts get $1.00 of free credit.

## Best Buy APIs

| API | What it returns | Price | Page |
| --- | --- | --- | --- |
| [Best Buy Product Details](#best-buy-product-details) | Get product details from a BestBuy.com product URL, including price, ratings, specifications, images and availability. | $0.02 | [https://dataguru.cc/apis/bestbuy-product-details/](https://dataguru.cc/apis/bestbuy-product-details/) |

## Quick start

1. Create a free account and an API key at [dashboard.dataguru.cc](https://dashboard.dataguru.cc).
2. Install and run:

```bash
git clone https://github.com/dataguru-cc/best-buy-scraper-api.git
cd best-buy-scraper-api
pip install -r requirements.txt
export DATAGURU_API_KEY="your key"
python examples/sdk_example.py bestbuy-product-details
```

## Examples

Every example covers all 1 Best Buy API. Pass an API name to run just one; with no name each script runs them all, and each call is billed at the price above.

| File | Style | Run |
| --- | --- | --- |
| [`examples/sdk_example.py`](examples/sdk_example.py) | [DataGuru Python SDK](https://github.com/dataguru-cc/dataguru-python) (`pip install dataguru-sdk`), one function per API, saves JSON to `output/` | `python examples/sdk_example.py` |
| [`examples/requests_example.py`](examples/requests_example.py) | Plain `requests`, synchronous | `python examples/requests_example.py` |
| [`examples/async_example.py`](examples/async_example.py) | `asyncio` + `httpx`, concurrent with a limit | `python examples/async_example.py` |
| [`examples/scrapy_spider.py`](examples/scrapy_spider.py) | Scrapy spider, items to JSON/CSV | `scrapy runspider examples/scrapy_spider.py -O best-buy.json` |

All requests use the header `Authorization: Api-Key YOUR_API_KEY`. Errors return `{"success": false, "error": {"code", "message", "request_id"}}`, with HTTP 402 when the balance runs out and 429 (with `Retry-After`) when rate limited. Failed requests are not charged.

## API reference

### Best Buy Product Details

Get product details from a BestBuy.com product URL, including price, ratings, specifications, images and availability.

- Endpoint: `POST https://api.dataguru.cc/api/v1/bestbuy/products/details`
- Price: $0.02 per successful request ($20.00 per 1,000)
- Rate limit: 60 requests/minute
- Page and live playground: https://dataguru.cc/apis/bestbuy-product-details/
- Documentation: https://dataguru.cc/documentation/bestbuy-product-details/

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `location` | string | no | Two-letter country code (default US). |
| `product_url` | string | yes | Full Best Buy product URL (e.g. https://www.bestbuy.com/site/hp-14-laptop.../6667483.p?skuId=6667483). |

**Response fields:** `sku`, `title`, `brand`, `model_number`, `upc`, `url`, `categories`, `price`, `rating`, `qa_stats`, `availability`, `description`, `bullet_descriptions`, `specifications`, `specifications_detailed`, `images`, `variants`, `badges`, `seller`, `return_policy_url`, plus `_metadata`

```bash
curl -X POST "https://api.dataguru.cc/api/v1/bestbuy/products/details" \
  -H "Authorization: Api-Key $DATAGURU_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_url": "https://www.bestbuy.com/product/apple-airpods-4-white/JJGCQ83JQ5"}'
```

<details><summary>Response schema</summary>

Values are type placeholders from the API's published schema, not real data.

```json
{
  "sku": "string",
  "title": "string",
  "brand": "string",
  "model_number": "string",
  "upc": "string",
  "url": "https://example.com/...",
  "categories": [
    "string"
  ],
  "price": {
    "current_price": 0.0,
    "regular_price": 0.0,
    "savings": 0.0,
    "savings_percentage": 0.0,
    "currency": "USD",
    "open_box_options": [
      {
        "condition": "string",
        "price": 0.0,
        "pdp_url": "https://example.com/...",
        "availability": "string"
      }
    ]
  },
  "rating": {
    "average_rating": 0.0,
    "review_count": 0,
    "review_summary": "string"
  },
  "qa_stats": {
    "answered_questions": 0
  },
  "availability": {
    "in_stock": false,
    "status": "string"
  },
  "description": "string",
  "bullet_descriptions": [
    "string"
  ],
  "specifications": {},
  "specifications_detailed": [
    {
      "category": "string",
      "name": "string",
      "value": "string",
      "definition": "string"
    }
  ],
  "images": [
    "string"
  ],
  "variants": [
    {
      "bsin": "string",
      "sku": "string",
      "options": [
        {
          "name": "string",
          "value": "string"
        }
      ]
    }
  ],
  "badges": [
    "string"
  ],
  "seller": {
    "name": "Best Buy",
    "type": "1P"
  },
  "return_policy_url": "https://example.com/...",
  "_metadata": {
    "request_id": "3f6c1a2e-8b4d-4c1e-9a7f-2d5e6b7c8d9e",
    "execution_time_ms": 842,
    "endpoint": "Best Buy Product Details",
    "mode": "live",
    "format": "json",
    "timestamp": "2026-01-01T12:00:00+00:00"
  }
}
```

</details>

## More

- Python SDK and examples for all DataGuru APIs: [github.com/dataguru-cc/dataguru-python](https://github.com/dataguru-cc/dataguru-python) ([docs](https://dataguru-python.readthedocs.io/))
- Every API, with a live playground: [https://dataguru.cc/apis/](https://dataguru.cc/apis/)
- Use DataGuru from Claude, ChatGPT or Cursor through the MCP server: [https://dataguru.cc/mcp/](https://dataguru.cc/mcp/)
- Run thousands of inputs from a CSV at half price with batch jobs: [https://dataguru.cc/documentation/](https://dataguru.cc/documentation/)
- Other scraper APIs: [1688](https://github.com/dataguru-cc/1688-scraper-api), [Airbnb](https://github.com/dataguru-cc/airbnb-scraper-api), [Alibaba](https://github.com/dataguru-cc/alibaba-scraper-api), [AliExpress](https://github.com/dataguru-cc/aliexpress-scraper-api), [Amazon](https://github.com/dataguru-cc/amazon-scraper-api), [arXiv](https://github.com/dataguru-cc/arxiv-scraper-api), [ASOS](https://github.com/dataguru-cc/asos-scraper-api), [Booking.com](https://github.com/dataguru-cc/booking-scraper-api), [Brave Search](https://github.com/dataguru-cc/brave-search-scraper-api), [CA State Bar](https://github.com/dataguru-cc/california-state-bar-scraper-api), [Capterra](https://github.com/dataguru-cc/capterra-scraper-api), [CoinGecko](https://github.com/dataguru-cc/coingecko-scraper-api), [CoinMarketCap](https://github.com/dataguru-cc/coinmarketcap-scraper-api), [Companies House](https://github.com/dataguru-cc/companies-house-scraper-api), [Costco](https://github.com/dataguru-cc/costco-scraper-api), [CourtListener](https://github.com/dataguru-cc/courtlistener-scraper-api), [Crunchbase](https://github.com/dataguru-cc/crunchbase-scraper-api), [Discord](https://github.com/dataguru-cc/discord-scraper-api), [DoorDash](https://github.com/dataguru-cc/doordash-scraper-api), [eBay](https://github.com/dataguru-cc/ebay-scraper-api), [Etsy](https://github.com/dataguru-cc/etsy-scraper-api), [Expedia](https://github.com/dataguru-cc/expedia-scraper-api), [Fiverr](https://github.com/dataguru-cc/fiverr-scraper-api), [Flipkart](https://github.com/dataguru-cc/flipkart-scraper-api), [Glassdoor](https://github.com/dataguru-cc/glassdoor-scraper-api), [Google Flights](https://github.com/dataguru-cc/google-flights-scraper-api), [Google Patents](https://github.com/dataguru-cc/google-patents-scraper-api), [Google Scholar](https://github.com/dataguru-cc/google-scholar-scraper-api), [Google Search](https://github.com/dataguru-cc/google-search-scraper-api), [Grubhub](https://github.com/dataguru-cc/grubhub-scraper-api), [Home Depot](https://github.com/dataguru-cc/home-depot-scraper-api), [Instagram](https://github.com/dataguru-cc/instagram-scraper-api), [Investing.com](https://github.com/dataguru-cc/investing-com-scraper-api), [Justia](https://github.com/dataguru-cc/justia-scraper-api), [Kayak](https://github.com/dataguru-cc/kayak-scraper-api), [Kick](https://github.com/dataguru-cc/kick-scraper-api), [Lazada](https://github.com/dataguru-cc/lazada-scraper-api), [MarketWatch](https://github.com/dataguru-cc/marketwatch-scraper-api), [Mercado Libre](https://github.com/dataguru-cc/mercado-libre-scraper-api), [Monster](https://github.com/dataguru-cc/monster-scraper-api), [OpenCorporates](https://github.com/dataguru-cc/opencorporates-scraper-api), [OpenTable](https://github.com/dataguru-cc/opentable-scraper-api), [PACER](https://github.com/dataguru-cc/pacer-scraper-api), [PitchBook](https://github.com/dataguru-cc/pitchbook-scraper-api), [PubMed](https://github.com/dataguru-cc/pubmed-scraper-api), [Reddit](https://github.com/dataguru-cc/reddit-scraper-api), [Redfin](https://github.com/dataguru-cc/redfin-scraper-api), [Resy](https://github.com/dataguru-cc/resy-scraper-api), [Rightmove](https://github.com/dataguru-cc/rightmove-scraper-api), [SEC EDGAR](https://github.com/dataguru-cc/sec-edgar-scraper-api), [Seeking Alpha](https://github.com/dataguru-cc/seeking-alpha-scraper-api), [Shopee](https://github.com/dataguru-cc/shopee-scraper-api), [Skyscanner](https://github.com/dataguru-cc/skyscanner-scraper-api), [Target](https://github.com/dataguru-cc/target-scraper-api), [TikTok](https://github.com/dataguru-cc/tiktok-scraper-api), [TradingView](https://github.com/dataguru-cc/tradingview-scraper-api), [TripAdvisor](https://github.com/dataguru-cc/tripadvisor-scraper-api), [Trulia](https://github.com/dataguru-cc/trulia-scraper-api), [TrustRadius](https://github.com/dataguru-cc/trustradius-scraper-api), [Twitch](https://github.com/dataguru-cc/twitch-scraper-api), [Uber Eats](https://github.com/dataguru-cc/uber-eats-scraper-api), [Upwork](https://github.com/dataguru-cc/upwork-scraper-api), [Vrbo](https://github.com/dataguru-cc/vrbo-scraper-api), [Walmart](https://github.com/dataguru-cc/walmart-scraper-api), [Wayfair](https://github.com/dataguru-cc/wayfair-scraper-api), [X (Twitter)](https://github.com/dataguru-cc/twitter-scraper-api), [Yahoo Finance](https://github.com/dataguru-cc/yahoo-finance-scraper-api), [YouTube](https://github.com/dataguru-cc/youtube-scraper-api), [Zillow](https://github.com/dataguru-cc/zillow-scraper-api), [ZoomInfo](https://github.com/dataguru-cc/zoominfo-scraper-api), [Zoopla](https://github.com/dataguru-cc/zoopla-scraper-api)

## License

The example code is MIT licensed. Use of the DataGuru API is subject to the [terms of service](https://dataguru.cc/terms/).
