import re

def is_valid_rrn(rrn):
    pattern = re.compile(r'^\d{6}[-]?\d{7}$')

    if not pattern.match(rrn):
        return False

    rrn_digits = re.sub(r'[^\d]', '', rrn)

    year = int(rrn_digits[:2])
    month = int(rrn_digits[2:4])
    day = int(rrn_digits[4:6])

    if month < 1 or month > 12:
        return False

    if day < 1 or day > 31:
        return False

    last_digit = int(rrn_digits[-1])

    if last_digit % 2 == 1:
        if year < 00 or year > 99:
            return False
    else:
        if year < 00 or year > 99:
            return False

    return True

rrn = input("주민등록번호를 입력하세요: ")
if is_valid_rrn(rrn):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
