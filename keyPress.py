from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
#https://github.com/andohuman/pyKey

pressKey("LCTRL")
pressKey("LALT")
pressKey("TAB")

releaseKey("LCTRL")
releaseKey("LALT")
releaseKey("TAB")


terminal = ("LCTRL","LALT","TAB")
print("Sequence next")
print(terminal)

sendSequence(seq=terminal)

