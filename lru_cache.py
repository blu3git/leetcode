"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""

from collections import OrderedDict


class LRUCache(OrderedDict):
    """
    We're asked to implement the structure which provides the following operations 
    in O(1) time :

        Get the key / Check if the key exists

        Put the key

        Delete the first added key

    The first two operations in O(1) time are provided by the standard hashmap, and 
    the last one - by linked list.
    There is a structure called ordered dictionary, it combines behind 
    both hashmap and linked list. In Python this structure is called OrderedDict.

    Time complexity : O(1) both for put and get since all operations with ordered 
    dictionary : get/in/set/move_to_end/popitem (get/containsKey/put/remove) are done 
    in a constant time.

    Space complexity : O(capacity) since the space is used only for an ordered dictionary 
    with at most capacity + 1 elements.
    """

    def __init__(self, capacity: int):
        if capacity > 3000: raise Exception("Invalid capacity value.")
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1); # cache is {1=1}
    lRUCache.put(2, 2); # cache is {1=1, 2=2}
    print(lRUCache.get(1))    # return 1
    lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2))   # returns -1 (not found)
    lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(lRUCache.get(1))    # return -1 (not found)
    print(lRUCache.get(3))    # return 3
    print(lRUCache.get(4))    # return 4

