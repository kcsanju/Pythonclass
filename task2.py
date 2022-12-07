# def get_prime_numbers(num):
# for i in range(1, 101):
#     count = 0
#     for num in range(1, i+1):
#         if(i%j==0):
#             count= count +1
#     if(count== 2):
#             print(i)

    
# def is_prime():
#     for n in range(1,101):
#         status = True
#         if n < 2:
#             status = False
#         else:
#             for i in range(2,n):
#                 if n % i == 0:
#                     status = False
#         return status

# if is_prime():    
#     print(n, '', sep=',', end='')

# output = []
# def is_prime(n):
    
#     status = True
#     if n < 2:
#         status = False
#     else:
#         for i in range(2,n):
#             if n % i == 0:
#                 status = False
#     return status

# for n in range(1,101):
#     if is_prime(n):
#         if n==97:
#             output.append(n)
#     print (output)

# primes=[]
# for i in range(2,101): 
#     if all(i%p for p in primes): 
#         primes=[]
#         print(i) 
#         primes.append(i) 
#     print(primes)


output=[]
for i in range(2,101): 
    for j in range(2,101):
        if i%j == 0:
            break
        
    if i == j:
        
        
        output.append(i)
print(output)