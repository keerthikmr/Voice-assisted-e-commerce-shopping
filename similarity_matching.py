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


def main(query, specification_dict):

    query = query.lower()   
    
    absolute_match = find_absolute_match(query, specification_dict)
    
    if absolute_match:
        match = absolute_match
    
    else:
        result_list = get_most_similar_word(query, specification_dict)
          
        most_similar_word = result_list[0]
        max_similarity = result_list[1]

        if max_similarity > 0.5:        
            match = most_similar_word

        else:
            match = '0'
    
    if match != '0':
        specification_name = match
        specification_detail = specification_dict[match]
    
    else:
        specification_name = '0'
        specification_detail = '0'

    return [specification_name, specification_detail]