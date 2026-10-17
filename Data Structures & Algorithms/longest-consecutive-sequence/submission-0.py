class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0

        seq_len_map = defaultdict(int)
        for n in nums:
            if not seq_len_map[n]:
                seq_len_map[n] = seq_len_map[n-1] + seq_len_map[n+1] + 1
                seq_len_map[n - seq_len_map[n-1]] = seq_len_map[n]
                seq_len_map[n + seq_len_map[n+1]] = seq_len_map[n]
                max_length = max(max_length, seq_len_map[n])
        
        return max_length