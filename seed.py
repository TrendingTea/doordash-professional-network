import random, os
from db import Store
path='instance/pro-network.sqlite3'
if os.path.exists(path): os.remove(path)
s=Store(path); random.seed(42)
with s.connect() as c:
    dashers=[('Alex R.','Independent Delivery Professional','4+ years in local delivery and customer service.','Customer Service, Logistics, Technology, Sales','Continuing education','Operations, Technical Support, Software Development, Sales',1),('Jordan M.','Delivery & Hospitality Professional','Reliable local delivery professional focused on restaurant partnerships.','Hospitality, Logistics, Communication','Associate coursework','Restaurant Operations, Account Management',1),('Taylor S.','Independent Courier','Delivery professional building transferable operational skills.','Routing, Customer Service, Safety','High school diploma','Operations, Logistics',1)]
    c.executemany('INSERT INTO dashers(display_name,headline,bio,skills,education,career_interests,public_profile) VALUES(?,?,?,?,?,?,?)',dashers)
    for i in range(1,51): c.execute('INSERT INTO merchants(name,location_name,city,pilot_group) VALUES(?,?,?,?)',("McDonald's",f'Pilot Restaurant {i:02d}','Milwaukee, WI','synthetic-mcdonalds'))
    merchants=[r['id'] for r in c.execute('SELECT id FROM merchants')]; dashers=[r['id'] for r in c.execute('SELECT id FROM dashers')]
    for i in range(1,1001):
        mid=random.choice(merchants); did=random.choice(dashers); pickup=max(1.5,random.gauss(7.0,2.0))
        delivery_id=c.execute('INSERT INTO deliveries(external_order_ref,merchant_id,dasher_id,pickup_minutes) VALUES(?,?,?,?)',(f'SYN-{i:05d}',mid,did,pickup)).lastrowid
        if random.random()<.72:
            yes=lambda p:1 if random.random()<p else 0
            c.execute('INSERT INTO feedback(delivery_id,well_presented,insulated_bag,respectful,followed_instructions,handled_carefully,efficient_interaction,recognition,manager_note) VALUES(?,?,?,?,?,?,?,?,?)',(delivery_id,yes(.96),yes(.94),yes(.98),yes(.96),yes(.97),yes(.95),random.choice(['Professional','Prepared','Efficient','Helpful','Excellent communication']),'') )
print('Seeded synthetic pilot: 50 restaurants, 3 Dashers, 1,000 deliveries.')
