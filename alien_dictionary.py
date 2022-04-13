"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a 
different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true 
if and only if the given words are sorted lexicographically in this alien language.

Example - 

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

"""


class AlienDictionary:

    def isAlienSorted(self, words, order):
        """
        Let N be the length of order, and M be the total number of characters 
        in words.

        Time complexity : O(M).

        Storing the letter-order relation of each letter takes O(N) time. 
        For the nested for-loops, we examine each pair of words in the outer-loop 
        and for the inner loop, we check each letter in the current word. 
        Therefore, we will iterate over all of letters in words.

        Taking both into consideration, the time complexity is O(M + N). However, 
        we know that NN is fixed as 2626. Therefore, the time complexity is O(M).

        Space complexity : O(1). The only extra data structure we use is the 
        hashmap/array that serves to store the letter-order relations for each word 
        in order. Because the length of order is fixed as 2626, this approach achieves 
        constant space complexity.
        """
        if len(words) < 2: 
            return True

        order_dict = {}
        for index, letter in enumerate(order):
            order_dict[letter] = index
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                # if length of words is not same, i.e., 
                # second word length is smaller
                if j >= len(words[i+1]): return False
                # we don't need to compare for matching words.
                if words[i][j] != words[i+1][j]:
                    # check order from the dictionary. In the above example, 
                    # h will be 0, l will be 1, etc.
                    if order_dict[words[i][j]] > order_dict[words[i+1][j]]:
                        return False
                    break
        return True



if __name__ == "__main__":
    words = ['hello', 'leetcode']
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(AlienDictionary().isAlienSorted(words, order))