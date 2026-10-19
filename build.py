import html, json
G="https://platinum00001.github.io/"
groups=[
 ("Community & Recovery","rise",[
  ("Root to Rise MA","Recovery community for Mashpee and Falmouth: meetups, resources and support.","https://roottorisema.org",None),
  ("Root to Rise App","Benefits checker, resource finder and member perks for people in recovery.",G+"root-to-rise-app/",None),
  ("Recovery Milestones","Celebrate sobriety anniversaries with rewards from local businesses.",G+"recovery-milestones/",None),
  ("Clubs for Love","Donated golf gear and time on the course for people in recovery.","https://clubsforlove.com",None),
  ("Cape Island Recovery","Food transport and resource connection at 316 Gifford St, Falmouth.",G+"cape-island-recovery/","capeisland.org coming soon"),
  ("Health & Wellness Maps","A map of local wellness resources across Cape Cod.","https://healthandwellnessmaps.com",None),
 ]),
 ("Food & Cafe","cafe",[
  ("Cape Island Cafe","Lunch in Falmouth, MA. Order online.","https://capeislandcafe.com",None),
  ("Rex: Restaurant Exchange","Restaurant gift-card exchange for local kindness. Members only (access code).",G+"rex-app/",None),
  ("Chef Bookings","Book a private chef. Coming soon.","https://chefbookings.org",None),
  ("Koinonia Kitchen","Shared meals, shared life.",G+"koinoniakitchen.com/","koinoniakitchen.com coming soon"),
  ("Cape Sushi","Sushi on Cape Cod, from local waters.",G+"capesushi.com/","capesushi.com coming soon"),
 ]),
 ("Business & Services","math",[
  ("Autonomous Boat Service","Boat repair requests matched to trusted Cape Cod shops.",G+"autonomousboatservice.com/","autonomousboatservice.com coming soon"),
  ("Cape Island AI","Automate your business with AI.",G+"cape-island-ai/",None),
  ("Cape Edge","Pre-filled peptide pens for licensed practices.",G+"cape-edge/",None),
  ("Peptide Certification","Peptide Certification Level 1 course.",G+"peptide-cert/",None),
  ("Tanorama Falmouth","Tanning salon at 365 Main St, Falmouth, MA.",G+"tanorama-falmouth/",None),
  ("Paws NH","Pet services across New Hampshire, in one place.",G+"pawsnh.com/","pawsnh.com coming soon"),
 ]),
 ("Apps & Projects","ink",[
  ("Social Footprint","See and tidy up your social media footprint.","https://social-footprint-app.vercel.app",None),
  ("Dark Web Check","Public data-breach lookup.","https://dark-web-check.vercel.app",None),
  ("Beyond the Wall","Story game: The First Hard Mile.","https://beyond-the-wall-3d.vercel.app",None),
 ]),
]
kava=[("kapekava.com","Cape Kava","Kava culture, coming to Cape Cod."),("kavalounges.com","Kava Lounges","A laid-back kava lounge concept for the Cape."),("kavaretreats.com","Kava Retreats","Slow weekends inspired by island kava circles."),("kavachef.com","Kava Chef","Food pairings and kitchen ideas for kava nights."),("kavasushi.com","Kava Sushi","Where a kava bowl meets a sushi bar."),("kavacooking.com","Kava Cooking","Recipes, pairings and kitchen stories."),("kavasoup.com","Kava Soup","Warm bowls and kava nights for Cape Cod winters."),("kavavacations.com","Kava Vacations","Travel ideas for the islands where kava began."),("kavacharities.com","Kava Charities","Kava nights that give back."),("kavagolfing.com","Kava Golfing","The 19th hole, island style."),("kavamodeling.com","Kava Modeling","Models, photographers and creators.")]
groups.append(("Kava domain network (for sale)","kava",[(n,d+" Domain for sale.",G+dom+"/",dom+" coming soon") for dom,n,d in kava]))
e=html.escape
out=[]; data=[]
for title,tone,items in groups:
  out.append(f'<section class="group group--{tone}"><h2>{e(title)} <span class="count">{len(items)}</span></h2><div class="grid">')
  for n,d,u,note in items:
    data.append(dict(group=title,name=n,url=u,note=note))
    sub = f'<span class="card__note">{e(note)}</span>' if note else f'<span class="card__url">{e(u.split("//")[1].rstrip("/"))}</span>'
    out.append(f'<a class="card" href="{e(u)}" target="_blank" rel="noopener"><span class="card__name">{e(n)}</span><span class="card__line">{e(d)}</span>{sub}<span class="card__go" aria-hidden="true">Visit &rarr;</span></a>')
  out.append('</div></section>')
total=sum(len(i) for _,_,i in groups)
nav=''.join(f'<a href="#g{i}">{e(t)}</a>' for i,(t,_,_) in enumerate(groups))
body='\n'.join(out)
body=body.replace('<section class="group','<section id="gX" class="group')
for i in range(len(groups)): body=body.replace('id="gX"',f'id="g{i}"',1)
page=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>All Sites | Platinum Limo network</title>
<meta name="description" content="Every site in the Platinum Limo network: community, food, business, apps and domains.">
<link rel="stylesheet" href="styles.css"></head>
<body><div class="page">
<header class="header"><p class="eyebrow">Directory</p><h1>All our sites</h1>
<p class="subline">{total} sites in one place. Pick the one you need.</p><nav class="jump">{nav}</nav></header>
<main>
{body}
</main>
<footer class="footer"><p>Platinum Limo network &middot; Cape Cod, MA &middot; Updated October 2026</p><p class="small">Kava domains are for sale: each page links to its Afternic listing.</p></footer>
</div></body></html>'''
open("index.html","w").write(page)
json.dump(data,open("sites.json","w"),indent=1)
print(total)
