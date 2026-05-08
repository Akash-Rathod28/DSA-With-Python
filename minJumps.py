from collections import defaultdict, deque

class Solution:
    def minJumps(self, nums):
        n = len(nums)
        MAXV = max(nums)

        # Sieve for prime check
        is_prime = [True] * (MAXV + 1)
        if MAXV >= 0:
            is_prime[0] = False
        if MAXV >= 1:
            is_prime[1] = False

        p = 2
        while p * p <= MAXV:
            if is_prime[p]:
                for multiple in range(p * p, MAXV + 1, p):
                    is_prime[multiple] = False
            p += 1

        # prime -> indices divisible by prime
        divisible = defaultdict(list)

        for i, num in enumerate(nums):
            x = num
            d = 2

            while d * d <= x:
                if x % d == 0:
                    if is_prime[d]:
                        divisible[d].append(i)

                    while x % d == 0:
                        x //= d
                d += 1

            if x > 1:
                divisible[x].append(i)

        q = deque([0])
        visited = [False] * n
        visited[0] = True

        used_prime = set()
        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                if i == n - 1:
                    return steps

                # adjacent moves
                if i - 1 >= 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    q.append(i - 1)

                if i + 1 < n and not visited[i + 1]:
                    visited[i + 1] = True
                    q.append(i + 1)

                # teleportation only if nums[i] is prime
                val = nums[i]

                if is_prime[val] and val not in used_prime:
                    for ni in divisible[val]:
                        if not visited[ni]:
                            visited[ni] = True
                            q.append(ni)

                    used_prime.add(val)

            steps += 1

        return -1
