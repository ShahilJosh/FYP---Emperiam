import re
from readcv import text

def extract_mobile_number(text_array):
    phone_numbers = []
    for text in text_array:
        phones = re.findall("[0-9+-]", text)
        print(phones)  # print the contents of the `phones` list
        if phones:
            for phone in phones:
                number = phone[0]
                if len(number) > 10:
                    phone_numbers.append('+' + number)
                else:
                    phone_numbers.append(number)
    return phone_numbers

# Example usage
text_array = text
numbers = extract_mobile_number(text_array)
print(numbers)