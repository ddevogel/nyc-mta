from update import Update
from feed_providers.nyc_mta import NycMta
from feed_providers.bos_mbta import BosMbta

# NycMta.load()
# BosMbta.load()


# nyc = NycMta()
# entities = nyc.get("ace")

bos = BosMbta()
entities = bos.get("vehicle")
x="x"

