# Write a python program to find the best of two test average marks out of three test’s marks accepted from the user.


def find_best_average(marks):
    marks.sort()
    return (marks[1]+marks[2])/2

tests=[]
for i in range(3):
    test=int(input("enter marks for test{}:".format(i+1)))
    tests.append(test)
best_average=find_best_average(tests)
print("The best average marks of two tests:{}".format(best_average))