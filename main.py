n = int(input("Please enter number of * for the pattern : "))
for i in range (1,n+1):
    print((''*(n-i)) +('*'*i), end="")
    print("")
for i in range((n-1),0,-1):
    print('*'*i)