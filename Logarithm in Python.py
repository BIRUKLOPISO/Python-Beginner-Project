import math

# Calculating the logarithm of a number
num = 100
log_base_10 = math.log10(num)
log_base_e = math.log(num)

print("Logarithm of", num, "with base 10 is:", log_base_10)
print("Logarithm of", num, "with base e is:", log_base_e)

# Calculating the power of a number using logarithms
base = 2
exponent = 8
result = math.pow(base, exponent)
log_result = math.log(result, base)

print("Result of", base, "raised to the power of", exponent, "is:", result)
print("Logarithm of", result, "with base", base, "is:", log_result)