'''
    Good morning! Here's your coding interview problem for today.

    This problem was asked by Stripe.

    Given an integer n, return the length of the longest consecutive run
    of 1s in its binary representation.

    For example, given 156, you should return 3.
'''

import sys

def toBinary(number):
    return bin(number)[2:].zfill(len(str(number)))

def longestConsecutive_1s(string):
    numList = list(string)
    print(numList)
    seqList = []

    if len(numList) == 1 and numList[0] == '0':
        seqList.append(0)
        return seqList

    elif len(numList) == 1 and numList[0] == '1':
        seqList.append(1)
        return seqList

    elif len(numList) != 1:
        consec_1s = 0
        for i in range(len(numList) - 1):
            if i == 0:
                if numList[i] == '0' and numList[i + 1] == '0':
                    continue
                elif numList[i] == '1' and numList[i + 1] == '0':
                    seqList.append(1)
                elif numList[i] == '1' and numList[i + 1] == '1':
                    consec_1s += 1

            if i != len(numList) - 2:
                if numList[i] == '0' and numList[i + 1] == '0':
                    consec_1s = 0
                elif numList[i] == '0' and numList[i + 1] == '1':
                    consec_1s += 1
                elif numList[i] == '1' and numList[i + 1] == '0':
                    seqList.append(consec_1s)
                    consec_1s = 0
                elif numList[i] == '1' and numList[i + 1] == '1':
                    consec_1s += 1

            else:
                if numList[i] == '0' and numList[i + 1] == '0':
                    consec_1s = 0
                elif numList[i] == '0' and numList[i + 1] == '1':
                    seqList.append(1)
                elif numList[i] == '1' and numList[i + 1] == '0':
                    seqList.append(consec_1s)
                    consec_1s = 0
                elif numList[i] == '1' and numList[i + 1] == '1':
                    consec_1s += 1
                    seqList.append(consec_1s)
                    consec_1s = 0

        return seqList


try:
    num = int(input("Please enter an integer: "))

except ValueError:
    print("Value Error! Please enter an integer when you re-run the program.")
    sys.exit(1)

else:
    binary_repr = toBinary(num)
    print("Number in Binary: ", binary_repr)

    consec_1_seq = longestConsecutive_1s(binary_repr)
    print("Consecutive 1 Sequences: ", consec_1_seq)
    print("Longest Consecutive Sequence of 1s: ", max(consec_1_seq))
    sys.exit(0)
