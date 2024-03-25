class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        for i in range(1, len(searchWord)+1):
            temp = []
            for p in products:
                if p.startswith(searchWord[:i]):
                    temp.append(p)
            products = temp
            # if products: 
            products.sort()
            # else:
            #     break
            res.append(products[:3])
        return res