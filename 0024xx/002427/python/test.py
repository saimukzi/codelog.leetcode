import code

def test(input,expected):
    print(input,expected)
    solution = code.Solution()
    result = solution.commonFactors(*input)
    print(result)
    assert(result == expected)

# given
test((12,6),4)
test((25,30),2)
