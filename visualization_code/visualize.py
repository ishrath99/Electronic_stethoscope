import serial
import matplotlib.pyplot as plt
from collections import deque
from scipy.io import wavfile

ser = serial.Serial('COM3', 9600)  # Arduino's serial COM port

plt.ion()  # Turn on interactive mode for live plotting

sample_rate = 800

TIME_INTERVAL = 1 / sample_rate  # Time interval between data points (in seconds)
MAX_DATA_POINTS = int(TIME_INTERVAL * 4e6)  # Maximum number of data points to display

data = deque(maxlen=MAX_DATA_POINTS)

# L = len(audio_data)
i = 0

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            try:
                voltage = float(line)
                data.append(voltage)

                # if i == L-1:
                #     i = 0
                # else:
                #     i += 1

                plt.clf()
                plt.plot(list(data))
                plt.xlabel('Samples')
                plt.ylabel('Voltage (V)')
                plt.grid(True)
                plt.pause(TIME_INTERVAL / 100)
                
            except ValueError:
                print(f"Invalid data received: {line}")

except KeyboardInterrupt:
    pass

# ser.close()
plt.ioff()
