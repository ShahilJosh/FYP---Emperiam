import re
from readcv import text

def extract_mobile_number(text):
    phone = re.findall(r'\+?(?:\d{1,4}[-\.\s]?)?(?:\d{1,3}[-\.\s]?)?\d{1,4}(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?', text)
    if phone:
        number = phone[0][0]
        extension = phone[0][1] if len(phone[0]) > 1 else None
        if len(number) > 10:
            return '+' + number
        else:
            return number