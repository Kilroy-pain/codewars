def sum_two_smallest_numbers(numbers):  
    smallest_number = numbers[0]
    second_smallest_number = numbers[1]
    if numbers[0] < numbers[1]:
        smallest_number = numbers[0]
        second_smallest_number = numbers[1]
        
    else:
        smallest_number = numbers[1]
        second_smallest_number = numbers[0]   
        
    for number in numbers[2:-1]:
        if number < smallest_number:
            second_smallest_nummber = smallest_number
            smallest_number = number
            
        elif number > smallest_number and number < second_smallest_number:
            second_smallest_number = number
        
        
    return smallest_number + second_smallest_number
