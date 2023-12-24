from sentence_transformers import SentenceTransformer, util

def find_absolute_match(query, specification_list):
    for word in query.split():
        if word in specification_dict.keys():
            return word
        

def get_most_similar_word(sentence, word_list):
    
    word_list = list(specification_dict.keys())
    
    # Load a pre-trained sentence embedding model
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    # Encode the sentence and word list
    sentence_embedding = model.encode(sentence, convert_to_tensor=True)
    word_embeddings = model.encode(word_list, convert_to_tensor=True)

    # Calculate cosine similarity scores
    similarity_scores = util.pytorch_cos_sim(sentence_embedding, word_embeddings)[0].tolist()

    # Get the index of the word with the highest similarity score
    most_similar_index = similarity_scores.index(max(similarity_scores))
    
    most_similar_word = word_list[most_similar_index]
    
    return [most_similar_word, max(similarity_scores)]

if __name__ == "__main__":

    query = "What is the cost?"
    query = query.lower()   
    
    specification_dict = {'name': 'SAMSUNG Galaxy F14 5G (OMG Black, 128 GB)\xa0\xa0(6 GB RAM)', 'price': '₹13,490', 'original price': '₹18,490', 'discount': '27% off', 'seller': 'MYTHANGLORYRetail4.8', 'rating': '4.2', 'rating count': '77,490 Ratings', 'review count': '5,527 Reviews', 'in the box': 'handset, type-c data cable, quick start guide, sim ejection pin', 'model number': 'sm-e146bzkhins', 'model name': 'galaxy f14 5g', 'color': 'omg black', 'browse type': 'smartphones', 'sim type': 'dual sim', 'hybrid sim slot': 'no', 'touchscreen': 'yes', 'otg compatible': 'yes', 'display size': '16.76 cm (6.6 inch)', 'resolution': '2408 x 1080 pixels', 'resolution type': 'full hd+', 'gpu': 'arm mali g68 mp2', 'display type': 'full hd+ lcd display', 'hd game support': 'yes', 'display colors': '16 million', 'other display features': 'in-cell touch display', 'operating system': 'android 13', 'processor brand': 'exynos', 'processor type': 'exynos 1330, octa core', 'processor core': 'octa core', 'primary clock speed': '2.4 ghz', 'secondary clock speed': '2 ghz', 'operating frequency': '2g gsm: gsm850/gsm900/dcs1800/pcs1900, 3g umts(wcdma): b1(2100)/b2(1900)/b4(aws)/b5(850)/b8(900), 4g lte fdd: b1(2100)/b2(1900)/b3(1800)/b4(aws)/b5(850)/b7(2600)/b8(900)/b12(700)/b17(700)/b20(800)/b26(850)/b28(700)/b66(aws-3), 5g: n1(2100)/n3(1800)/n5(850)/n7(2600)/n8(900)/n20(800)/n28(700)/n66(aws-3)', 'internal storage': '128 gb', 'ram': '6 gb', 'expandable storage': '1 tb', 'supported memory card type': 'microsd', 'memory card slot type': 'dedicated slot', 'primary camera available': 'yes', 'primary camera': '50mp + 2mp', 'primary camera features': 'dual camera setup: 50mp main camera + 2mp camera, camera features: deco pic, food, macro, panorama, photo, portrait, pro, video', 'optical zoom': 'yes', 'secondary camera available': 'yes', 'secondary camera': '13mp front camera', 'secondary camera features': '13mp front camera setup: camera features: fixed focus', 'flash': 'back flash', 'hd recording': 'yes', 'full hd recording': 'yes', 'video recording': 'yes', 'video recording resolution': 'fhd (1920 x 1080)', 'digital zoom': '10x', 'frame rate': '30 fps', 'image editor': 'yes', 'dual camera lens': 'primary camera', 'call wait/hold': 'yes', 'conference call': 'yes', 'hands free': 'yes', 'video call support': 'yes', 'call divert': 'yes', 'phone book': 'yes', 'call timer': 'yes', 'speaker phone': 'yes', 'speed dialing': 'yes', 'call records': 'yes', 'logs': 'yes', 'network type': '2g, 3g, 4g, 5g', 'supported networks': '4g lte, 5g, gsm, wcdma', 'internet connectivity': '5g, 4g, 3g, 2g', '3g': 'yes', '3g speed': '5.76 mbps', 'micro usb port': 'no', 'mini usb port': 'no', 'bluetooth support': 'yes', 'bluetooth version': 'v5.2', 'wi-fi': 'yes', 'wi-fi version': '802.11', 'wi-fi hotspot': 'yes', 'mini hdmi port': 'no', 'nfc': 'no', 'usb tethering': 'yes', 'usb connectivity': 'yes', 'audio jack': '3.5mm', 'map support': 'google maps', 'gps support': 'yes', 'smartphone': 'yes', 'touchscreen type': 'full touch capacitance', 'sim size': 'nano sim', 'social networking phone': 'yes', 'instant message': 'yes', 'business phone': 'no', 'removable battery': 'no', 'mms': 'yes', 'sms': 'yes', 'keypad': 'no', 'voice input': 'yes', 'graphics ppi': '401 ppi', 'predictive text input': 'yes', 'sim access': 'dual/single', 'sensors': 'accelerometer, fingerprint sensor, gyro sensor, geomagnetic sensor, light sensor, proximity sensor', 'upgradable operating system': '2 times android updates and 4 years of security updates', 'series': 'samsung galaxy f14 5g series', 'browser': 'google chrome | samsung s-browser 18.0', 'ringtones format': 'mp3, m4a, 3ga, aac', 'fm radio': 'yes', 'fm radio recording': 'yes', 'dlna support': 'no', 'audio formats': 'mp3, m4a, 3ga, aac', 'music player': 'yes', 'video formats': 'mp4, m4v, 3gp', 'battery capacity': '6000 mah', 'battery type': 'lithium ion', 'dual battery': 'no', 'width': '77.2 mm', 'height': '166.8 mm', 'depth': '9.4 mm', 'weight': '205 g', 'warranty summary': '1 year manufacturer warranty for device and 6 months manufacturer warranty for in-box accessories', 'not covered in warranty': 'manufacturing defect'}
    
    absolute_match = find_absolute_match(query, specification_dict)
    
    if absolute_match:
        match = absolute_match
    
    else:
        result_list = get_most_similar_word(query, specification_dict)
        print(result_list)    
        most_similar_word = result_list[0]
        max_similarity = result_list[1]

        if max_similarity > 0.5:        
            match = most_similar_word

        else:
            match = "Can't find a match"

    print(match)
    print(specification_dict.get(match))
