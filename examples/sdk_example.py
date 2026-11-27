"""Best Buy scraper API: DataGuru Python SDK example.

Runs DataGuru's Best Buy APIs and prints the JSON they return:
  - Best Buy Product Details: $0.02 per successful request ($20.00 per 1,000)

Setup:
    pip install -r requirements.txt
    export DATAGURU_API_KEY="your key"   # free credit at https://dashboard.dataguru.cc

Run:
    python examples/sdk_example.py            # every API below
    python examples/sdk_example.py bestbuy-product-details
"""
import json
import sys
from pathlib import Path

from dataguru import DataGuru, DataGuruError

def bestbuy_product_details(dg):
    """Best Buy Product Details: Get product details from a BestBuy.com product URL, including price, ratings, specifications, images and availability."""
    return dg.call(
        "bestbuy-product-details",
        product_url="https://www.bestbuy.com/product/apple-airpods-4-white/JJGCQ83JQ5",
    )


EXAMPLES = {
    "bestbuy-product-details": bestbuy_product_details,
}
DEFAULT = ['bestbuy-product-details']


def main(names):
    out = Path("output")
    out.mkdir(exist_ok=True)
    with DataGuru() as dg:  # reads DATAGURU_API_KEY
        for name in names:
            data = EXAMPLES[name](dg)
            (out / f"{name}.json").write_text(json.dumps(data, indent=2, ensure_ascii=False))
            print(f"{name}: saved output/{name}.json")
            print(json.dumps(data, indent=2, ensure_ascii=False)[:1500])


if __name__ == "__main__":
    names = sys.argv[1:] or DEFAULT
    unknown = [n for n in names if n not in EXAMPLES]
    if unknown:
        sys.exit(f"Unknown API {unknown}. Choose from: {', '.join(EXAMPLES)}")
    try:
        main(names)
    except DataGuruError as error:
        sys.exit(f"DataGuru error: {error}")
