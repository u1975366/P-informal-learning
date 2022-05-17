# def validate(s):
#     if 0 >= score:
#         return false
#     return true
#
while(1):
    score = input('Enter score: ')
    try:
        score = float(score)
    except:
        print("Please enter score in numerical values")
        continue
    # try bottom bit again after i know more about functions and error handling
    # else:
    #     break
    # try:
    #     if not validate(score):
    #         pass
    # except rangeError:
    #     print("Out of bounds working.")
    #     continue
    else:
        break
if 0.9 <= score and score < 1:
    print("A")
elif 0.8 <= score and score < 0.9:
    print("B")
elif 0.7 <= score and score < 0.8:
    print("C")
elif 0.6 <= score and score < 0.7:
    print("D")
elif 0.6 > score and score > 0:
    print("F")
else:
    print("Out of bounds.")
