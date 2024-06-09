class Solution(object):
    def romanToInt(self, s):
        romanDict = {
            \I\: 1,
            \V\: 5,
            \X\: 10,
            \L\: 50,
            \C\: 100,
            \D\: 500,
            \M\: 1000
        }

        total = 0
        prev_value = 0
        
        # Process each character from the end to the start
        for char in reversed(s):
            value = romanDict[char]
            
            # If the current value is less than the previous one, subtract, otherwise add
            if value < prev_value:
                total -= value
            else:
                total += value
                prev_value = value

        return total