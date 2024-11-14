# Apriori and PCY (Park-Chen-Yu) Algorithm Implementation

This project provides an implementation of the Apriori and Park-Chen-Yu (PCY) algorithms, commonly used for discovering frequent itemsets in large transactional datasets. Frequent itemsets are sets of items that appear together in transactions with a frequency above a specified threshold. This information is valuable in fields like market basket analysis, where patterns in consumer purchases can be identified and used for decision-making.

The Apriori algorithm is a classic approach for mining frequent itemsets, generating larger itemsets by building on smaller frequent ones. However, it can be memory-intensive when handling large datasets. The PCY algorithm addresses this limitation by incorporating a hash table that reduces memory usage, making the process more efficient, especially with high-dimensional data.

## My Implementation of the Apriori and Park Chen Yu (PCY) Algorithm

The Apriori Algorithm Program takes as input the items (L1, L2, ...), their counts (frequency), and returns the most frequent itemsets that fulfill the minimum support and confidence criteria.

The PCY Algorithm, on the other hand, accomplishes the same in a more memory-efficient approach with the use of hash tables to store the counts of smaller subsets.

