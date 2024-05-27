from math import sin, cos, sqrt, atan2, radians
import logging
logger = logging.getLogger('app')
from geopy.distance import geodesic



def distanceKm(point_a,point_b):
    try:
        logger.info(f'process distanceKm A{point_a} - B{point_b}')
        origin = (point_a['lat'], point_a['long'])  # (latitude, longitude) don't confuse
        dist = (point_b['lat'], point_b['long'])
        logger.info(f'process distanceKm Successful')
        return geodesic(origin, dist).kilometers
    except Exception as e:
        logger.error(f'process distanceKm Error')
        return e

      

