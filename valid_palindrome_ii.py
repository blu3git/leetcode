"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Examples -
Input: s = "aba"
Output: true

Input: s = "abca" acba
Output: true
Explanation: You could delete the character 'c'.

Input: s = "abac" caba
Output: false
"""

class ValidPalindromeII:

    def validPalindrome(self, s):
        """
        Time Complexity = O(N)
        The main while loop we use can iterate up to N / 2 times, since each iteration represents a pair of characters. 
        On any given iteration, we may find a mismatch and call checkPalindrome twice. checkPalindrome can also iterate 
        up to N / 2 times, in the worst case where the first and last character of s do not match.

        Because we are only allowed up to one deletion, the algorithm only considers one mismatch. This means that checkPalindrome 
        will never be called more than twice.

        Space Complexity = O(1)
        The only extra space used is by the two pointers i and j, which can be considered constant relative to the input size.

        """
        if s == s[::-1]: return True
        i = 0
        j = len(s) - 1

        # start checking from both sides.
        while i < j:
            print("1st comparing: {} and  {}".format(s[i], s[j]))
            if s[i] != s[j]:
                # if two letters are not equal then check by skipping them
                return self.is_palindrome(s, i+1, j) or self.is_palindrome(s, i, j-1)
            i = i + 1
            j = j - 1

        # Another way to solve this by using slicing 
        # while left < right:
        #     if s[left] != s[right]:
        #         one = s[left:right]
        #         two = s[left+1:right+1]
        #         return one == one[::-1] or two == two[::-1]
        #     left += 1
        #     right -= 1
        return True

    def is_palindrome(self, word, left, right):
        while left < right:
            if word[left] != word[right]:
                return False
            left = left+1
            right = right - 1
        return True



if __name__ == "__main__":
    s = "abcba"
    print(ValidPalindromeII().validPalindrome(s))
