# Instacart Market Basket Analysis

  

## About Instacart

-   An American based company that delivers grocery items to customers on the same day.
    
-   The Goal of this company is to be an efficient real-time logistics platform of moving goods from the store to the customer place as efficiently and predictably as possible
    
-   Product recommendation plays a crucial role.
    

  

![](https://lh4.googleusercontent.com/-RGWaOYNgzvqxZUklVJD9HLTX9SHQ3xXuhQZPlA9uu8psgIBbv4bxWALa2ORDAqH8ASfHQLEAYYtyLGrOgBxnoGpkrlhv6srvVKQQlO6tmx8Lkdtm8Zt-3Bhq4xvEZCpmc7Qczpm)

  

## Aim of the Project

-   Analyze grocery purchasing data and group customers who have similar buying habits together.
    
-   Provide product suggestions based on keyword searches, as well as additional cart products.
    

## Dataset Description

The dataset is anonymized and contains a sample of over 3 million grocery orders from more than 200,000 Instacart users.

### aisles.csv

```
 aisle_id,aisle  
 1,prepared soups salads  
 2,specialty cheeses  
 3,energy granola bars  
 ...

```

### departments.csv

```
 department_id,department  
 1,frozen  
 2,other  
 3,bakery  
 ...

```

### order_products__*.csv

These files specify which products were purchased in each order. order_products__prior.csv contains previous order contents for all customers. 'reordered' indicates that the customer has a previous order that contains the product. Note that some orders will have no reordered items. You may predict an explicit 'None' value for orders with no reordered items. See the evaluation page for full details.

```
 order_id,product_id,add_to_cart_order,reordered  
 1,49302,1,1  
 1,11109,2,1  
 1,10246,3,0  
 ... 

```

### orders.csv

This file tells to which set (prior, train, test) an order belongs. You are predicting reordered items only for the test set orders. 'order_dow' is the day of week.

```
 order_id,user_id,eval_set,order_number,order_dow,order_hour_of_day,days_since_prior_order  
 2539329,1,prior,1,2,08,  
 2398795,1,prior,2,3,07,15.0  
 473747,1,prior,3,3,12,21.0  
 ...

```

### products.csv

```
 product_id,product_name,aisle_id,department_id
 1,Chocolate Sandwich Cookies,61,19  
 2,All-Seasons Salt,104,13  
 3,Robust Golden Unsweetened Oolong Tea,94,7  
 ...

```

### sample_submission.csv

```
order_id,products
17,39276  
34,39276  
137,39276  
...
```

  
  

## Staging the Data

  

![](https://lh5.googleusercontent.com/x_PRJX4Mgp27WTdm9RlX4u88wovBbsn5MiPeAvEERzFk72hGCo90-AR_IBNbG3hRJxZIev5snhUVLBimhcTbzbZsreOWVScklbKuwenGXMkMTse7ALFaMqwRpXUU8s4WHU1K0BGo)

  

![](https://lh3.googleusercontent.com/b12Hc8IXbTvrTkZau8lb2tkQKEaNhaJkDdCfpOI_hCGoDJiWNWCwo2UahM-xGfnydCjxVVl6FX-QdptdG9zA8HiWx81R5Mo-LPBNcC1oMhs0i6G_0OvAYNIb2ZPy4BkhnHu8F_ri)

## RFM Analysis

### What is RFM Analysis?

RFM (Recency, Frequency,Monetary Value) Analysis measures how recently, how often, and how much money a customer has given your brand.

  

![](https://lh3.googleusercontent.com/RD3KTiToa2jtjSSwtgv-wsl89s5AW1A6p0HMGhrazlPwab1hqZ6DQguH86otkMpZkqwsKVEdwvT7gbtywwUF8mCPXcgsmHCz7bjTss_uPFhZtl4y29Z1tC8tdhCFABJb_jaFygIr)

  

### How does RFM help?

RFM analysis helps marketers answer:

• Who are their best customers?

• Which of their customers could contribute to churn rate?

• Who has the potential to become valuable customers?

  
  

## Customer Segmentation

  

![](https://lh6.googleusercontent.com/8zY-uDs4R3-J1TqTxljoxWQjaYAbvMWrw_2thc9cJsdjjNT7TFMZsmzLCk-lZ6y7gQbgZZmJ43a2oZApfX-zIWCO81bfzVtOdACKWrz2O-Gy3_kNJsyqggxYr2yaEoCbU5nutSve)

  

## Recommendations

### Best Customers

-   We can reward them for their multiple purchases.
    
-   We can Suggest them to "Refer a friend" and can give points or rewards for both.
    
-   They can be the early adopters to new products
    

### Lost Cheap Customers

-   We can send them personalized Emails to encourage them to order by giving some discounts
    
-   We can create campaigns by sending out feedback surveys with which we can analyze the issue
    
-   Once we identify the problem, work to correct it. Once corrected, spin it into a marketing campaign.
    

### Big Spenders

-   We can give them early access to good deals.
    
-   Award higher status
    
-   Leverage better deals
    

  
  

### Loyal Customers

-   Loyalty cards can be awarded to them and later the points that were accumulated can be converted to discounts.
    

### Potential Loyalists

-   Offer Membership or Loyalty Programs.
    
-   Recommend related products to upsell them.
    

### At Risk Customers

-   Use a new channel to reach out like social media targeted Ads.
    
-   Winback campaigns can be set up.
    

  

## NLP based Product Search

  

![](https://lh3.googleusercontent.com/sxY-TWOQqGqpI84DzrDgQdhpB8KNYEFWXywouT45rFziE_zGRyWkBGm5wWqV6Wy9NpOdqVmkgln8GW06Oa63jCNGJIKmbMAoxghTuhtKwWDS6wJ-XSKt-NUcVibFJAoxn42KUnhO)

  

![](https://lh6.googleusercontent.com/57WlMjZdrQrltGmIXfL13eO72jh11g2JGvSg5Iz7sHAfMlsogl4bLWqzUGbLDokOGg1G9c_OSifyaPYtaaES01EHxBe3d1Q7eEz5y9Q59UyhBfYM05oCgqsoJ_JjQucKAY6YHYEg)

  

-   Uses Product names, Aisle name, and department name with a count vectorizer and calculates cosine similarity to existing product base.
    
-   Works like search Engine Optimization.
    

  

## Market Basket Analysis

Association rules indicate a strong relationship between items that customers purchased in the same transaction.

  

Frequency: Probability of buying a product or pair of products

  

Support: Probability of buying X and Y products together:

![](https://lh3.googleusercontent.com/LZPPHRoAcpyMiSb64gk3WkTRPXf1eKpKmLuouzMRgZZ7cUeyWoDjb_JbuKkhrylc1Vxc3efENI0QfydyZwhzY1N9y5AD-uMutFZgFmpFX6qncfkEQrrpBuBHUjkqvms4KA45PPs-)

Confidence: This says how likely item Y is purchased when item X is purchased.

![](https://lh4.googleusercontent.com/Q6xh7JbE7WlA0aq_HkqyDGBf34IlzYDheUykbax9LfoHMQN7tqp8x-QGhLknArtUXJEQHll7lZ9F0SYboqSUQ6l128_77n2pCUlT2EZ5Pjc0YGZqg9ZK7F4t7xQ1PysTwABA0YUh)

Lift: Shows how likely item Y is purchased when item X is purchased, while controlling for how popular they are.

![](https://lh5.googleusercontent.com/imXs-ReSDTKwqjs90JKyAeyp7Ujw9uqNXINMZuYIk-X__QBaO8vgfSGX_xF0KrEJaNceLmniqyhleCIEkOIBL-ZtH5Up95Edz-SJNxNft1AIOP3_Tm1xzWnWdoI0IvvUfHNpDEE_)

  

Using association rules derived from these probabilities for each product pair ordered for each cluster, I can generate recommendations for new products based on a single product purchased or 'added to cart'.
  
## Streamlit Output
  
![Streamlit](https://user-images.githubusercontent.com/71303032/116770068-ea2cca00-aa0e-11eb-850f-47cd55971ec9.jpeg)
 
 
