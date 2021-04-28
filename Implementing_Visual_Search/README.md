
## Introduction

The most general term for a variety of mechanisms that share the concept of searching large spaces of objects where the only available comparator is the similarity between any two objects is known as **similarity search**. This is becoming highly prevalent in an era of vast knowledge repositories containing items with no natural order.Nearest neighbor search and range queries are important subclasses of similarity search.The most general approach to similarity search is based on the mathematical concept of metric space, which allows for the development of efficient index structures and thus search domain scalability.

Below are the 3 methods with which we implement similarity search:

1.  Artistic Style Similarity Search - Cosine Similarity
2.  Facebook Artificial Intelligence Similarity Search (FAISS)
3.  Spotify Annoy

## Artistic Style Similarity Search - Cosine Similarity:

![](https://lh4.googleusercontent.com/HvmoLK7ZiavTywAmkxaii5F5Rt5jAKS8tYhX0V3rF3lg_Q2nmXy1iTZlCnWu0BpM4Ln4tkGXUt68NGP3U00gbdTNaV0mzYsuZmovWrvXV3qEHjkULA0uFn8eu1pxG2ZcQlSI1QAj)

**Cosine similarity**  is a measure of similarity between two non-zero vectors of an inner product space. It is defined to equal the cosine of the angle between them, which is also the same as the inner product of the same vectors normalized to both have length 1.

It is a judgement of orientation.

-   Two vectors with the same orientation have a cosine similarity of 1.
-   Two vectors oriented at 90° relative to each other have a similarity of 0.
-   Two vectors diametrically opposed have a similarity of -1.

The cosine similarity is particularly used in positive space, where the outcome is neatly bounded in [0,1].

**Formula:**

![](https://lh3.googleusercontent.com/uvRyWx9U8bnp8uxP6Mr2xPiYS2u4p1v_lFAjczuEwM2lSCoSzZ_ZRCb6Ug3HQWgtG3ezmMdiKEXOmP7dBUZJc-xvu9TGAOapSUi9tZNR7vi7yzTYBaEmSFCIGNZmMwtbD2m2r-Vt)

Values range between -1 and 1, where -1 is perfectly dissimilar and 1 is perfectly similar.

## Facebook Artificial Intelligence Similarity Search (FAISS)

![](https://lh5.googleusercontent.com/HhCuVPKp8RDdlFjLZbjihK5-Kx5i03vCXlE98oYFpnZip_QCAiPHBOnZJGk2AqKu3h3JbQzT33a6TVSrLt7ObCJgDmvY_lpE6A9KTAG_86mWDtYSRD-HYDsk7BKa2j85okaSDKn0)

Facebook AI Similarity Search (FAISS), a library that allows to quickly search for multimedia documents that are similar to each other — a challenge where traditional query search engines fall short.  **Nearest-neighbor search**  has been built to implement billion-scale data sets that are some 8.5x faster than the previously reported state-of-the-art, along with the fastest k-selection algorithm on the GPU known in the literature.

![](https://lh5.googleusercontent.com/JsiLRPDlKi_n7hDM5Uhkx-DKaLroJDVMJsllE_EeYQ2AHgT98XMJzal18o1eFIDz-lppT0wHWYOuxyVzSn1SNdUqAJIxPOAgSM-JPQ4BCbfkQmECzTZlyfYpgeABgWJfggcDXjmh)

**Advantages:**

-   Speed
-   Memory Usage
-   Accuracy

## Spotify- Annoy:

Annoy ([Approximate Nearest Neighbors](http://en.wikipedia.org/wiki/Nearest_neighbor_search#Approximate_nearest_neighbor)  Oh Yeah) is a C++ library with Python bindings to search for points in space that are close to a given query point. It also creates large read-only file-based data structures that are  [mapped](https://en.wikipedia.org/wiki/Mmap)  into memory so that many processes may share the same data.

![](https://lh6.googleusercontent.com/-QaTbnF4VJVYTC7HVWjDmfmGeoXFf1jnxHtW7OwB7UN04l0x9Qt7NhuebEW21xA531ubZtmOCBWMOLFKm07mEc_k1tuYh0Qm0tdsKUprZ4RlCrQWN2RPkgaA3sBOMAF_Ne0m-fUU)

**Advantages:**

-   Works better if you don't have too many dimensions (like <100) but seems to perform surprisingly well even up to 1,000 dimensions
-   Small memory usage
-   Lets you share memory between multiple processes
