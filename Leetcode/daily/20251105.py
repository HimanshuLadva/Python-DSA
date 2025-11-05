# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii?envType=daily-question&envId=2025-11-05
# #MIMP

from typing import List
from collections import Counter
from heapq import nlargest
import heapq
import bisect
from sortedcontainers import SortedList
class Solution:
    # 3064ms
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        Find the x-sum of all k-long subarrays.
        
        x-sum: Sum of occurrences of top x most frequent elements.
        Tie-breaker: If frequencies are equal, larger value is more frequent.
        """
        
        def add_to_sets(value: int) -> None:
            """Add element to top_x or remaining based on priority."""
            if frequency[value] == 0:
                return
            
            priority = (frequency[value], value)
            
            # If priority is better than minimum in top_x, add to top_x
            if top_x and priority > top_x[0]:
                nonlocal current_sum
                current_sum += priority[0] * priority[1]
                top_x.add(priority)
            else:
                remaining.add(priority)
        
        def remove_from_sets(value: int) -> None:
            """Remove element from whichever set it belongs to."""
            if frequency[value] == 0:
                return
            
            priority = (frequency[value], value)
            
            if priority in top_x:
                nonlocal current_sum
                current_sum -= priority[0] * priority[1]
                top_x.remove(priority)
            else:
                remaining.remove(priority)
        
        # Initialize data structures
        top_x = SortedList()  # Top x elements by (frequency, value)
        remaining = SortedList()  # Remaining elements
        frequency = Counter()  # Frequency counter
        current_sum = 0
        n = len(nums)
        result = [0] * (n - k + 1)
        
        # Process each element
        for i in range(n):
            current_value = nums[i]
            
            # Update frequency
            remove_from_sets(current_value)
            frequency[current_value] += 1
            add_to_sets(current_value)
            
            # Check if we have a complete window
            window_start = i - k + 1
            if window_start < 0:
                continue
            
            # Balance sets: ensure top_x has exactly x elements (or all if less than x)
            while remaining and len(top_x) < x:
                element = remaining.pop()
                top_x.add(element)
                current_sum += element[0] * element[1]
            
            while len(top_x) > x:
                element = top_x.pop(0)
                current_sum -= element[0] * element[1]
                remaining.add(element)
            
            # Store result
            result[window_start] = current_sum
            
            # Remove leftmost element from window
            leftmost = nums[window_start]
            remove_from_sets(leftmost)
            frequency[leftmost] -= 1
            if frequency[leftmost] > 0:
                add_to_sets(leftmost)
        
        return result
    
    # 3102ms
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def add(v: int):
            if cnt[v] == 0:
                return
            p = (cnt[v], v)
            if l and p > l[0]:
                nonlocal s
                s += p[0] * p[1]
                l.add(p)
            else:
                r.add(p)

        def remove(v: int):
            if cnt[v] == 0:
                return
            p = (cnt[v], v)
            if p in l:
                nonlocal s
                s -= p[0] * p[1]
                l.remove(p)
            else:
                r.remove(p)

        l = SortedList()
        r = SortedList()
        cnt = Counter()
        s = 0
        n = len(nums)
        ans = [0] * (n - k + 1)
        for i, v in enumerate(nums):
            remove(v)
            cnt[v] += 1
            add(v)
            j = i - k + 1
            if j < 0:
                continue
            while r and len(l) < x:
                p = r.pop()
                l.add(p)
                s += p[0] * p[1]
            while len(l) > x:
                p = l.pop(0)
                s -= p[0] * p[1]
                r.add(p)
            ans[j] = s

            remove(nums[j])
            cnt[nums[j]] -= 1
            add(nums[j])
        return ans
    
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        Find the sum of top x frequent elements for each sliding window of size k.
        Elements are ranked by (frequency, value) in descending order.
      
        Args:
            nums: Input array
            k: Window size
            x: Number of top frequent elements to sum
      
        Returns:
            List of sums for each window
        """
      
        def add_to_sets(value: int) -> None:
            """Add element to either top_x_set or remaining_set based on its priority."""
            if frequency_map[value] == 0:
                return
          
            priority_tuple = (frequency_map[value], value)
          
            # If top_x_set is empty or this element has higher priority than the minimum in top_x_set
            if top_x_set and priority_tuple > top_x_set[0]:
                nonlocal current_sum
                current_sum += priority_tuple[0] * priority_tuple[1]  # frequency * value
                top_x_set.add(priority_tuple)
            else:
                remaining_set.add(priority_tuple)
      
        def remove_from_sets(value: int) -> None:
            """Remove element from whichever set it belongs to."""
            if frequency_map[value] == 0:
                return
          
            priority_tuple = (frequency_map[value], value)
          
            if priority_tuple in top_x_set:
                nonlocal current_sum
                current_sum -= priority_tuple[0] * priority_tuple[1]  # frequency * value
                top_x_set.remove(priority_tuple)
            else:
                remaining_set.remove(priority_tuple)
      
        # Initialize data structures
        top_x_set = SortedList()      # Maintains top x elements by (frequency, value)
        remaining_set = SortedList()   # Maintains remaining elements
        frequency_map = Counter()       # Tracks frequency of each element in current window
        current_sum = 0                 # Sum of top x elements
        n = len(nums)
        result = [0] * (n - k + 1)     # Result array for each window
      
        # Process each element
        for i, current_value in enumerate(nums):
            # Update frequency for current element
            remove_from_sets(current_value)
            frequency_map[current_value] += 1
            add_to_sets(current_value)
          
            # Calculate window start index
            window_start = i - k + 1
          
            # Skip if we haven't formed a complete window yet
            if window_start < 0:
                continue
          
            # Balance the sets: ensure top_x_set has exactly x elements
            # Move elements from remaining_set to top_x_set if needed
            while remaining_set and len(top_x_set) < x:
                element = remaining_set.pop()
                top_x_set.add(element)
                current_sum += element[0] * element[1]
          
            # Move excess elements from top_x_set to remaining_set
            while len(top_x_set) > x:
                element = top_x_set.pop(0)  # Remove smallest element
                current_sum -= element[0] * element[1]
                remaining_set.add(element)
          
            # Store result for current window
            result[window_start] = current_sum
          
            # Remove the leftmost element of the window for next iteration
            leftmost_element = nums[window_start]
            remove_from_sets(leftmost_element)
            frequency_map[leftmost_element] -= 1
            if frequency_map[leftmost_element] > 0:
                add_to_sets(leftmost_element)
      
        return result
    
    # opus 4
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        Alternative implementation using heaps instead of sorted lists.
        This might be needed if sortedcontainers is not available.
        """
        import heapq
        from collections import defaultdict
        
        n = len(nums)
        ans = []
        
        for start in range(n - k + 1):
            # Count frequencies in current window
            freq = defaultdict(int)
            for i in range(start, start + k):
                freq[nums[i]] += 1
            
            # Create list of (frequency, value) pairs
            freq_list = []
            for val, count in freq.items():
                # Use negative to create max heap behavior
                freq_list.append((-count, -val, val, count))
            
            # Use heap to get top x elements
            heapq.heapify(freq_list)
            
            # Calculate x-sum
            x_sum = 0
            elements_added = 0
            
            while freq_list and elements_added < x:
                _, _, val, count = heapq.heappop(freq_list)
                x_sum += val * count
                elements_added += 1
            
            ans.append(x_sum)
        
        return ans
    
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        count = Counter()
        sorted_items = []
        current_sum = 0
        
        def find_pos(item):
            left, right = 0, len(sorted_items)
            while left < right:
                mid = (left + right) // 2
                if sorted_items[mid] < item:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def update_sum():
            nonlocal current_sum
            if len(sorted_items) >= x:
                current_sum = sum(freq * val for freq, val in sorted_items[-x:])
            else:
                current_sum = sum(freq * val for freq, val in sorted_items)
        
        def update(val, old_freq, new_freq):
            # Remove old
            if old_freq > 0:
                pos = find_pos((old_freq, val))
                if pos < len(sorted_items) and sorted_items[pos] == (old_freq, val):
                    sorted_items.pop(pos)
            
            # Add new
            if new_freq > 0:
                pos = find_pos((new_freq, val))
                sorted_items.insert(pos, (new_freq, val))
        
        # Initialize first window
        for i in range(k):
            old = count[nums[i]]
            count[nums[i]] += 1
            update(nums[i], old, count[nums[i]])
        
        update_sum()
        result.append(current_sum)
        
        # Slide window
        for i in range(k, len(nums)):
            # Remove left
            left = nums[i - k]
            old = count[left]
            count[left] -= 1
            new = count[left]
            if new == 0:
                del count[left]
            update(left, old, new)
            
            # Add right
            right = nums[i]
            old = count.get(right, 0)
            count[right] += 1
            update(right, old, count[right])
            
            update_sum()
            result.append(current_sum)
        
        return result
    
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        count = Counter()
        
        # List to maintain sorted (frequency, value) pairs
        sorted_list = []
        
        def update(val, old_freq, new_freq):
            # Remove old entry
            if old_freq > 0:
                idx = bisect.bisect_left(sorted_list, (old_freq, val))
                if idx < len(sorted_list) and sorted_list[idx] == (old_freq, val):
                    sorted_list.pop(idx)
            
            # Add new entry
            if new_freq > 0:
                bisect.insort(sorted_list, (new_freq, val))
        
        # Build first window
        for i in range(k):
            old_freq = count[nums[i]]
            count[nums[i]] += 1
            update(nums[i], old_freq, count[nums[i]])
        
        # Calculate results
        if len(sorted_list) >= x:
            result.append(sum(freq * val for freq, val in sorted_list[-x:]))
        else:
            result.append(sum(freq * val for freq, val in sorted_list))
        
        # Slide window
        for i in range(k, len(nums)):
            # Remove left
            left_val = nums[i - k]
            old_freq = count[left_val]
            count[left_val] -= 1
            if count[left_val] == 0:
                del count[left_val]
            update(left_val, old_freq, count[left_val])
            
            # Add right
            right_val = nums[i]
            old_freq = count[right_val]
            count[right_val] += 1
            update(right_val, old_freq, count[right_val])
            
            # Calculate
            if len(sorted_list) >= x:
                result.append(sum(freq * val for freq, val in sorted_list[-x:]))
            else:
                result.append(sum(freq * val for freq, val in sorted_list))
        
        return result
    
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        count = Counter(nums[:k])
        
        for i in range(len(nums) - k + 1):
            if i > 0:
                count[nums[i - 1]] -= 1
                if count[nums[i - 1]] == 0:
                    del count[nums[i - 1]]
                count[nums[i + k - 1]] += 1
            
            # Use negative values for max heap behavior
            heap = [(-freq, -num) for num, freq in count.items()]
            heapq.heapify(heap)
            
            total = 0
            for _ in range(min(x, len(heap))):
                neg_freq, neg_num = heapq.heappop(heap)
                total += (-neg_freq) * (-neg_num)
            
            result.append(total)
        
        return result
    
    def findXSumV2(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        count = Counter(nums[:k])
        
        i = 0
        for i in range(len(nums) - k + 1):
            if i > 0:
                count[nums[i - 1]] -= 1
                if count[nums[i - 1]] == 0:
                    del count[nums[i - 1]]
                count[nums[i + k - 1]] += 1

            if len(count) >= x:
                top_x = nlargest(x, count.items(), key=lambda item: (item[1], item[0]))
                result.append(sum(num * freq for num, freq in top_x))
            else:
                result.append(sum(count.elements()))

        return result
    
    def findXSumV1(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        count = Counter(nums[:k])
        
        i = 0
        for i in range(len(nums) - k + 1):
            if i > 0:
                count[nums[i - 1]] -= 1
                if count[nums[i - 1]] == 0:
                    del count[nums[i - 1]]
                count[nums[i + k - 1]] += 1

            if len(count) >= x:
                sorted_items = sorted(count.items(), key=lambda x: (x[1], x[0]), reverse=True)
                tempsum = sum(sorted_items[j][0]*sorted_items[j][1] for j in range(x))
                result.append(tempsum)
            else:
                result.append(sum(count.elements()))

        return result
    
# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
    
sol = Solution()
nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2
sol.findXSum(nums, k, x)