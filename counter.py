def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count+=1
    return count
assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "one upper case"
assert count_upper_case("a") == 0, "one lower case"
assert count_upper_case("%$£%^%") == 0, "Special charaters"
assert count_upper_case("DaDLLedmjYYT") == 7,"7 Upper case"
assert count_upper_case("^$%$£&*G") == 1,"1 Upper case"

print("All test passed")