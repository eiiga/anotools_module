def cal_velocity(v0, a, t):
    """ 速度を求める
    :param v0: 初速度 m/s
    :param a: 加速度 m/s**2
    :param t: 時刻 s
    :return: 速度（v） m/s
    """
    return v0 + (a * t)


def cal_displacement(v0, t, a):
    """ 変位を求める
    :param v0: 初速度 m/s
    :param t: 時刻 s
    :param a: 加速度 m/s**2
    :return: 変位（x） m
    """
    return (v0 * t) + ((a * t ** 2) / 2)


def cal_displacement_ver2(v, v0, a):
    """ 変位を求める（ver2）
    :param v: 速度 m/s
    :param v0: 初速度 m/s
    :param a: 加速度 m/s**2
    :return: 変位（x） m
    """
    if a == 0:
        raise ValueError("a must not be zero to avoid division by zero.")
    x = (v ** 2 - v0 ** 2) / (2 * a)
    return x


if __name__ == '__main__':
    v0 = 4.0
    a = - 0.50

    print('===== 問1 =====')
    t_q1 = 2.0
    print(f'速度: {cal_velocity(v0, a, t_q1)}m/s')

    print('===== 問2 =====')
    t_q2 = 2.0
    print(f'変位: {cal_displacement(v0, t_q2, a)}m')

    print('===== 問3 =====')
    v_q3 = 0
    print(f'変位: {cal_displacement_ver2(v_q3, v0, a)}m')

    print('===== 問4 =====')
    t_q4 = 12
    print(f'速度: {cal_velocity(v0, a, t_q4)}m/s')

    print('===== 問5 =====')
    t_q5 = 12
    print(f'変位: {cal_displacement(v0, t_q5, a)}m')
