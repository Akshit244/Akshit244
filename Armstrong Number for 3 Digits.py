n=int(input("Enter the number to check its armstrong properties: "))
org=n
sum=0
while (n>0):
    sum+=(n%10)**3
    n//=10
print(sum)

if sum==org:
    print(org,"is an Armstrong number.")
else:
    print(org,"is not an Armstrong number.")
