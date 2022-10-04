class Wordplay:
# • words_with_length(length) — returns a list of all the words of length length
# • starts_with(s) — returns a list of all the words that start with s
# • ends_with(s) — returns a list of all the words that end with s
# • palindromes() — returns a list of all the palindromes in the list
# • only(L) — returns a list of the words that contain only those letters in L
# • avoids(L) — returns a list of the words that contain none of the letters in L
    def __init__(self,Words) -> None:
        self.Words=Words
    def words_with_length(self,length):
        return [word for word in self.Words if len(word)==length]
    def starts_with(self,s):
        return [word for word in self.Words if word[0]==s]
    def ends_with(self,s):
        return [word for word in self.Words if word[-1]==s]
    def palindromes(self) :
        return [word for word in self.Words if word == word[::-1]]
    def only(self,l) :
        x=len(l)
        for i in self.Words:
            B=True
            for j in i :
                if j not in l: B=False
            if B: l.append(i)    
        return l[x:]
    def avoid(self,l) :
        x=len(l)
        for i in self.Words:
            B=True
            for j in i :
                if j in l: B=False
            if B: l.append(i)    
        return l[x:]
Game1=Wordplay(['append','pop','insert','get']) 
print(Game1.words_with_length(3)) 
print(Game1.starts_with('a'))   
print(Game1.ends_with('t'))   
print(Game1.palindromes())   
print(Game1.only(['a','p','e','n','d']))   
print(Game1.avoid(['a','p']))   





        