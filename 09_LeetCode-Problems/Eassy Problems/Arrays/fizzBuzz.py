class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = [""] * n
        for i in range(n): 
            if (i+1)%5 == 0 and (i+1)%3 ==0:    # Multicontition first to avoid overriding 
                arr[i] = "FizzBuzz"
            elif (i+1)%3 == 0:
                arr[i] = "Fizz"
            elif (i+1)%5 == 0:
                arr[i] = "Buzz"
            else:
                arr[i] = str(i+1)
        return arr