#uses python3, yes i know this code is terrible and only runs on one thread.

#n is the number in which to calculate all prime numbers from 0. i.e. if n = 100 any primes in range 0-100 will be singled out and saved. since the main goal is to factor primes for a given bit length public
#key the number is divided by 2 as it is pointless to calculate any integers that would result in a product larger than the maximum bit length.
n=(2**256)//2
#opens prime number file and sets the starting number to the last prime stored. it tests for a empty line ("") as well as ensuring that the number isn't smaller than the last one ensuring incomplete values
#are not used thus ruining progress. pretty inneficient given it checks every single line individually but is not much of a concern personally due to relatively low overall computation needed.
#optimization is very welcome.
nums=open("primes.txt","r")
num=0
for line in nums:
  if line=="":
    break
  elif int(line)>num:
      num=int(line)
print("starting at"+str(num))
nums.close()
i=num
#integer used as if a boolean. represents if the number is prime or not
prime=0

#buffer used to store prime values. not strictly nessisary but may provide a miniscule amount of performance improvement as well as seperate the sections of code better so as to enhance readability with minimal time/effort put in.
target_buffer_size=50000
buffer_size=0
prime_buffer=[]

#loops through all the numbers between the starting number and n before determining whether each number is a prime or not by brute force.
while(i<n):
  j=1
  while(j<i//2):
    j+=2
    
    #checks if the number is prime using the modulous operator. if the number is divisible by any positive integer below its own value it is not prime so if there is no remainder it can be assumed not prime.
    if(i%j == 0):
      prime=0
      #no need to keep checking all the other numbers in the loop so exit early.
      break
      
  #if it is determined to be prime add it to the buffer
  if(prime==1):
    prime_buffer.append(i)
    buffer_size+=1
    
  #if the buffer size is greater than or equal to the target save all the values and reset the buffer.
  if(buffer_size>=target_buffer_size):
    output=open("primes.txt","a")
    for p in prime_buffer:
      output.write(str(p)+"\n")
    prime_buffer=[]
    buffer_size=0
    output.close()
  prime=1
  i+=2
