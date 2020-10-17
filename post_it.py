class PostIt:
    def __init__(self, hatter_szin, szoveg, szoveg_szin):
        self.hatter_szin = hatter_szin
        self.szoveg = szoveg
        self.szoveg_szin = szoveg_szin


sarga_postit = PostIt('sarga', 'Elso otlet!', 'kek')
rozsaszin_postit = PostIt('rozsaszin', 'Hurra!', 'fekete')
zold_postit = PostIt('zold', 'Szuper!', 'barna')
print(sarga_postit.hatter_szin)
print("hello" + "[2J")
