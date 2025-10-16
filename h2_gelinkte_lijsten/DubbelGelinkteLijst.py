class DubbelGelinkteLijst():

    class DubbeleKnoop():
        
        def __init__ (self, data=None, volgende=None, vorige=None) -> None:
            self.data = data
            self.volgende = volgende
            self.vorige = vorige
        
    def __init__(self) -> None:
        self.eerste = DubbelGelinkteLijst.DubbeleKnoop()
        self.laatste = DubbelGelinkteLijst.DubbeleKnoop()
        self.eerste.volgende = self.laatste
        self.laatste.vorige = self.eerste

    def zoek(self,zoek_item):
        ref_vooruit = self.eerste.volgende # ankercomponent overslaan
        ref_achteruit = self.laatste.vorige # ankercomponent overslaan
        while(ref_achteruit != ref_vooruit \
              and ref_vooruit.vorige != ref_achteruit \
              and ref_vooruit.data != zoek_item and ref_achteruit.data != zoek_item \
            ):
            ref_vooruit = ref_vooruit.volgende
            ref_achteruit = ref_vooruit.vorige
        return ref 
    
    def voeg_toe_na(self, ref, element): # O(1) Constante
        nieuw = DubbelGelinkteLijst.DubbeleKnoop()
        nieuw.data = element
        nieuw.volgende = ref.volgende
        nieuw.vorige = ref

        ref.volgenede.vorige = nieuw
        ref.volgende = nieuw

    def voeg_toe_voor(self, ref, element):
        self.voeg_toe_na(ref.vorige, element)

    def verwijder_na(self, ref):
        element = ref.data
        ref.volgende.vorige = ref.vorige
        ref.vorige.volgende = ref.volgende
        return element

    def size(self) -> int:
        ref = self.eerste.volgende
        aantal_knopen = 0
        while ref != self.laatste:
            ref = ref.volgende
            aantal += 1

        return aantal_knopen

    def invert(self):                                     
        lijst_invers = GelinkteLijst()                    
        ref = self.eerste                                 
        while ref is not None:                            
            ref = ref.volgende                            
            lijst_invers.voeg_toe_na(self.eerste, ref.data)

l1 = GelinkteLijst()
l1.voeg_toe_na(l1.eerste, 6)
l1.voeg_toe_na(l1.eerste, 4)
l1.voeg_toe_na(l1.eerste, 3)
print(l1.size)
l1.verwijder_na(l1.eerste)
print(l1.size)