from common import ws_depog as depog
from common import ws_artbar as artbar
from common import ws_hadi as hadi
from common import ws_husa as husa
from common import ws_marta as marta
from common import ws_mdb as mdb
from common import ws_ndb as ndb
from common import ws_polar as polar
from common import ws_teren as teren
from common import ws_bolek as bolek

# from common import ws_buran as buran
# from common import ws_zahradbami as zahrad
# from common import ws_radost as radost
# from common import ws_feste as feste
from pydash import flatten


def webscraped():
    output = []
    output.append(depog.depog())
    output.append(artbar.artbar())
    output.append(husa.husa())
    output.append(marta.marta())
    output.append(mdb.mdb())
    output.append(hadi.hadi())
    output.append(ndb.ndb())
    output.append(polar.polar())
    output.append(teren.teren())
    output.append(bolek.bolek())
    # output.append(buran.buran())
    # output.append(zahrad.zahradbami())
    # output.append(radost.radost())
    # output.append(feste.feste())
    flat_output = flatten(output)
    return flat_output
