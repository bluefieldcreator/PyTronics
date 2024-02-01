import math

def sound_pressure_loss(pressure: int, wattage: int, distance: int) -> int:
    """
    :rtype int Total pressure loss
    :param pressure: Pressure of the speaker 
    :param wattage: Wattage of the speaker
    :param distance: Distance traveled by sound
    """
    return round(pressure - (20 * math.log(distance, 10)) + (10 * math.log(wattage, 10)), 2)

if __name__ == "__main__":
    print(f"{sound_pressure_loss(91, 1, 8)} Db")
