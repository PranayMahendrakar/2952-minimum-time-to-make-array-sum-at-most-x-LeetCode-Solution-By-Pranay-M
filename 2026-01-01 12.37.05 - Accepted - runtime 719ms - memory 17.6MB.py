class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        s1, s2 = sum(nums1), sum(nums2)
        
        # If sum already <= x, no time needed
        if s1 <= x:
            return 0
        
        # Sort by nums2 in ascending order
        pairs = sorted(zip(nums1, nums2), key=lambda p: p[1])
        
        # dp[j] = max reduction we can achieve by setting j elements to 0
        # At time t, element i contributes nums1[i] + t * nums2[i]
        # If we set it to 0 at time j, we save nums1[i] + j * nums2[i]
        dp = [0] * (n + 1)
        
        for i, (a, b) in enumerate(pairs):
            # Iterate backwards to avoid using same element twice
            for j in range(i + 1, 0, -1):
                # Set this element to 0 at time j
                dp[j] = max(dp[j], dp[j - 1] + a + j * b)
        
        # Check each possible time
        for t in range(n + 1):
            if s1 + t * s2 - dp[t] <= x:
                return t
        
        return -1