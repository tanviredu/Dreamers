def first_half(s):
    # Calculate the length of the string
    length = len(s)
    
    # Calculate the index where we need to split the string (halfway point)
    split_index = length // 2
    
    # Use string slicing to extract the first half of the string
    first_half_string = s[:split_index]
    
    return first_half_string

# Example usage:
string = "WooHoo"
result = first_half(string)
print(result)  # Output: "Woo"
