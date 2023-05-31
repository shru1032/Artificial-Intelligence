def knapsack_brute_force(values, weights, capacity):
 n = len(values)
 max_value = 0
 best_subset = None
 # Generate all possible subsets of items
 for i in range(2**n):
 subset = []
 subset_weight = 0
 subset_value = 0
 for j in range(n):
 if (i >> j) & 1==1:
 subset.append(j)
 subset_weight += weights[j]
 subset_value += values[j]

 # Check if the subset is feasible and has higher value than previous best
 if subset_weight <= capacity and subset_value > max_value:
 max_value = subset_value
 best_subset = subset
 return max_value, best_subset

print(knapsack_brute_force([10,20,30,40],[30,10,40,20],40))
