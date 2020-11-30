import importlib
import os

import torch

from gfl import device
from gfl.conf import job_dir
from gfl.entity import Job
from gfl.conf.fl_config import TrainConfig


class Trainer(object):

    def __init__(self, job: Job):
        super(Trainer, self).__init__()
        self.job = job

    def _parse_job(self, job: Job):
        job_path = os.path.join(job_dir, job.job_id)
        model_module_pack = job_path.replace("/", ".") + ".fl_model"
        model_module = importlib.import_module(model_module_pack)
        self.model = model_module.__getattribute__(job.train_config)




def epoch_train(self, dataloader, model, optimizer, scheduler, criterion):
    epoch_loss = 0.0
    iter_num = 0

    correct = 0
    total = 0

    model = model.to(device())

    for i, data in enumerate(dataloader, 0):
        inputs, labels = data
        inputs = inputs.to(device())
        labels = labels.to(device())

        if torch.is_grad_enabled():
            optimizer.zero_grad()

        outputs = model(inputs)

        loss = criterion(outputs, labels)

        if torch.is_grad_enabled():
            loss.backward()

            optimizer.step()

        epoch_loss += loss.item()
        iter_num += 1

        _, predicted = torch.max(outputs, 1)
        c = (predicted == labels).squeeze()
        for i, lb in enumerate(labels):
            correct += c[i].item()
            total += 1

    return epoch_loss / iter_num, correct / total