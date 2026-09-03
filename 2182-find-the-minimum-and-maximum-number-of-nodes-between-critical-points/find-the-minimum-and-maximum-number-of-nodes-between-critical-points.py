class Solution:
    def nodesBetweenCriticalPoints(
        self,
        head: Optional[ListNode]
    ) -> List[int]:
        first = -1
        last = -1
        min_dist = float('inf')

        pos = 1

        prev = head
        curr = head.next

        while curr and curr.next:
            nxt = curr.next

            if (
                (curr.val > prev.val and curr.val > nxt.val)
                or
                (curr.val < prev.val and curr.val < nxt.val)
            ):
                if first == -1:
                    first = pos

                if last != -1:
                    min_dist = min(min_dist, pos - last)

                last = pos

            prev = curr
            curr = nxt
            pos += 1

        if first == -1 or first == last:
            return [-1, -1]

        return [min_dist, last - first]