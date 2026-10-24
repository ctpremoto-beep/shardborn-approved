# Regenerates approved.json from img/<Faction>/ folders. To add an approval: drop the image into img/<Faction>/ and run python3 build.py, then git push.
import json,os,re
out=[]
order=["Cyborg","Agent","Builder","Explorer","Rogue","Trader","Validator"]
facs=sorted(os.listdir("img"),key=lambda f:(order.index(f) if f in order else 99,f))
for f in facs:
    items=[]
    for fn in sorted(os.listdir(f"img/{f}")):
        name=re.sub(r'^[A-Z]\d+_','',os.path.splitext(fn)[0]).replace('_',' ')
        items.append({"name":name,"id":fn.split('_')[0],"file":f"img/{f}/{fn}"})
    out.append({"faction":f,"items":items})
json.dump(out,open("approved.json","w"),indent=1)
