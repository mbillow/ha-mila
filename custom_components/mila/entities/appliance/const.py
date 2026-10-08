# Fan Services
MAX_FAN_RPM = 2000
MIN_FAN_RPM = 500 #docs say 600, but mine seems like 500, make into an option?
# Automagic is exposed as "Auto" so HomeKit (and other bridges) recognize it as
# the purifier's automatic mode. Manual mode has no preset: it is the absence of
# one, entered by setting a speed.
PRESET_MODE_AUTO = "Auto"
PRESET_MODES = [
    PRESET_MODE_AUTO,
]

TVOC_PPB_TO_UGM3 = 3.767