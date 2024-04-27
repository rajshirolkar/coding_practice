class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        rec_ing_cnt = defaultdict(int)
        graph = defaultdict(list)
        for rec, ing in zip(recipes, ingredients):
            rec_ing_cnt[rec] = len(ing)
            for i in ing:
                graph[i].append(rec)
        
        res = []
        leaves = deque(supplies)
        recipes = set(recipes)

        while leaves:
            supply = leaves.popleft()

            if supply in recipes:
                res.append(supply)
            
            for rec in graph[supply]:
                rec_ing_cnt[rec] -= 1
                if rec_ing_cnt[rec] == 0:
                    leaves.append(rec)
        return res
            
            
            
        