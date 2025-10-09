# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    },
    "Acamar": {
        "RA": "02h 58m 15.7s",
        "Dec": "−40° 18′ 16.839″",
        "Magnitude": 3.18,
        "Spectral Type": "A3IV-V"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def name_lister(dict):
    for key in dict:
        print(f"{key}")
name_lister(targets)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def spectral_type_lister(dict):
    for key in dict:        
        print(f"{key}: {dict[key]["Spectral Type"]}")
spectral_type_lister(targets)
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def conditional_magnitude_lister(dict):
    for key in dict:
        if dict[key]["Magnitude"] >= 0.1:        
            print(f"{key}: {dict[key]["Magnitude"]}")
conditional_magnitude_lister(targets)
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def brightest_star(dict):
    current_winner = list(dict.keys())[0]
    current_winner_magnitude = dict[current_winner]["Magnitude"]
    for key in dict:
        if dict[key]["Magnitude"] < current_winner_magnitude:
            current_winner = key
            current_winner_magnitude = dict[key]["Magnitude"]
    print(f"{current_winner}: {current_winner_magnitude}")
brightest_star(targets)
# 6) What is your favorite constellation?
# I like Orion because it's the only one I can recognize immediately