class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            stack.append(a)
            #compare last two asteroids
            while len(stack) > 1 and stack[-1]<0 and stack[-2] >0:
                if abs(stack[-1]) > abs(stack[-2]):
                    stack.pop(-2)
                elif abs(stack[-1]) < abs(stack[-2]):
                    stack.pop()
                else:
                    stack.pop()
                    stack.pop()
        return stack
