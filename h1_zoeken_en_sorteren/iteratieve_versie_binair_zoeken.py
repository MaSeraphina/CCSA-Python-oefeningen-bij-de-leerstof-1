

def zoek_binair(rij, getal):
  links = 0
  rechts = len(rij) - 1

  while links != rechts: # lengte rij > 1
    print(f'{links}, {rechts}')

    midden = (links+rechts)//2
    if rij[midden] < getal:
      links = midden+1 # verder zoeken rechterkant
    else:
      rechts = midden

  # 1 getal over
  if rij[links] == getal:
    #gevonden
    return links
  else: 
    return -1


# mijn_rij = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# getal  = 70
# print(zoekBinair(mijn_rij, getal))