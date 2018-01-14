# sorting - Bubble sort
def bubbleSort (numbers):
  length = len(numbers)
  for i in range(0,length) :
    for j in range(0,length-1-i) :
      if numbers[j] > numbers[j+1] :
        numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
  return numbers    
      
numbersList = [7,8,2,28,35,75,20,39,43,25,16,32,70,81]
print(bubbleSort(numbersList))