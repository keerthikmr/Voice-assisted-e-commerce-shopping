import requests
from bs4 import BeautifulSoup


def extract_information(url):
    try:
        response = requests.get(url)
    except:
        return 1

    # Check if connectino is established
    if response.status_code == 200:
        # Fetch the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Dictionary to store the product details
        detail_dict = {}

        # Extract product name
        name = soup.find(class_="B_NuCI").text
        detail_dict["name"] = name

        # Extract product price
        current_price = soup.find(class_="_30jeq3 _16Jk6d").text
        detail_dict["price"] = current_price

        # Extract product original price
        if soup.find(class_="_3I9_wc _2p6lqe") is not None:
            original_price = soup.find(class_="_3I9_wc _2p6lqe").text
            detail_dict["original price"] = original_price

        # Extract product discount
        if soup.find(class_="_3Ay6Sb _31Dcoz") is not None:
            discount = soup.find(class_="_3Ay6Sb _31Dcoz").text
            detail_dict["discount"] = discount

        # Extract seller name
        seller_name = soup.find(class_="_1RLviY").text
        detail_dict["seller"] = seller_name

        # Extract product rating
        if soup.find(class_="_3LWZlK") is not None:
            rating = soup.find(class_="_3LWZlK").text
            detail_dict["rating"] = rating

        # Extract product rating count
        if soup.find(class_="row _2afbiS") is not None:
            rating_count = soup.find(class_="row _2afbiS").text[:-2]
            detail_dict["rating count"] = rating_count

        # Extract product review count
        # Rating and review share same class. Find second element of find_all list
        try:
            review_count = soup.find_all(class_="row _2afbiS")[1].text
            detail_dict["review count"] = review_count

        # Index error if product does not have review
        except IndexError:
            review_count = 0

        # Find the table that contains the product specifications
        table = soup.find(class_="_14cfVK")

        # col-3-12 class contains the specification name
        specification_name = soup.find_all(class_="_1hKmbr col col-3-12")

        # col-9-12 class contains the specification detail
        specification_detail = soup.find_all(class_="URwL2w col col-9-12")

        # Add each specification to the dictionary
        for i in range(len(specification_name)):
            key = specification_name[i].text.lower()
            value = specification_detail[i].text.lower()
            detail_dict[key] = value

        return detail_dict

    else:
        if response.status_code == 429:
            # For use in displaying "too many requests" in selector window label
            return 2

        return 1
