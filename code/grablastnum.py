import datetime
nums=open("primes.txt","r")
num=0
now = datetime.datetime.now()
for line in nums:
  if line=="":
    break
  elif int(line)>num:
      num=int(line)
print(now.strftime("%Y-%m-%d %H:%M:%S")+ " -- " + str(num))
nums.close()
