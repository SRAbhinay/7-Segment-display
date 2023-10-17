seven_segment_patterns = {
    
    '0': ['###', 
          '# #', 
          '# #', 
          '# #', 
          '###'],
    
    '1': ['  #',
          '  #',
          '  #',
          '  #',
          '  #'],
    
    '2': ['###',
          '  #',
          '###',
          '#  ',
          '###'],
    
    '3': ['###',
          '  #',
          '###',
          '  #',
          '###'],
    
    '4': ['# #',
          '# #',
          '###',
          '  #',
          '  #'],
    '5': ['###',
          '#  ',
          '###',
          '  #',
          '###'],
    '6': ['###',
          '#  ',
          '###',
          '# #',
          '###'],
    '7': ['###',
          '  #',
          '  #',
          '  #',
          '  #'],
    '8': ['###',
          '# #',
          '###',
          '# #',
          '###'],
    '9': ['###',
          '# #',
          '###',
          '  #',
          '###']
}

def display_number(number):
    if number < 0:
        print("Please enter a non-negative integer.")
        return

    number_str = str(number)
    display = ["", "", "", "", ""]

    for digit in number_str:
        if digit in seven_segment_patterns:
            digit_pattern = seven_segment_patterns[digit]
            for i in range(5):
                display[i] += digit_pattern[i] + " "
    
    for row in display:
        print(row)

user_input = input("Enter a non-negative integer: ")
try:
    user_number = int(user_input)
    display_number(user_number)
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")
