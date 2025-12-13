import requests
from typing import List, Optional
import argparse


class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        city: str,
        state: str,
        country: str,
        website_url: Optional[str],
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.state = state
        self.country = country
        self.website_url = website_url

    def __str__(self) -> str:
        return (f"{self.name} ({self.brewery_type}) "
                f"- {self.city}, {self.state}, {self.country}"
                f" Website: {self.website_url}")


def fetch_breweries(
    per_page: int = 20, city: Optional[str] = None
) -> List[Brewery]:
    url = f"https://api.openbrewerydb.org/v1/breweries?per_page={per_page}"
    if city:
        url += f"&by_city={city}"
    try:
        response = requests.get(url, headers={"User-Agent": "python-requests"})
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        data = []

    breweries = [
        Brewery(
            id=b["id"],
            name=b["name"],
            brewery_type=b.get("brewery_type", ""),
            city=b.get("city", ""),
            state=b.get("state", ""),
            country=b.get("country", ""),
            website_url=b.get("website_url"),
        )
        for b in data
    ]
    return breweries


# Command-line argument parsing
parser = argparse.ArgumentParser(description="Fetch breweries")
parser.add_argument("--city", type=str, help="Filter breweries by city")
args = parser.parse_args()

breweries = fetch_breweries(city=args.city)
for brewery in breweries:
    print(brewery)
