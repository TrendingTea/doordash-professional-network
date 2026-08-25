import os
from flask import Flask,jsonify,redirect,render_template,request,url_for
from db import Store
app=Flask(__name__); store=Store(os.environ.get('PRO_NETWORK_DB','instance/pro-network.sqlite3'))
def yn(name,nullable=False):
    v=request.form.get(name)
    if nullable and v=='na': return None
    return 1 if v=='yes' else 0
@app.get('/')
def home(): return render_template('index.html',summary=store.pilot_summary())
@app.get('/merchant')
def merchant(): return render_template('merchant.html',deliveries=store.unrated()[:50])
@app.get('/merchant/feedback/<int:delivery_id>')
def feedback_form(delivery_id):
    with store.connect() as c: r=c.execute('SELECT d.*,m.name merchant_name,m.location_name,da.display_name FROM deliveries d JOIN merchants m ON m.id=d.merchant_id JOIN dashers da ON da.id=d.dasher_id WHERE d.id=?',(delivery_id,)).fetchone()
    return render_template('feedback.html',delivery=dict(r) if r else None)
@app.post('/merchant/feedback/<int:delivery_id>')
def submit_feedback(delivery_id):
    store.submit_feedback(delivery_id,{'well_presented':yn('well_presented'),'insulated_bag':yn('insulated_bag',True),'respectful':yn('respectful'),'followed_instructions':yn('followed_instructions'),'handled_carefully':yn('handled_carefully'),'efficient_interaction':yn('efficient_interaction'),'recognition':request.form.get('recognition',''),'manager_note':request.form.get('manager_note','')}); return redirect(url_for('merchant'))
@app.get('/dashers')
def dashers(): return render_template('dashers.html',dashers=store.dashers())
@app.get('/dasher/<int:did>')
def dasher(did): return render_template('dasher.html',dasher=store.get_dasher(did),metrics=store.metrics(did))
@app.get('/card/<int:did>')
def card(did):
    d=store.get_dasher(did)
    if not d or not d['public_profile']: return 'Profile unavailable',404
    return render_template('card.html',dasher=d,metrics=store.metrics(did))
@app.get('/analytics')
def analytics(): return render_template('analytics.html',summary=store.pilot_summary(),dashers=[(d,store.metrics(d['id'])) for d in store.dashers()])
@app.get('/api/pilot')
def api_pilot(): return jsonify(store.pilot_summary())
@app.get('/health')
def health(): return jsonify(status='ok',product='DoorDash Professional Network Proposal',independent=True)
if __name__=='__main__': app.run(host='0.0.0.0',port=int(os.environ.get('PORT','8022')),debug=False)
