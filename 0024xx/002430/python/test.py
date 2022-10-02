import code

def test(input,expected):
    print(input,expected)
    solution = code.Solution()
    result = solution.deleteString(*input)
    print(result)
    assert(result == expected)

# given
test(("abcabcdabc",),2)
test(("aaabaab",),4)
test(("aaaaa",),5)

# extreme
test(('a'*4000,),4000)
