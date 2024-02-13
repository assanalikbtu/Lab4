import json
from tabulate import tabulate

with open('sample-data.json') as f:
    data = json.load(f)
    d2 = data['imdata']
    headers = ["DN", "Description", "Speed", "MTU"]
    ans = []
    for i in d2:
        temp = i['l1PhysIf']['attributes']
        d = {'DN': temp.get('dn'),
             'Description': temp.get('pathSDescr'),
             'Speed': temp.get('speed'),
             'MTU': temp.get('mtu')}
        ans.append(d)
    print(tabulate(ans, headers="keys", tablefmt="fancy_grid"))

