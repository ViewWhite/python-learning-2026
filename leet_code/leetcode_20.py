class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in mapping: # 如果是右括号
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char) # 如果是左括号，入栈
                
        return not stack # 最后栈为空说明全部匹配成功

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()[]{}"))  # True
    print(sol.isValid("(]"))      # False