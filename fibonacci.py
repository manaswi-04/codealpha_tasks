# Program to display the Fibonacci sequence up to n terms

# Taking input from the user
n_terms = int(input("Enter the number of terms: "))

# First two terms
n1, n2 = 0, 1
count = 0

# Check if the number of terms is valid
if n_terms <= 0:
    print("Please enter a positive integer")
elif n_terms == 1:
    print("Fibonacci sequence up to", n_terms, "term:")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
