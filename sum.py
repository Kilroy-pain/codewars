def sum_two_smallest_numbers(numbers):  
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
            
    numbers.remove(smallest) 
    
    second_smallest = numbers[0]
    for number in numbers:
        if number < second_smallest:
            second_smallest = number
        
        
    return smallest + second_smallest
