def is_Palindrome(string):
    return string == string[::-1]

string1 = "civic"
string2 = "coconut"

print (is_Palindrome(string1))
print (is_Palindrome(string2))