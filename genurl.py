import argparse
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

def main():
    parser = argparse.ArgumentParser(description="Scrape URLs from a specific part of a webpage")
    parser.add_argument("url", help="Base URL to scrape")
    parser.add_argument("selector_type", choices=['class', 'id'], help="Type of selector: class or id")
    parser.add_argument("selector_value", help="Value of the class or ID to identify the DOM element")
    args = parser.parse_args()

    base_url = args.url
    if not base_url.startswith(('http://', 'https://')):
        print(f"Provided base URL does not include scheme: {base_url}")
        return

    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Failed to fetch {base_url}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Construct the selector based on the input type
    if args.selector_type == 'class':
        selector = '.' + '.'.join(args.selector_value.split())
    elif args.selector_type == 'id':
        selector = '#' + args.selector_value

    selected_element = soup.select_one(selector)
    
    if selected_element is None:
        print(f"No element found with the {args.selector_type}: {args.selector_value}")
        return

    links = selected_element.find_all('a', href=True)
    urls = [urljoin(base_url, link['href']) for link in links]

    with open('urls.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')

    print(f"URLs extracted to urls.txt")

if __name__ == "__main__":
    main()
