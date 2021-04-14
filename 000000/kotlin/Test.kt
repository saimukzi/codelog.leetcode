fun main() {
  test(123,true)
}

fun test(x: Int, expected: Boolean) {
  println("x=%d, expected=%s".format(x, expected))
  var solution: Solution = Solution()
  var result: Boolean = solution.func(x)
  println("result=%s".format(result))
  aassert(result == expected)
}

fun join(ary: IntArray): String {
  var sb: StringBuffer = StringBuffer()
  sb.append("[")
  var isFirst: Boolean=true
  for(v in ary){
      if(!isFirst){sb.append(",")}
      isFirst=false
      sb.append(Integer.toString(v))
  }
  sb.append("]")
  return sb.toString()
}

fun aassert(cond: Boolean){
    if(!cond)throw AssertionError()
}