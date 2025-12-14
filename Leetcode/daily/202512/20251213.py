from typing import List
import re
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        categories = ("electronics", "grocery", "pharmacy", "restaurant")
        res = []
        pattern = r'[A-Za-z0-9_]+'

        for c, b, flag in zip(code, businessLine, isActive):
            if flag and b in categories and re.fullmatch(pattern, c):
                res.append((b, c))

        res.sort()
        return [x[1] for x in res]
        
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def is_valid(s):
            return bool(s) and all(c.isalnum() or c == '_' for c in s)

        allowed_lines = {"electronics", "grocery", "pharmacy", "restaurant"}
        
        # Store valid coupons with their business lines
        valid_coupons = []
        for c, b, active in zip(code, businessLine, isActive):
            if is_valid(c) and b in allowed_lines and active:
                valid_coupons.append((c, b))
        
        # Define business line order
        business_order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        
        # Sort by business line first, then by code lexicographically
        valid_coupons.sort(key=lambda x: (business_order[x[1]], x[0]))
        
        # Extract just the codes
        return [c for c, b in valid_coupons]
    
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def is_valid(s):
            return bool(s) and all(c.isalnum() or c == '_' for c in s)

        allowed_lines = {"electronics", "grocery", "pharmacy", "restaurant"}
        ans = []
        for c,b,active in zip(code,businessLine,isActive):
            if is_valid(c) and b in allowed_lines and active:
                ans.append(c)
        return ans