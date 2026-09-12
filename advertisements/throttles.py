from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class AdvertisementAnonRateThrottle(AnonRateThrottle):
    rate = '10/min'

class AdvertisementUserRateThrottle(UserRateThrottle):
    rate = '20/min'