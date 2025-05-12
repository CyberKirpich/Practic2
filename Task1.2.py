def combinationSum(candidates, target):
    candidates.sort()
    results = []

    def backtrack(start, remaining_target, path):
        if remaining_target == 0:
            results.append(path[:])
            return
        if remaining_target < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining_target:
                break
            backtrack(i + 1, remaining_target - candidates[i], path + [candidates[i]])
    backtrack(0, target, [])
    return results
candidates = [2, 5, 2, 1, 2]
target = 5
print(combinationSum(candidates, target))
candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum(candidates, target))