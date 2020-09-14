def calculate_dose(weight, time, total_doze_24):
    """
    :param weight: weight of user (kg)
    :param time: time period has passed from the previous dose (full hours)
    :param total_doze_24: total dose for the last 24 hours (mg)
    :return: recommended dóage
    """
    MAX_DOZE = 4000
    if 24 > time > 6:
        doze = MAX_DOZE - total_doze_24
    if time == 6 or time == 24:
        doze = 15*weight
    if time < 6:
        doze = 0
    return doze

def main():
    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)

    weight = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the previous dose (full hours): "))
    total_doze_24 = int(input("The total dose for the last 24 hours (mg): "))
    print(f"The amount of Parasetamol to give to the patient: {calculate_dose(weight, time, total_doze_24)}")

if __name__ == "__main__":
  main()
