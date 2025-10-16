class GelinkteLijst():

    class Knoop():
        
        def __init__ (self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende
        
    def __init__(self) -> None:
        self.eerste = GelinkteLijst.Knoop()

    def zoek(self,zoek_item):
        ref = self.eerste.volgende # ankercomponent overslaan
        while(ref is not None and ref.data != zoek_item):
            ref = ref.volgende
        return ref 
    
    def voeg_toe_na(self, ref, element): # O(1) Constante
        nieuw = GelinkteLijst.Knoop() # We kunenn zaken toevoegen om minder lijnen te schrijven (constructor aanpassen)
        nieuw.data = element                                  # Of element toevoegen op deze manier, meer lijnen, maar makkelijker
        nieuw.volgende = ref.volgende                         # Of element toevoegen op deze manier, meer lijnen, maar makkelijker
        ref.volgende = nieuw

    def verwijder_na(self, ref):
        element = ref.volgende.data # element opslaan (voor verijderen)
        ref.volgende = ref.volgende.volgende
        return element

    def size(self) -> int:
        ref = self.eerste.volgende
        aantal_knopen = 0
        while ref is not None:
            ref = ref.volgende
            aantal += 1

        return aantal_knopen

    def invert(self):                                     
        lijst_invers = GelinkteLijst()                    
        ref = self.eerste                                 
        while ref is not None:                            
            ref = ref.volgende                            
            lijst_invers.voeg_toe_na(self.eerste, ref.data)

        return lijst_invers

l1 = GelinkteLijst()
l1.voeg_toe_na(l1.eerste, 6)
l1.voeg_toe_na(l1.eerste, 4)
l1.voeg_toe_na(l1.eerste, 3)
print(l1.size)
l1.verwijder_na(l1.eerste)
print(l1.size)