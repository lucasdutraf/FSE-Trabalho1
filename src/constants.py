LOCAL_IP = "127.0.0.1"
CROSS_1_PORT = 10251
CROSS_2_PORT = 10252
MAIN_SERVER_PORT = 10253

TRAFFIC_LIGHTS = {
    "C_1": {
        "1": {
            "green": 1,
            "yellow": 26,
            "red": 21,
        },
        "2": {
            "green": 20,
            "yellow": 16,
            "red": 12,
        }
    },
    "C_2": {
        "1": {
            "green": 2,
            "yellow": 3,
            "red": 11,
        },
        "2": {
            "green": 0,
            "yellow": 5,
            "red": 6,
        }
    }
}

LIGHTS_TIME_COUNT = {
    "green": {
        "1": {
            "min": 10,
            "max": 20,
        },
        "2": {
            "min": 5,
            "max": 10,
        }
    },
    "yellow": {
        "1": {
            "min": 3,
            "max": 3,
        },
        "2": {
            "min": 3,
            "max": 3,
        }
    },
    "red": {
        "1": {
            "min": 5,
            "max": 10,
        },
        "2": {
            "min": 10,
            "max": 20,
        },
        "total": 1,
    },
}