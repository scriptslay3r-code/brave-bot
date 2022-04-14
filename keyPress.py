from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
#https://github.com/andohuman/pyKey

'''pressKey("LCTRL") 
pressKey("LALT")
pressKey("t")

press("LCTRL","LALT","t")
releaseKey("LCTRL")
releaseKey("LALT")
releaseKey("t")

'''
press("LCTRL","LALT","t")
terminal = ["LCTRL","LALT","t"]
print("Sequence next")
print(terminal)

sendSequence(seq=terminal)

