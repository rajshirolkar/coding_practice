class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        for i in range(len(searchWord)):
            temp = []
            for p in products:
                if p.startswith(searchWord[:i+1]):
                    temp.append(p)
            products = temp
            # if products: 
            products.sort()
            # else:
            #     break
            res.append(products[:3])
        return res