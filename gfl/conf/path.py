import os


home_dir = os.path.expanduser("~")
gfl_dir = os.path.join(home_dir, ".gfl")
key_file = os.path.join(gfl_dir, "key.json")

data_dir = "res"
job_dir = os.path.join(data_dir, "job")
model_dir = os.path.join(data_dir, "model")
client_dir = os.path.join(data_dir, "client")
server_dir = os.path.join(data_dir, "server")

os.makedirs(gfl_dir, exist_ok=True)
os.makedirs(data_dir, exist_ok=True)


