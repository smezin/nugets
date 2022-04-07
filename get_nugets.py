from typing import List

def can_i_have_that_many(packs: List[int], i_want_that_many: int) -> List[bool]:
    """
    param packs: the number of chicken nuggets in pack selection (i.e [6,9] means you can buy 6 or 9 nuggets pack)
    param i_want_that_many: number of nuggets you want to buy
    rvalue: True you can buy the desired amount, False otherwise
    """
    def gimme_nuggets(current_nuggets, i_want_that_many):
        if current_nuggets > i_want_that_many or is_possible[current_nuggets]:
            return
       
        is_possible[current_nuggets] = True

        for pack in packs:
            gimme_nuggets(current_nuggets + pack, i_want_that_many)
       
    is_possible = [False for _ in range(i_want_that_many + 1)]
    gimme_nuggets(0, i_want_that_many)
    return is_possible[i_want_that_many]

#driver
if __name__ == "__main__":
    packs = [6, 9, 20]
    i_want_that_many = 43
    print (can_i_have_that_many(packs, i_want_that_many))