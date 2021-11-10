from decimal import Decimal

from flask import url_for

def _create_geolocation(testapp, **kwargs):
    return testapp.post_json(url_for('geo.make_geolocation'), {
        "geo": {
            "entity": "entity",
            "eid": 1234,
            "point_lat": Decimal(75.85),
            "point_lon": Decimal(75.85)
        }}, **kwargs)

class TestGeolocation:

    def test_make_geolocation(self, testapp):
        resp = _create_geolocation(testapp)
        assert resp.json['geo']['eid'] == 1234
        assert resp.json['geo']['entity'] == "entity"
