from typing import List, Optional
import requests
import argparse

URL_API = "https://api.openbrewerydb.org/v1/breweries"


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
        return (f"{self.name} ({self.brewery_type}) - "
                f"{self.city}, {self.state},"
                f" {self.country} Website: {self.website_url}")


def get_breweries_from_api(city: Optional[str] = None) -> list:
    if city:
        response = requests.get(f"{URL_API}?by_city={city}")
    else:
        response = requests.get(URL_API)
    response.raise_for_status()
    return response.json()


def brewery_factory(breweries: list) -> List[Brewery]:
    brewery_objects = []
    for b in breweries:
        brewery_objects.append(
            Brewery(
                id=b.get("id", ""),
                name=b.get("name", ""),
                brewery_type=b.get("brewery_type", ""),
                city=b.get("city", ""),
                state=b.get("state", ""),
                country=b.get("country", ""),
                website_url=b.get("website_url"),
            )
        )
    return brewery_objects


def get_args():
    parser = argparse.ArgumentParser(description="Fetch breweries from API")
    parser.add_argument(
        "-c", "--city", help="Filter breweries by city", required=False
    )
    return vars(parser.parse_args())


def main():
    args = get_args()
    breweries_json = get_breweries_from_api(city=args["city"])
    breweries = brewery_factory(breweries_json)

    for brewery in breweries:
        print(brewery)
    print(f"Total breweries fetched: {len(breweries)}")


if __name__ == "__main__":
    main()
