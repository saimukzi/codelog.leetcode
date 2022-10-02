class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num2_bit = self.cnt_bit(num2)
        num1_bit = self.cnt_bit(num1)
        # print(f'num1_bit={num1_bit} num2_bit={num2_bit}')
        
        if num1_bit >= num2_bit:
            bin1 = self.to_bin(num1)
            bit_remain = num1_bit-num2_bit
            i = len(bin1)-1
            while bit_remain > 0:
                if bin1[i] == '1':
                    bin1[i] = '0'
                    bit_remain -= 1
                i -= 1
            return int(''.join(bin1),2)
        else:
            bin1 = self.to_bin(num1)
            bit_remain = num2_bit-num1_bit
            i = len(bin1)-1
            while (bit_remain > 0) and (i >= 0):
                if bin1[i] == '0':
                    bin1[i] = '1'
                    bit_remain -= 1
                i -= 1
            return int(('1'*bit_remain) + ''.join(bin1),2)

    def cnt_bit(self, x):
        ret = 0
        while x > 0:
            if x % 2 == 1:
                ret += 1
            x //= 2
        return ret

    def to_bin(self,x):
        return list(bin(x).replace('0b',''))

# bin(5).replace('0b','')
