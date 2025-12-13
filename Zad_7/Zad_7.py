from typing import List, Optional
import requests

class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str, city: str, state: str, country: str, website_url: Optional[str]):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.state = state
        self.country = country
        self.website_url = website_url

    def __str__(self) -> str:
        return f"{self.name} ({self.brewery_type}) - {self.city}, {self.state}, {self.country} Website: {self.website_url}"

def get_breweries_from_api(per_page: int = 20) -> list:
    url = f"https://api.openbrewerydb.org/v1/breweries?per_page={per_page}"
    try:
        response = requests.get(url, headers={"User-Agent": "python-requests"})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def brewery_factory(breweries: list) -> List[Brewery]:
    return [
        Brewery(
            id=b["id"],
            name=b["name"],
            brewery_type=b.get("brewery_type", ""),
            city=b.get("city", ""),
            state=b.get("state", ""),
            country=b.get("country", ""),
            website_url=b.get("website_url")
        )
        for b in breweries
    ]

def main():
    breweries_json = get_breweries_from_api()
    breweries = brewery_factory(breweries_json)
    for brewery in breweries:
        print(brewery)

if __name__ == "__main__":
    main()
