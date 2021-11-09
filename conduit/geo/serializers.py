# coding: utf-8

from marshmallow import Schema, fields, pre_load, post_dump

class GeolocationSchema(Schema):
    eid = fields.Str()
    entity = fields.Str()
    lat = fields.Decimal()
    lon = fields.Decimal()
    geolocation = fields.Nested('self', exclude=('geolocation',), default=True, load_only=True)

    @pre_load
    def make_geo(self, data, **kwargs):
        return data['geolocation']

    @post_dump
    def dump_geo(self, data, **kwargs):
        return {'geolocation': data}

    class Meta:
        strict = True


geolocation_schema = GeolocationSchema()
geolocations_schema = GeolocationSchema(many=True)
