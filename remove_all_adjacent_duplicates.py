"""
You are given a string s consisting of lowercase English letters. A duplicate removal 
consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be 
proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, 
and this is the only possible move.  The result of this move is that the string is "aaca", 
of which only "aa" is possible, so the final string is "ca".

Example 2:

Input: s = "azxxzy"
Output: "ay"
"""

class RemoveAdjacentDuplicates:

    def removeDuplicates(self, s: str) -> str:
        # Brute force, doesn't work for large string
        # i = 0
        # l = len(s)
        # while i < len(s):
        #     if i >= len(s)-1: break
        #     if s[i] == s[i+1]:
        #         s = s[:i] + s[i+2:]
        #         i = 0
        #     else:
        #         i = i + 1
        # return s

        # solution using stack
        """
        Time complexity : O(N), where N is a string length.
        Space complexity : O(N-D) where D is a total length for all duplicates.
        """
        result = []
        for ch in s:
            # check if the character is equal to the last character that was added
            if result and ch == result[-1]:
                # remove the last added character if its duplicate
                result.pop()
            else:
                # add the character in list
                result.append(ch)
        return ''.join(result)

if __name__ == "__main__":
    print(RemoveAdjacentDuplicates().removeDuplicates("abbaca"))