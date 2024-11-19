import requests
from bs4 import BeautifulSoup
from PIL import Image as PILImage
from io import BytesIO
# URL of the webpage to scrape
url = "https://webscraper.io/test-sites/e-commerce/allinone"
base_url = "https://webscraper.io"

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all titles (adjust the tag and class as needed)
    titles = soup.find_all(class_="product-wrapper")  # Example: change based on the website
    
    print("product content:")
    for i, product in enumerate(titles, 1):
        print(f"{i}. {product.get_text(strip=True)}")
        img_tag = product.find("img")
        print(f"image tag is=====>{img_tag.get('src')}")
        full_img_url = base_url + img_tag.get('src') if img_tag.get('src').startswith("/") else img_tag.get('src')

        img_response = requests.get(full_img_url)
        if img_response.status_code == 200:
                # Open the image using Pillow
                img = PILImage.open(BytesIO(img_response.content))
                img.show(title=f"Product {i}")
       
        
        print(f"Product {i}:")
        
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
