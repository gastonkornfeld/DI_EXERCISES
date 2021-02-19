

# Instructions
# Write a Python function to reverse the bits of an integer (32 bits unsigned).
# Input : 1234
# Output : 1260388352
# For example, 1234 represented in binary as 10011010010 and returns 1260388352 which represents in binary as 01001011001000000000000000000000



def reverse_bit_integer(number):
    number_in_binary = str(bin(number))
    binary_backwards = number_in_binary[:2] + number_in_binary[:1:-1]
    new_number = int(binary_backwards, 2)
     
    return f"when you take the binary of {number} and reverse it the binary is this number: {new_number}"



print(reverse_bit_integer(1234))


