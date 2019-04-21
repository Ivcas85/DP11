class Ctverec:
    def __init__(self,strana):
        self.strana = strana

    def obvod(self):
        return self.strana*4

    def obsah(self):
        return self.strana**2

    def rozdil_obsahu(self,ctverec_druhy):
        return self.strana**2 - ctverec_druhy.strana**2

ctverec_prvni=Ctverec(9)
ctverec_druhy=Ctverec(3)

print(ctverec_prvni.obvod())
print(ctverec_druhy.obvod())
print(ctverec_prvni.obsah())
print(ctverec_druhy.obsah())
print(ctverec_prvni.rozdil_obsahu(ctverec_druhy))
