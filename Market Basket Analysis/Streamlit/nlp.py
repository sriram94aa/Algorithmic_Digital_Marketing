import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

#count_vec_matrix = pickle.load(open("count_vec_matrix.p", "rb"))
product_desc = pickle.load(open("product_meta.p", "rb"))

def metadata_search_engine(product_input):

    count_vec = CountVectorizer(stop_words='english')
    count_vec_matrix = count_vec.fit_transform(product_desc['metadata'])
    vec = count_vec.transform(pd.Series(product_input))
    cosine_sim = cosine_similarity(vec, count_vec_matrix)
    similarity_score = pd.DataFrame(cosine_sim.reshape(49688,), index = product_desc.index, columns=['score'])
    non_zero_scores = similarity_score[similarity_score['score'] > 0]

    if len(non_zero_scores) == 0:
        print('No similar products found.  Please refine your search terms and try again')
        return

    if len(non_zero_scores) < 10:
        item_count = len(non_zero_scores)
    else:
        item_count = 5

    similarity_scores = similarity_score.sort_values(['score'], ascending=False)[:item_count]

    return product_desc['product_name'].iloc[similarity_scores.index]


