from sentence_transformers import SentenceTransformer, util


# Find any absolute matches between query and specification name
def find_absolute_match(query, specification_dict):
    for word in query.split():
        if word in specification_dict.keys():
            return word


# Find the most similar word between query and specification name
def get_most_similar_word(sentence, specification_dict):
    word_list = list(specification_dict.keys())

    # Load pre-trained sentence embedding model
    model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

    # Encode the sentence and word list
    sentence_embedding = model.encode(sentence, convert_to_tensor=True)
    word_embeddings = model.encode(word_list, convert_to_tensor=True)

    # Calculate cosine similarity scores
    similarity_scores = util.pytorch_cos_sim(sentence_embedding, word_embeddings)[0].tolist()

    most_similar_index = similarity_scores.index(max(similarity_scores))

    # Get the most similar word
    most_similar_word = word_list[most_similar_index]

    # Return the most similar word and its similarity score
    return [most_similar_word, max(similarity_scores)]


def main(query, specification_dict):
    # To support absolute matching
    query = query.lower()

    absolute_match = find_absolute_match(query, specification_dict)

    if absolute_match:
        # Disregard similarity matching
        match = absolute_match

    else:
        result_list = get_most_similar_word(query, specification_dict)

        most_similar_word = result_list[0]
        max_similarity = result_list[1]

        if max_similarity > 0.5:
            match = most_similar_word

        else:
            match = "0"

    if match != "0":
        # Prepare for returning
        specification_name = match
        specification_detail = specification_dict[match]

    else:
        # For use in displaying "no match found" in label
        specification_name = "0"
        specification_detail = "0"

    return [specification_name, specification_detail]
