from Webscraping import output
from pydash import flatten

merge = flatten(output.output)
print(merge)