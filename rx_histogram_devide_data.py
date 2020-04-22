import pandas as pd
import matplotlib.pyplot as plt
from av_parse_data import ParseData

LIST_FILE = "data/list/train.csv"


#------------------------------------------------------------------------------
data = pd.read_csv(LIST_FILE)
parsedata = ParseData()

image = []
servo = []
motor = []
for index in range(len(data)):
    _,ser,mot = parsedata.parse_data(data["image"][index])
    servo.append(ser)
    motor.append(mot)

plt.figure()
plt.hist(servo, bins=11)
plt.title("Histogram of Servo Data")
plt.savefig("curves/Histogram for Servo Dataset.png")

plt.figure()
plt.hist(motor, bins=11)
plt.title("Histogram of Motor Data")
plt.savefig("curves/Histogram for Motor Dataset.png")


#------------------------------------------------------------------------------
all_10 = []
all_11 = []
all_12 = []
all_13 = []
all_14 = []
all_15 = []
all_16 = []
all_17 = []
all_18 = []
all_19 = []
all_20 = []
for index in range(len(servo)):
    if servo[index] == 10:
        all_10.append(data["image"][index])
    elif servo[index] == 11:
        all_11.append(data["image"][index])
    elif servo[index] == 12:
        all_12.append(data["image"][index])
    elif servo[index] == 13:
        all_13.append(data["image"][index])
    elif servo[index] == 14:
        all_14.append(data["image"][index])
    elif servo[index] == 15:
        all_15.append(data["image"][index])
    elif servo[index] == 16:
        all_16.append(data["image"][index])
    elif servo[index] == 17:
        all_17.append(data["image"][index])
    elif servo[index] == 18:
        all_18.append(data["image"][index])
    elif servo[index] == 19:
        all_19.append(data["image"][index])
    elif servo[index] == 20:
        all_20.append(data["image"][index])

# write data
# pd.DataFrame(all_10, columns=["image"]).to_csv("data/list/all_10.csv", index=False)
# pd.DataFrame(all_11, columns=["image"]).to_csv("data/list/all_11.csv", index=False)
# pd.DataFrame(all_12, columns=["image"]).to_csv("data/list/all_12.csv", index=False)
# pd.DataFrame(all_13, columns=["image"]).to_csv("data/list/all_13.csv", index=False)
# pd.DataFrame(all_14, columns=["image"]).to_csv("data/list/all_14.csv", index=False)
# pd.DataFrame(all_15, columns=["image"]).to_csv("data/list/all_15.csv", index=False)
# pd.DataFrame(all_16, columns=["image"]).to_csv("data/list/all_16.csv", index=False)
# pd.DataFrame(all_17, columns=["image"]).to_csv("data/list/all_17.csv", index=False)
# pd.DataFrame(all_18, columns=["image"]).to_csv("data/list/all_18.csv", index=False)
# pd.DataFrame(all_19, columns=["image"]).to_csv("data/list/all_19.csv", index=False)
# pd.DataFrame(all_20, columns=["image"]).to_csv("data/list/all_20.csv", index=False)