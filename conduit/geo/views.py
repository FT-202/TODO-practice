# coding: utf-8

import datetime as dt

from flask import Blueprint, jsonify
from flask_apispec import marshal_with, use_kwargs
from flask_jwt_extended import current_user, jwt_required, jwt_optional
from marshmallow import fields

from conduit.exceptions import InvalidUsage
from conduit.geo.models import Geolocation
from .serializers import geolocation_schema, geolocations_schema

blueprint = Blueprint('geolocations', __name__)


##########
# Geolocations
##########

@blueprint.route('/api/geo/<entity>/<eid>', methods=('POST',))
@jwt_required
# @use_kwargs(geolocation_schema)
@marshal_with(geolocation_schema)
def make_geolocation(entity, eid):
    ...


@blueprint.route('/api/geo/<entity>/<eid>', methods=('DELETE',))
@jwt_required
def delete_geolocation(entity, eid):
    ...


@blueprint.route('/api/geo/<entity>/<eid>', methods=('GET',))
@jwt_optional
@marshal_with(geolocation_schema)
def get_geolocation(entity, eid):
    ...

