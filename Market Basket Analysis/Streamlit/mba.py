import pickle
import pandas as pd
group_association_rules_dic = pickle.load(open("grouped_association_rules_dic.p", "rb"))
products = pd.read_csv("products.csv")
clustered_users = pickle.load(open("clustered_users.p", "rb"))


def product_to_product(cluster, product_id, item_lift, product_name, num_products):
    df = group_association_rules_dic[cluster]
    df = df[(df['item_A'] == product_id) | (df['item_B'] == product_id)][['product_name_A', 'item_A', 'product_name_B',
                                                                          'item_B', 'confAtoB', 'lift']].sort_values('lift', ascending=False)
    df = df[df['lift'] > item_lift]
    df = df.sort_values('lift', ascending=False)
    df = df.head(n=num_products)
    product_to_product_associations = df['product_name_A'].values.tolist()
    for x in df['product_name_B'].values.tolist():
        product_to_product_associations.append(x)
    product_to_product_associations = [x for x in product_to_product_associations if x != product_name]
    return product_to_product_associations


def product_recommender(user_id, product_name, item_lift, num_products):
    product_id = products.index[products['product_name'] == product_name].tolist()[0] + 1
    cluster = clustered_users.at[user_id, 'cluster']
    return product_to_product(cluster=cluster, product_id=product_id, item_lift=item_lift,
                              product_name=product_name, num_products=num_products)


#print(product_recommender(134922, "Mild Salsa Roja", 1, 5))