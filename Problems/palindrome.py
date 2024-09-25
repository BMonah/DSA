class Palindrome:
    def __init__(self, num):
        self.num = num

    def palindrom(self):
        arr = []
        arr2 = []
        num = str(self.num)
        for i in range(0, len(num), 1):
            arr.append(num[i])
        for j in range(len(num)-1, -1, -1):
            arr2.append(num[j])

        print(arr, arr2)
        if arr == arr2:
            return True
        else:
            return False


print(Palindrome(-123).palindrom())


def isPalindrome(value):
    arr = []
    arr1 = []
    arr2 = []
    value = str(value)
    for i in value:
        arr.append(i)
    for i in range(0, len(arr), 1):
        arr1.append(arr[i])
    for i in range(len(arr)-1, -1, -1):
        arr2.append(arr[i])
    print(arr1, arr2)
    if arr1 == arr2:
        return True
    return False


print(isPalindrome('-12321-'))


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
