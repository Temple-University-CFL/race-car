import torch
import onnx
from onnx_tf.backend import prepare

ONNX_MODEL = 'models/motor_model.onnx'
TF_MODEL = 'models/motor_model.pb'


# Load ONNX model and convert to TensorFlow format
model_onnx = onnx.load(ONNX_MODEL)

tf_rep = prepare(model_onnx)

# Export model as .pb file
tf_rep.export_graph(TF_MODEL)