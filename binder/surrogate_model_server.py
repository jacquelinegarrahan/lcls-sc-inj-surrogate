from lume_epics.epics_server import Server
from binder.surrogate_model import Model
from lume_model.utils import load_variables
import argparse
import tensorflow as tf

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

parser = argparse.ArgumentParser()
parser.add_argument('--no-monitor', help='Run server without monitor.', action='store_false', dest="monitor", default=True)
args = parser.parse_args()
monitor = args.monitor

variable_file = "binder/files/surrogate_model_variables.pickle"
input_variables, output_variables = load_variables(variable_file)

prefix = "test"
model_file = "binder/files/CNN_081120_SurrogateModel.h5"
model_kwargs= {"model_file": model_file, "input_variables": input_variables, "output_variables": output_variables}
server = Server(Model, input_variables, output_variables, prefix, model_kwargs=model_kwargs)

server.start(monitor=monitor) # monitor = False does not loop in main thread
