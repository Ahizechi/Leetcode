class Solution(object):
    def isValid(self, s):
        # Define a stack to keep track of opening brackets
        stack = []
        # Define a dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate over each character in the string
        for character in s:
            # If the character is a closing bracket
            if character in bracket_map:
                # Pop the topmost element from the stack if it is not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the corresponding opening bracket
                if bracket_map[character] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(character)
        
        # If the stack is empty, all brackets were matched correctly; otherwise, return False
        return not stack
