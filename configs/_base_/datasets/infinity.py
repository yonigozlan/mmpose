dataset_info = dict(
    dataset_name="infinity",
    keypoint_info={
        0: dict(name="nose", id=0, color=[51, 153, 255], type="upper", swap=""),
        1: dict(
            name="left_eye", id=1, color=[51, 153, 255], type="upper", swap="right_eye"
        ),
        2: dict(
            name="right_eye", id=2, color=[51, 153, 255], type="upper", swap="left_eye"
        ),
        3: dict(
            name="left_ear", id=3, color=[51, 153, 255], type="upper", swap="right_ear"
        ),
        4: dict(
            name="right_ear", id=4, color=[51, 153, 255], type="upper", swap="left_ear"
        ),
        5: dict(
            name="left_shoulder",
            id=5,
            color=[0, 255, 0],
            type="upper",
            swap="right_shoulder",
        ),
        6: dict(
            name="right_shoulder",
            id=6,
            color=[255, 128, 0],
            type="upper",
            swap="left_shoulder",
        ),
        7: dict(
            name="left_elbow", id=7, color=[0, 255, 0], type="upper", swap="right_elbow"
        ),
        8: dict(
            name="right_elbow",
            id=8,
            color=[255, 128, 0],
            type="upper",
            swap="left_elbow",
        ),
        9: dict(
            name="left_wrist", id=9, color=[0, 255, 0], type="upper", swap="right_wrist"
        ),
        10: dict(
            name="right_wrist",
            id=10,
            color=[255, 128, 0],
            type="upper",
            swap="left_wrist",
        ),
        11: dict(
            name="left_hip", id=11, color=[0, 255, 0], type="lower", swap="right_hip"
        ),
        12: dict(
            name="right_hip", id=12, color=[255, 128, 0], type="lower", swap="left_hip"
        ),
        13: dict(
            name="left_knee", id=13, color=[0, 255, 0], type="lower", swap="right_knee"
        ),
        14: dict(
            name="right_knee",
            id=14,
            color=[255, 128, 0],
            type="lower",
            swap="left_knee",
        ),
        15: dict(
            name="left_ankle",
            id=15,
            color=[0, 255, 0],
            type="lower",
            swap="right_ankle",
        ),
        16: dict(
            name="right_ankle",
            id=16,
            color=[255, 128, 0],
            type="lower",
            swap="left_ankle",
        ),
        17: dict(
            name="sternum",
            id=17,
            color=[255, 0, 255],
            type="upper",
            swap="",
        ),
        18: dict(
            name="rshoulder",
            id=18,
            color=[255, 0, 255],
            type="upper",
            swap="lshoulder",
        ),
        19: dict(
            name="lshoulder",
            id=19,
            color=[255, 0, 255],
            type="upper",
            swap="rshoulder",
        ),
        20: dict(
            name="r_lelbow",
            id=20,
            color=[255, 0, 255],
            type="upper",
            swap="l_lelbow",
        ),
        21: dict(
            name="l_lelbow",
            id=21,
            color=[255, 0, 255],
            type="upper",
            swap="r_lelbow",
        ),
        22: dict(
            name="r_melbow",
            id=22,
            color=[255, 0, 255],
            type="upper",
            swap="l_melbow",
        ),
        23: dict(
            name="l_melbow",
            id=23,
            color=[255, 0, 255],
            type="upper",
            swap="r_melbow",
        ),
        24: dict(
            name="r_mwrist",
            id=24,
            color=[255, 0, 255],
            type="upper",
            swap="l_mwrist",
        ),
        25: dict(
            name="l_mwrist",
            id=25,
            color=[255, 0, 255],
            type="upper",
            swap="r_mwrist",
        ),
        26: dict(
            name="r_lwrist",
            id=26,
            color=[255, 0, 255],
            type="upper",
            swap="l_lwrist",
        ),
        27: dict(
            name="l_lwrist",
            id=27,
            color=[255, 0, 255],
            type="upper",
            swap="r_lwrist",
        ),
        28: dict(
            name="r_ASIS",
            id=28,
            color=[255, 0, 255],
            type="lower",
            swap="l_ASIS",
        ),
        29: dict(
            name="l_ASIS",
            id=29,
            color=[255, 0, 255],
            type="lower",
            swap="r_ASIS",
        ),
        30: dict(
            name="r_PSIS",
            id=30,
            color=[255, 0, 255],
            type="lower",
            swap="l_PSIS",
        ),
        31: dict(
            name="l_PSIS",
            id=31,
            color=[255, 0, 255],
            type="lower",
            swap="r_PSIS",
        ),
        32: dict(
            name="r_knee",
            id=32,
            color=[255, 0, 255],
            type="lower",
            swap="l_knee",
        ),
        33: dict(
            name="l_knee",
            id=33,
            color=[255, 0, 255],
            type="lower",
            swap="r_knee",
        ),
        34: dict(
            name="r_mknee",
            id=34,
            color=[255, 0, 255],
            type="lower",
            swap="l_mknee",
        ),
        35: dict(
            name="l_mknee",
            id=35,
            color=[255, 0, 255],
            type="lower",
            swap="r_mknee",
        ),
        36: dict(
            name="r_ankle",
            id=36,
            color=[255, 0, 255],
            type="lower",
            swap="l_ankle",
        ),
        37: dict(
            name="l_ankle",
            id=37,
            color=[255, 0, 255],
            type="lower",
            swap="r_ankle",
        ),
        38: dict(
            name="r_mankle",
            id=38,
            color=[255, 0, 255],
            type="lower",
            swap="l_mankle",
        ),
        39: dict(
            name="l_mankle",
            id=30,
            color=[255, 0, 255],
            type="lower",
            swap="r_mankle",
        ),
        40: dict(
            name="r_5meta",
            id=40,
            color=[255, 0, 255],
            type="lower",
            swap="l_5meta",
        ),
        41: dict(
            name="l_5meta",
            id=41,
            color=[255, 0, 255],
            type="lower",
            swap="r_5meta",
        ),
        42: dict(
            name="r_toe",
            id=42,
            color=[255, 0, 255],
            type="lower",
            swap="l_toe",
        ),
        43: dict(
            name="l_toe",
            id=43,
            color=[255, 0, 255],
            type="lower",
            swap="r_toe",
        ),
        44: dict(
            name="r_big_toe",
            id=44,
            color=[255, 0, 255],
            type="lower",
            swap="l_big_toe",
        ),
        45: dict(
            name="l_big_toe",
            id=45,
            color=[255, 0, 255],
            type="lower",
            swap="r_big_toe",
        ),
        46: dict(
            name="l_calc",
            id=46,
            color=[255, 0, 255],
            type="lower",
            swap="r_calc",
        ),
        47: dict(
            name="r_calc",
            id=47,
            color=[255, 0, 255],
            type="upper",
            swap="l_calc",
        ),
        48: dict(
            name="r_bpinky",
            id=48,
            color=[255, 0, 255],
            type="upper",
            swap="l_bpinky",
        ),
        49: dict(
            name="l_bpinky",
            id=49,
            color=[255, 0, 255],
            type="upper",
            swap="r_bpinky",
        ),
        50: dict(
            name="r_tpinky",
            id=50,
            color=[255, 0, 255],
            type="upper",
            swap="l_tpinky",
        ),
        51: dict(
            name="l_tpinky",
            id=51,
            color=[255, 0, 255],
            type="upper",
            swap="r_tpinky",
        ),
        52: dict(
            name="r_bindex",
            id=52,
            color=[255, 0, 255],
            type="upper",
            swap="l_bindex",
        ),
        53: dict(
            name="l_bindex",
            id=53,
            color=[255, 0, 255],
            type="upper",
            swap="r_bindex",
        ),
        54: dict(
            name="r_tindex",
            id=54,
            color=[255, 0, 255],
            type="upper",
            swap="l_tindex",
        ),
        55: dict(
            name="l_tindex",
            id=55,
            color=[255, 0, 255],
            type="upper",
            swap="r_tindex",
        ),
        56: dict(
            name="r_tmiddle",
            id=56,
            color=[255, 0, 255],
            type="upper",
            swap="l_tmiddle",
        ),
        57: dict(
            name="l_tmiddle",
            id=57,
            color=[255, 0, 255],
            type="upper",
            swap="r_tmiddle",
        ),
        58: dict(
            name="r_tring",
            id=58,
            color=[255, 0, 255],
            type="upper",
            swap="l_tring",
        ),
        59: dict(
            name="l_tring",
            id=59,
            color=[255, 0, 255],
            type="upper",
            swap="r_tring",
        ),
        60: dict(
            name="r_bthumb",
            id=60,
            color=[255, 0, 255],
            type="upper",
            swap="l_bthumb",
        ),
        61: dict(
            name="l_bthumb",
            id=61,
            color=[255, 0, 255],
            type="upper",
            swap="r_bthumb",
        ),
        62: dict(
            name="r_tthumb",
            id=62,
            color=[255, 0, 255],
            type="upper",
            swap="l_tthumb",
        ),
        63: dict(
            name="l_tthumb",
            id=63,
            color=[255, 0, 255],
            type="upper",
            swap="r_tthumb",
        ),
        64: dict(
            name="C7",
            id=64,
            color=[255, 0, 255],
            type="upper",
            swap="",
        ),
        65: dict(
            name="L2",
            id=65,
            color=[255, 0, 255],
            type="lower",
            swap="",
        ),
        66: dict(
            name="T11",
            id=66,
            color=[255, 0, 255],
            type="upper",
            swap="",
        ),
        67: dict(
            name="T6",
            id=67,
            color=[255, 0, 255],
            type="upper",
            swap="",
        ),
    },
    skeleton_info={
        0: dict(link=("left_ankle", "left_knee"), id=0, color=[0, 255, 0]),
        1: dict(link=("left_knee", "left_hip"), id=1, color=[0, 255, 0]),
        2: dict(link=("right_ankle", "right_knee"), id=2, color=[255, 128, 0]),
        3: dict(link=("right_knee", "right_hip"), id=3, color=[255, 128, 0]),
        4: dict(link=("left_hip", "right_hip"), id=4, color=[51, 153, 255]),
        5: dict(link=("left_shoulder", "left_hip"), id=5, color=[51, 153, 255]),
        6: dict(link=("right_shoulder", "right_hip"), id=6, color=[51, 153, 255]),
        7: dict(link=("left_shoulder", "right_shoulder"), id=7, color=[51, 153, 255]),
        8: dict(link=("left_shoulder", "left_elbow"), id=8, color=[0, 255, 0]),
        9: dict(link=("right_shoulder", "right_elbow"), id=9, color=[255, 128, 0]),
        10: dict(link=("left_elbow", "left_wrist"), id=10, color=[0, 255, 0]),
        11: dict(link=("right_elbow", "right_wrist"), id=11, color=[255, 128, 0]),
        12: dict(link=("left_eye", "right_eye"), id=12, color=[51, 153, 255]),
        13: dict(link=("nose", "left_eye"), id=13, color=[51, 153, 255]),
        14: dict(link=("nose", "right_eye"), id=14, color=[51, 153, 255]),
        15: dict(link=("left_eye", "left_ear"), id=15, color=[51, 153, 255]),
        16: dict(link=("right_eye", "right_ear"), id=16, color=[51, 153, 255]),
        17: dict(link=("left_ear", "left_shoulder"), id=17, color=[51, 153, 255]),
        18: dict(link=("right_ear", "right_shoulder"), id=18, color=[51, 153, 255]),
    },
    joint_weights=[
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.2,
        1.2,
        1.5,
        1.5,
        1.0,
        1.0,
        1.2,
        1.2,
        1.5,
        1.5,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
    ],
    sigmas=[
        0.026,
        0.025,
        0.025,
        0.035,
        0.035,
        0.079,
        0.079,
        0.072,
        0.072,
        0.062,
        0.062,
        0.107,
        0.107,
        0.087,
        0.087,
        0.089,
        0.089,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
    ],
)
