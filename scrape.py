import requests
from bs4 import BeautifulSoup

def extract_information(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract specification type
        specification_name = soup.find_all(class_='_1hKmbr')

        # Extract specificaion detail
        specification_detail = soup.find_all(class_='_21lJbe')
        
        i=0
        
        # Add each specification to a dictionary
        specification_dict = {}
        for i in range(len(specification_name)):
            key = specification_name[i].text
            value = specification_detail[i].text
            specification_dict[key] = value
        
        return specification_dict
        

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

url_to_scrape = ''
specifications = extract_information(url_to_scrape)
