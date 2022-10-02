import code

def test(input,expected):
    print(input,expected)
    solution = code.Solution()
    result = solution.maxSum(*input)
    print(result)
    assert(result == expected)

# given
test(([[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]],),30)
test(([[1,2,3],[4,5,6],[7,8,9]],),35)
