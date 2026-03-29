# 15. 3Sum


# HashMap
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        hm = {}
        res = set()
        n = len(nums)

        for k, v in enumerate(nums):
            hm[v] = k

        for i in range(n):
            for j in range(i+1, n):
                rem = -nums[i] - nums[j]

                if rem in hm and hm[rem] != i and hm[rem] != j:
                    res.add(tuple(sorted([nums[i], nums[j], rem])))

        res = list(map(list, res))
        # res = [list(tup) for tup in res]

        return res


# Two Pointers
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            lp, rp = i+1, n-1
            while lp < rp:
                summ = nums[i] + nums[lp] + nums[rp]

                if summ == 0:
                    res.append([nums[i], nums[lp], nums[rp]])

                    lp, rp = lp+1, rp-1
                    while lp < rp and nums[lp] == nums[lp-1]:
                        lp += 1
                    while lp < rp and nums[rp] == nums[rp+1]:
                        rp -= 1

                elif summ < 0:
                    lp += 1

                else:
                    rp -= 1

        return res

