from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:

        def func(left, right):
            if left >= right:
                return

            s[left], s[right] = s[right], s[left]
            func(left + 1, right - 1)

        func(0, len(s) - 1)