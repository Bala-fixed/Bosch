def is_balanced(x):
    stack = []
    opening = "({["
    closing = ")}]"
    mapping = {')': '(', '}': '{', ']': '['}

    for char in x:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack.pop() != mapping[char]:
                return "NO"
    return "YES" if not stack else "NO"


print(is_balanced('({'))
