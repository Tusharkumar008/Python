import ast
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
if __name__ == "__main__":
    try:
        input_str = input("Enter the array of numbers (e.g., [2,7,11,15]): ")
        if not input_str.strip().startswith('['):
            input_str = f"[{input_str}]"
        nums = ast.literal_eval(input_str)
        target = int(input("Enter the target integer: "))
        solution = Solution()
        result = solution.twoSum(nums, target)
        print(f"Output: {result}")
    except ValueError:
        print("Invalid input! Please ensure you enter integers for the list and target.")
    except SyntaxError:
        print("Syntax Error! Please enter the list in a valid format like [2, 7, 11, 15].")