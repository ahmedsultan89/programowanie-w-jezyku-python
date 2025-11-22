
import requests
from typing import List, Optional

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

url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"
response = requests.get(url)

if response.status_code != 200:
    print(f"Error fetching data: {response.status_code}")
    print(response.text)
    data = []
else:
    data = response.json()

breweries: List[Brewery] = [
    Brewery(
        id=b["id"],
        name=b["name"],
        brewery_type=b.get("brewery_type", ""),
        city=b.get("city", ""),
        state=b.get("state", ""),
        country=b.get("country", ""),
        website_url=b.get("website_url")
    )
    for b in data
]

for brewery in breweries:
    print(brewery)
