# a=[[1,4],[4,8]]
# i=0
# r=1
# while i<len(a):
#     j=1
#     while j<len(a):
#         print(a[i][r])
#         j=j+1
#         r=r-1
#     i=i+1


# n=int(input("enter the number"))
# i=1
# sum=0
# while i<=n:
#           if i%3==0:
#                     sum=sum+i
#                     print(sum)

#           i=i+1
#           print(sum)


# a="srisai"
# n=len(a)
# for i in range(n):
#           for j in range(i+1):
#               print(a[j],"l",end="") 
#           print()     

# a=150//10
# print(a)

# n,atm=map(float,input().split())
# n=int(n)
# if (n+0.5<=atm and n%5==0):
#     print(float(atm-n-0.5))
# else:
#     print(float(atm))



# number=["","one","two","three","four"]
# n=int(input("Enter a number"))
# print(number[n])


n=int(input("enter the number"))
i=1
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end=" ")
        k=k+1
    j=i
    while j>=1:
        print(j,end=" ")
        j=j-1
    k=2
    while k<=i:
        print(k,end=" ")
        k=k+1
    i=i+1
    print()

