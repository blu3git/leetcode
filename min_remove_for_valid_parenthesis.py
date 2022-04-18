"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
"""

import enum


class MinimumRemoveToMakeValidParenthesis:

    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Maintain a stack. Add index whenever ( is found. If ) is found after that
        and stack already has an index for ( then it means we have found a valid match
        of () -> remove the index value of ( from stack. If stack is empty and we get ), 
        then it means we found a ) before ( -> which is not valid as the parenthesis should
        occur in () order only. So we add the index for invalid ) in idx_remove set.
        Now, there is a chance that we found ( but didn't find its matching ) in the string.
        So the index for ( will still be there in the stack. In the end, we do a union of 
        stack indexes and idx_remove indexes and form a valid string by removing all invalid
        parenthesis. A set is used instead of string as it is faster to search for an item in
        set.

        Time complexity : O(n), where nn is the length of the input string.

        There are 3 loops we need to analyze. We also need to check carefully for any library 
        functions that are not constant time.

        The first loop iterates over the string, and for each character, either does nothing, 
        pushes to a stack or adds to a set. Pushing to a stack and adding to a set are both O(1). 
        Because we are processing each character with an O(1) operation, this overall loop is O(n).

        The second loop (hidden in library function calls for the Python code) pops each item from 
        the stack and adds it to the set. Again, popping items from a stack is O(1), and there are 
        at most nn characters on the stack, and so it too is O(n).

        The third loop iterates over the string again, and puts characters into a list. Checking if 
        an item is in a set and appending to the end of a list is O(1). Again, this is O(n) overall.

        The "".join(...) method is O(n). So again, this operation is O(n).
        So this gives us O(4n), and we drop the 4 because it is a constant.

        Space complexity : O(n), where nn is the length of the input string.

        We are using a stack, set, and string builder, each of which could have up to n characters 
        in them, and so require up to O(n) space.
        """
        if s.isalpha():
            return s

        stack = []
        idx_remove = set()
        for idx, el in enumerate(s):
            if el not in "()":
                continue
            elif el == "(":
                stack.append(idx)
            elif not stack:
                idx_remove.add(idx)
            else:
                stack.pop()
        idx_remove = idx_remove.union(set(stack))
        return ''.join([x for i, x in enumerate(s) if i not in idx_remove])

if __name__ == "__main__":
    print(MinimumRemoveToMakeValidParenthesis().minRemoveToMakeValid("a))b(c)d"))