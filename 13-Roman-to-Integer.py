class Solution(object):
    def romanToInt(self, s):
        romanDict = {
            \I\: 1,
            \IV\: 4,
            \V\: 5,
            \IX\: 9,
            \X\: 10,
            \XL\: 40,
            \L\: 50,
            \XC\: 90,
            \C\: 100,
            \CD\: 400,
            \D\: 500,
            \CM\: 900,
            \M\: 1000
        }

        total = 0
        i = 0
        while i < len(s):
            # Check if the current and next character form a valid Roman numeral and prevent index out of range error
            if i + 1 < len(s) and s[i:i+2] in romanDict:
                total += romanDict[s[i:i+2]]
                i += 2  # Move past the next character as it's part of the current numeral
            else:
                # Single character numeral
                total += romanDict[s[i]]
                i += 1

        return total

