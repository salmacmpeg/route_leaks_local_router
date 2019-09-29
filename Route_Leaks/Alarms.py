import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration1 = 500  # Set Duration To 1000 ms == 1 second
duration2 = 1000  # Set Duration To 1000 ms == 1 second
duration3 = 1500  # Set Duration To 1000 ms == 1 second
#-----------------------------------------------------------------------------------#
# this function makes a beep sound for short/long/verylong durations
def alarm(s):
    if s=="short":
        winsound.Beep(frequency, duration1)
    elif s=="long":
        winsound.Beep(frequency, duration2)
    else :
        winsound.Beep(frequency, duration3)
