"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping 
intervals, and return an array of the non-overlapping intervals that cover all the 
intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

class MergeIntervals:
    def merge(self, intervals):
        """
        If we sort the intervals by their start value, then each set of intervals that 
        can be merged will appear as a contiguous "run" in the sorted list.

        Algorithm

        First, we sort the list as described. Then, we insert the first interval into our 
        merged list and continue considering each interval in turn as follows: If the current 
        interval begins after the previous interval ends, then they do not overlap and we can 
        append the current interval to merged. Otherwise, they do overlap, and we merge them 
        by updating the end of the previous interval if it is less than the end of the current 
        interval.

        A simple proof by contradiction shows that this algorithm always produces the correct 
        answer. First, suppose that the algorithm at some point fails to merge two intervals 
        that should be merged. This would imply that there exists some triple of indices i, j, 
        and k in a list of intervals ints such that i < j < k and (ints[i], ints[k]) can be 
        merged, but neither (ints[i], ints[j]) nor (ints[j], ints[k]) can be merged. From this 
        scenario follow several inequalities:

            ints[i].end<ints[j].start
            ints[j].end<ints[k].start
            ints[i].end≥ints[k].start
        
        We can chain these inequalities (along with the following inequality, implied by the 
        well-formedness of the intervals: ints[j].start ≤ ints[j].end) to demonstrate a 
        contradiction:
            ints[i].end<ints[j].start≤ints[j].end<ints[k].start
            ints[i].end≥ints[k].start
        Therefore, all mergeable intervals must occur in a contiguous run of the sorted list.

        Complexity Analysis

        Time complexity : O(nlogn)

        Other than the sort invocation, we do a simple linear scan of the list, so the runtime 
        is dominated by the O(nlogn) complexity of sorting.

        Space complexity : O(logN) (O(n))

        If we can sort intervals in place, we do not need more than constant additional space, 
        although the sorting itself takes O(\log n)O(logn) space. Otherwise, we must allocate 
        linear space to store a copy of intervals and sort that.

        """
        # sort the list in-place so that extra space is not used 
        # for another object
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged



if __name__ == "__main__":
    mi = MergeIntervals()
    print(mi.merge([[2,6],[1,3],[8,10],[15,18]]))
    print(mi.merge([[1,4],[4,5]]))