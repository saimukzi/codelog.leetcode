import code

def test(input,expected):
    print(input,expected)
    solution = code.Solution()
    result = solution.minimizeXor(*input)
    print(result)
    assert(result == expected)

# given
test((3,5),3)
test((1,12),3)
# judge
test((25,72),24)
