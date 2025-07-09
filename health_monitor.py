import csv
import matplotlib.pyplot as plt

with open("sensor_data.txt", "r") as infile, open("health_log.csv", "w", newline="") as outfile:
    reader = infile.readlines()
    writer = csv.writer(outfile)
    writer.writerow(["Heart Rate (bpm)", "Temperature (°C)"])

    heart_rates = []
    temps = []

    for line in reader:
        hr, temp = line.strip().split(",")
        hr = int(hr)
        temp = float(temp)
        heart_rates.append(hr)
        temps.append(temp)
        writer.writerow([hr, temp])

        if hr < 60 or hr > 100:
            print(f"⚠️ Abnormal Heart Rate: {hr} bpm")
        if temp < 36.1 or temp > 37.8:
            print(f"🌡️ Temperature Out of Range: {temp} °C")

plt.plot(heart_rates, label="Heart Rate (bpm)", marker='o')
plt.plot(temps, label="Temperature (°C)", marker='x')
plt.title("Health Monitor Readings")
plt.xlabel("Reading Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
