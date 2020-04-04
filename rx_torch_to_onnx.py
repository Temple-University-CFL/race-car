import torch

from racecarNet import ServoNet
from av_nn_datagen import Datagen


TORCH_MODEL = 'models/motor_model.pth'
ONNX_MODEL = 'models/motor_model.onnx'

IMAGE_FILE = "data/images/03_06_2020_0/output_0002/i0000000_s15_m15.jpg"
SHAPE = [100,100]



model_pytorch = ServoNet(SHAPE)
model_pytorch.load_state_dict(torch.load(TORCH_MODEL))

datagen_one = Datagen(shape=SHAPE)
dummy_input = datagen_one.get_image(IMAGE_FILE)
dummy_output = model_pytorch(dummy_input)

# Export to ONNX format
torch.onnx.export(model_pytorch, dummy_input, ONNX_MODEL, \
                  input_names=['test_input'], output_names=['test_output'])