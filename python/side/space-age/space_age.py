class SpaceAge(object):
    """ Provides the age on other planets """

    EARTH_YEAR_SECONDS = 31557600
    EARTH_FACTOR = 1.0
    MERCURY_FACTOR = 0.2408467
    VENUS_FACTOR = 0.61519726
    MARS_FACTOR = 1.8808158
    JUPITER_FACTOR = 11.862615
    SATURN_FACTOR = 29.447498
    URANUS_FACTOR = 84.016846
    NEPTUNE_FACTOR = 164.79132


    def __init__(self, seconds: int) -> int:
        self.seconds = seconds

    def on_mercury(self) -> float:
        elapsed_time = self._elapsed_time(self.MERCURY_FACTOR)
        return round(elapsed_time, 2)

    def on_venus(self) -> float:
        elapsed_time = self._elapsed_time(self.VENUS_FACTOR)
        return round(elapsed_time, 2)

    def on_earth(self) -> float:
        elapsed_time = self._elapsed_time(self.EARTH_FACTOR)
        return round(elapsed_time, 2)

    def on_mars(self) -> float:
        elapsed_time = self._elapsed_time(self.MARS_FACTOR)
        return round(elapsed_time, 2)

    def on_jupiter(self) -> float:
        elapsed_time = self._elapsed_time(self.JUPITER_FACTOR)
        return round(elapsed_time, 2)

    def on_saturn(self) -> float:
        elapsed_time = self._elapsed_time(self.SATURN_FACTOR)
        return round(elapsed_time, 2)

    def on_uranus(self) -> float:
        elapsed_time = self._elapsed_time(self.URANUS_FACTOR)
        return round(elapsed_time, 2)

    def on_neptune(self) -> float:
        elapsed_time = self._elapsed_time(self.NEPTUNE_FACTOR)
        return round(elapsed_time, 2)

    def _elapsed_time(self, planet_factor: float) -> float:
        return self.seconds / (self.EARTH_YEAR_SECONDS * planet_factor)
