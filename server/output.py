import ws_artbar as artbar
import ws_depog as depog
import ws_hadi as hadi
import ws_husa as husa
import ws_marta as marta
import ws_mdb as mdb
import ws_ndb as ndb
import ws_zahradbami as zahrad
import ws_polar as polar
import ws_teren as teren
import ws_bolek as bolek
import ws_radost as radost

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

## Out of order
# import ws_feste as feste
# output.append(feste.feste_output)

## connection issues
# import ws_buran as buran
# output.append(buran.buran_output)