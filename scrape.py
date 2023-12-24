import requests
from bs4 import BeautifulSoup

def extract_information(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Dictionary to store the product details
        detail_dict = {}        

        # Extract product name
        name = soup.find(class_='B_NuCI').text
        detail_dict['Name'] = name

        # Extract product price
        current_price = soup.find(class_='_30jeq3 _16Jk6d').text
        detail_dict['Current_price'] = current_price

        # Extract product original price
        if soup.find(class_='_3I9_wc _2p6lqe') is not None:
            original_price = soup.find(class_='_3I9_wc _2p6lqe').text
            detail_dict['Original_price'] = original_price

        # Extract product discount
        if soup.find(class_='_3Ay6Sb _31Dcoz') is not None:
            discount = soup.find(class_='_3Ay6Sb _31Dcoz').text
            detail_dict['Discount'] = discount

        # Extract seller name
        seller_name = soup.find(class_='_1RLviY').text
        detail_dict['Seller_name'] = seller_name

        # Extract product rating
        if soup.find(class_='_3LWZlK') is not None:
            rating = soup.find(class_='_3LWZlK').text
            detail_dict['Rating'] = rating
        
        # Extract product rating count
        if soup.find(class_='row _2afbiS') is not None:
            rating_count = soup.find(class_='row _2afbiS').text[:-2]
            detail_dict['Rating_count'] = rating_count

        # Extract product review count
        try:
            review_count = soup.find_all(class_='row _2afbiS')[1].text
            detail_dict['Review_count'] = review_count

        except IndexError:
            review_count = 0

        # Find the table with class _14cfVK
        table = soup.find(class_='_14cfVK')

        # Find all elements of the table with class _1hKmbr
        specification_name = soup.find_all(class_='_1hKmbr col col-3-12')

        # Find all li elements of the table
        specification_detail = soup.find_all(class_='URwL2w col col-9-12')
        

        # Add each specification to the dictionary        
        for i in range(len(specification_name)):
            key = specification_name[i].text
            value = specification_detail[i].text
            detail_dict[key] = value
        
        return detail_dict
        
    else:
        if(response.status_code == 429):
            print("Too many requests. Try again later.")
        else:
            print(f"Can't connect to webpage. Status code: {response.status_code}")

url_to_scrape = ''
specifications = extract_information(url_to_scrape)
