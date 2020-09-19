"""
COMP.CS.100 Programming 1
Hang Nguyen, hang.t.nguyen@tuni.fi, student id K429778
Triangle's angle
"""
def calculate_angle(s1,s2=90):
    """
    Calculate the magnitude of 3rd angle based the other 2 angles
    :param s1: magnitude of 1st angle
    :param s2: magnitude of 2nd angle
    :return: 3rd angle magnitude
    """
    if s2 != 90:
        s3 = 180-s1-s2
        return s3
    else:
        s3 = 90 - s1
        return s3
