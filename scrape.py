import requests
from bs4 import BeautifulSoup

def extract_information(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract product name
        name = soup.find(class_='B_NuCI').text

        # Extract product price
        current_price = soup.find(class_='_30jeq3 _16Jk6d').text

        # Extract product original price
        original_price = soup.find(class_='_3I9_wc _2p6lqe').text

        # Extract product discount
        discount = soup.find(class_='_3Ay6Sb _31Dcoz').text

        # Extract product rating
        rating = soup.find(class_='_3LWZlK').text

        # Extract product rating count
        rating_count = soup.find(class_='row _2afbiS').text[:-1]

        # Extract product review count
        review_count = soup.find_all(class_='row _2afbiS')[1].text


        # Extract specification type
        specification_name = soup.find_all(class_='_1hKmbr')

        # Extract specificaion detail
        specification_detail = soup.find_all(class_='_21lJbe')
        
        # Store the extracted information in a dictionary
        detail_dict = {}

        detail_dict['Name'] = name
        detail_dict['Current_price'] = current_price
        detail_dict['Original_price'] = original_price
        detail_dict['Discount'] = discount
        detail_dict['Rating'] = rating
        detail_dict['Rating_count'] = rating_count
        detail_dict['Review_count'] = review_count

                
        # Add each specification to the dictionary        
        for i in range(len(specification_name)):
            key = specification_name[i].text
            value = specification_detail[i].text
            detail_dict[key] = value
        
        return detail_dict
        

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

url_to_scrape = ''
specifications = extract_information(url_to_scrape)
