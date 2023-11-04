
n=2**2040//2
print(n)
nums=open("allprimes.txt","r")
num=0
for line in nums:
  if line=="":
    break
  elif int(line)>num:
      num=int(line)
print(num)
nums.close()
i=num
prime=0
prime_buffer=[1,3]
while(i<n):
  j=1
  while(j<i):
    j+=4
    if(i%j == 0):
      prime=1
      break
  if(prime==1):
    prime_buffer.append(i)
  if(len(prime_buffer)>=50000):
    output=open("allprimes.txt","a")
    for p in prime_buffer:
      output.write(str(p)+"\n")
    prime_buffer=[]
    output.close()
  prime=0
  i+=2
