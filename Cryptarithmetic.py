from itertools import permutations
def solve_cryptarithmetic(puzzle):
 letters = set(char for word in puzzle for char in word if char.isalpha())
 for digits in permutations(range(10), len(letters)):
 sol = dict(zip(letters, digits))
 if all(sol[word[0]] != 0 for word in puzzle):
 nums = [int(''.join(str(sol[char]) for char in word)) for word in puzzle]
 if nums[0] + nums[1] == nums[2]:
 return sol
 return None
# example usage
puzzle = ['APPLE', 'LEMON', 'BANANA']
solution = solve_cryptarithmetic(puzzle)
if solution:
 for word in puzzle:
 print(word, ':', ''.join(str(solution[char]) for char in word))
else:
 print('No solution found.')
