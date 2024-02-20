# Function to demonstrate printing pattern

""" 
* 
* * 
* * * 
* * * * 
* * * * * 
"""

def pypart(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
      
        print("\r")

# pypart(5)



# Function to demonstrate printing pattern triangle

""" 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""
def triangle(n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")

        k = k - 1
        for j in range(0, i+1):
            print("* ", end="")
     
        print("\r")

triangle(5)