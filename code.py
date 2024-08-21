
def function1(a):
    b = dict()
    for c in a:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    return b

def function2(a):
    print('freqs')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b]/total))

function2(function1('ATCTGACGCGCGCCGC'))

### UMGPT Documentation recommendation
# Certainly! I'll improve the readability of the code and add appropriate documentation.

# ```python
# def count_frequencies(sequence):
#     """
#     Count the frequency of each character in a given sequence.

#     Args:
#         sequence (str): A string for which character frequencies will be counted.

#     Returns:
#         dict: A dictionary where keys are characters and values are their respective counts.
#     """
#     frequency_dict = dict()
    
#     for char in sequence:
#         if char not in frequency_dict:
#             frequency_dict[char] = 1
#         else:
#             frequency_dict[char] += 1
    
#     return frequency_dict

# def print_normalized_frequencies(frequencies):
#     """
#     Print the normalized frequencies of characters in a dictionary.

#     Args:
#         frequencies (dict): A dictionary where keys are characters and values are their respective counts.

#     Returns:
#         None
#     """
#     print('Normalized Frequencies:')
#     total_count = float(sum(frequencies.values()))
    
#     for char, count in frequencies.items():
#         normalized_frequency = count / total_count
#         print(f"{char}: {normalized_frequency:.4f}")

# # Example usage
# sequence = 'ATCTGACGCGCGCCGC'
# frequencies = count_frequencies(sequence)
# print_normalized_frequencies(frequencies)
# ```

# ### Explanation:
# 1. **Function Renaming**:
#     - `function1` was renamed to `count_frequencies` to better describe its purpose.
#     - `function2` was renamed to `print_normalized_frequencies` for clarity.

# 2. **Documentation**:
#     - Added docstrings to both functions to describe their arguments and return values.

# 3. **Code Changes**:
#     - Used more descriptive variable names (`sequence`, `char`, `frequency_dict`) for clarity.
#     - Used `sum(frequencies.values())` to directly sum the values from the frequency dictionary.
#     - Used f-strings for formatted printing in `print_normalized_frequencies` for better readability.

# 4. **Example Usage**:
#     - Provided example usage at the bottom to show how the functions work together.
