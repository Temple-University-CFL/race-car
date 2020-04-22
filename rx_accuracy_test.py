import json
import pandas as pd

from av_nn_tools import NNTools
from av_parse_data import ParseData


TEST_LIST = "data/list/test.csv"
SETTINGS = "data/set_accuracy_test.json"


data = pd.read_csv(TEST_LIST)
parsedata = ParseData()
with open(SETTINGS) as fp:
    content = json.load(fp)
    
    shape = content['shape']
    servo_pred = NNTools(content["servo_setting"])
    motor_pred = NNTools(content["motor_setting"])
    servo_pred.load_model(content['servo_model'])
    motor_pred.load_model(content['motor_model'])

servo_count = 0
motor_count = 0

for index in range(len(data)):
    _,servo,motor = parsedata.parse_data(data["image"][index])
    
    pred_servo =  servo_pred.predict(data["image"][index])
    pred_motor =  motor_pred.predict(data["image"][index])
    
    if abs(servo - pred_servo) <= 1:
        servo_count += 1
    # if servo == 15:
    #     if servo - pred_servo == 0:
    #         servo_count += 1
    # elif (servo-15)*(pred_servo-15) > 0:
    #     servo_count += 1
    
    if abs(motor - pred_motor) <= 1:
        motor_count += 1
    
    if (index+1)%100 == 0:
        print("[%5d] servo: %2.2f motor: %2.2f" % \
              (index+1, 100*servo_count/(index+1), 100*motor_count/(index+1)))
        
print("servo: %2.2f motor: %2.2f" % (100*servo_count/(index+1), \
                                     100*motor_count/(index+1)))
    