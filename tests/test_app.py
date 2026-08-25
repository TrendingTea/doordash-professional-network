import importlib

def make_app(monkeypatch,tmp_path):
    monkeypatch.setenv('PRO_NETWORK_DB',str(tmp_path/'test.sqlite3'))
    import app; importlib.reload(app); app.app.config.update(TESTING=True)
    return app.app,app.store

def test_health(monkeypatch,tmp_path):
    application,_=make_app(monkeypatch,tmp_path)
    r=application.test_client().get('/health')
    assert r.status_code==200
    assert r.json['independent'] is True

def test_feedback_flow(monkeypatch,tmp_path):
    application,store=make_app(monkeypatch,tmp_path)
    with store.connect() as c:
        did=c.execute("INSERT INTO dashers(display_name) VALUES('Test Dasher')").lastrowid
        mid=c.execute("INSERT INTO merchants(name,location_name,city) VALUES('Test Merchant','1','Milwaukee')").lastrowid
        delivery=c.execute("INSERT INTO deliveries(external_order_ref,merchant_id,dasher_id) VALUES('T-1',?,?)",(mid,did)).lastrowid
    r=application.test_client().post(f'/merchant/feedback/{delivery}',data={'well_presented':'yes','insulated_bag':'yes','respectful':'yes','followed_instructions':'yes','handled_carefully':'yes','efficient_interaction':'yes','recognition':'Professional'})
    assert r.status_code==302
    assert store.metrics(did)['professionalism']==100.0
