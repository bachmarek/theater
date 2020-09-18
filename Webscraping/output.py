from Webscraping import ws_artbar as artbar
from Webscraping import ws_depog as depog
from Webscraping import ws_hadi as hadi
from Webscraping import ws_husa as husa
from Webscraping import ws_marta as marta
from Webscraping import ws_mdb as mdb
from Webscraping import ws_ndb as ndb
from Webscraping import ws_zahradbami as zahrad
from Webscraping import ws_polar as polar
from Webscraping import ws_teren as teren
from Webscraping import ws_bolek as bolek
from Webscraping import ws_radost as radost
#from Webscraping  import ws_feste as feste

output = []

output.append(depog.depog_output)
output.append(husa.husa_output)
output.append(marta.marta_output)
output.append(mdb.mdb_output)
output.append(hadi.hadi_output)
output.append(ndb.ndb_output)
output.append(artbar.artbar_output)
output.append(polar.polar_output)
output.append(zahrad.zahradbami_output)
output.append(teren.teren_output)
output.append(bolek.bolek_output)
output.append(radost.radost_output)
# output.append(feste.feste_output)

## connection issues
#from Webscraping  import ws_buran as buran
# output.append(buran.buran_output)