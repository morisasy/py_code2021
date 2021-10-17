from string import puchuation

Class Analyser():

    def __init__(self, s):
        for c in puchuation:
            s = s.replace(c, '')
            s = s.lower()
            self.words = s.split()

    def no_of_words(self):
        return len(self.words)

    def starts_with(self, s):
        return len([w for w in self.words if w[:len(s)==s]])
       


    def no_with_length(self, n):
         return len([w for w in self.words if len(w)==n])
       

s = "This is a string to analyse."

analyse = Analyser(s)
print(analyse.words)
print("Number of words:", analyse.no_of_words())
print("Number of words start wit 't' :", analyse.startswith('t'))
print("Number of 4-letter words:", analyse.no_with_length(4))
