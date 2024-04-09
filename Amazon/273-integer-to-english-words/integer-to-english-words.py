class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        less_than_20 = [
            '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
            'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
            'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
        ]
        tens = [
            '', 'Ten', 'Twenty', 'Thirty', 'Forty', 
            'Fifty', 'Sixty', 'Seventy', 'Eighty',  'Ninety'
        ]
        thousands = ['Billion', 'Million', 'Thousand', '']

        def translate(num):
            if num == 0:
                return ''
            elif num < 20:
                return less_than_20[num] + ' '
            elif num < 100:
                return tens[num // 10] + ' ' + translate(num % 10)
            else:
                return less_than_20[num // 100] + " Hundred " + translate(num % 100)
        
        i = 1000000000
        j = 0
        res = []
        while i > 0:
            if num//i != 0:
                res.append(translate(num // i))
                res.append(thousands[j])
                res.append(' ')
                num %= i
            j += 1
            i //= 1000
        return ''.join(res).strip()