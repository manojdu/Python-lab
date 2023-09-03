def is_pali(number):
    return str(number)==str(number)[::-1]
def count_occ(number):
    digits=[int(i) for i in str(number)]
    count={}
    for digit in digits:
        if digit in count:
            count[digit]+=1
        else:
            count[digit]=1
    return count
number=int(input("Enter a number:"))
if is_pali(number):
    print("The number is palindrome")
else:
    print("the numnber is not pali")
count=count_occ(number)
for digit,occ in count.items():
    print("digit {} occurs {} times".format(digit,occ))