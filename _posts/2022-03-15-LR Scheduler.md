---
layout: post
omments: true
title: "LR Scheduler"
excerpt: ""
date: 2022-03-15 18:13:09
mathjax: false
---
```python
from torch.optim.lr_scheduler import LambdaLR, MultiplicativeLR, StepLR, MultiStepLR
from torch.optim.lr_scheduler import ConstantLR, LinearLR, ExponentialLR, CosineAnnealingLR 
from torch.optim.lr_scheduler import ReduceLROnPlateau, CosineAnnealingWarmRestarts
```

```python
import matplotlib.pyplot as plt
%matplotlib inline
```

- [x] LambdaLR
- [x] MultiplicativeLR
- [x] StepLR
- [x] MultiStepLR
- [x] ConstantLR
- [x] LinearLR
- [x] ExponentialLR
- [x] CosineAnnealingLR
- [x] ReduceLROnPlateau
- [x] CosineAnnealingWarmRestarts

```python
import torch.optim as optim
from torch import nn
```

```python
class Config:
    epoch=30
    
cfg = Config()
```

## LambdaLR

���ݴ������������lambda����ѧϰ�ʵĵ�����������ѧϰ�� = ���ѧϰ�� * ������������ֵ

- lr_lambda: ����ָ��һ����������lambda��ÿ��lambdaӦ�õ���Ӧ��optimizer��ȥ���ú����������ǵ�ǰ��epoch��ֵ��

```python
def train(model, optimizer, scheduler, cfg):
    lrs = []
    lrs.append(optimizer.state_dict()['param_groups'][0]["lr"])
    for i in range(cfg.epoch):
        # train
        # valiadation
        optimizer.step()
        scheduler.step()
        lrs.append(optimizer.state_dict()['param_groups'][0]["lr"])
    return lrs

model = nn.Linear(10, 1)
```

```python
optimizer = optim.Adam(model.parameters(), 0.1)
scheduler = LambdaLR(optimizer, lr_lambda=[lambda epoch: epoch / cfg.epoch])
lrs = train(model, optimizer, scheduler, cfg)
```

```python
plt.plot(lrs)
```
<center><img src="https://cdn.jsdelivr.net/gh/AllenWrong/BlogCDN/img/output_9_1.png"/></center>

## MultiplicativeLR

�������������ķ���ֵ���е���ѧϰ�ʣ�������ѧϰ�� = ��ǰѧϰ�� * ���������ķ���ֵ�����֮ǰ��ͬ���ǣ������������ۻ��ĳ˷���

- lr_lambda: ����ָ��һ����������lambda��ÿ��lambdaӦ�õ���Ӧ��optimizer��ȥ���ú����������ǵ�ǰ��epoch��ֵ��

```python
optimizer = optim.Adam(model.parameters(), 0.1)
scheduler = MultiplicativeLR(optimizer, lr_lambda=[lambda epoch: 0.9])
lrs = train(model, optimizer, scheduler, cfg)
```

```python
plt.plot(lrs)
```

<center><img src="https://cdn.jsdelivr.net/gh/AllenWrong/BlogCDN/img/output_13_1.png"/></center>

## StepLR

ÿ����step_size��epoch��ͽ���˥����˥��������Ϊgamma��������ѧϰ�� = ��ǰ��ѧϰ�� * gamma

- step_size: ÿ����step_size��epoch����˥��

- gamma: ˥��������

```python
optimizer = optim.Adam(model.parameters(), 0.1)
scheduler = StepLR(optimizer, step_size=10, gamma=0.8)
lrs = train(model, optimizer, scheduler, cfg)
```

```python
plt.plot(lrs)
```

<center><img src="https://cdn.jsdelivr.net/gh/AllenWrong/BlogCDN/img/output_17_1.png"/></center>

## MultiStepLR

���ض���epoch������ѧϰ��˥����˥��������Ϊgamma��������ѧϰ�� = ��ǰѧϰ�� * gamma

- milestones: ����һϵ�н���˥����epoch

- gamma: ˥������

```python
optimizer = optim.Adam(model.parameters(), 0.1)
scheduler = MultiStepLR(optimizer, milestones=[3, 6, 9, 15, 20], gamma=0.5)
lrs = train(model, optimizer, scheduler, cfg)
```

```python
plt.plot(lrs)
```

<center><img src="https://cdn.jsdelivr.net/gh/AllenWrong/BlogCDN/img/output_21_1.png"/></center>

## ConstantLR

ѧϰ�ʰ�ĳ����������ָ����epoch���ٻָ���ֵ���ó���Ϊ���ѧϰ�ʳ�˥������

- factor: ˥������

- total_iters: �������ٸ�epoch

```python
optimizer = optim.Adam(model.parameters(), 0.1)
scheduler = ConstantLR(optimizer, factor=0.3, total_iters=10)
lrs = train(model, optimizer, scheduler, cfg)
```

```python
plt.plot(lrs)
```

<center><img src="https://cdn.jsdelivr.net/gh/AllenWrong/BlogCDN/img/output_25_1.png"/></center>

## LinearLR

```python

```

```python
optimizer = optim.Adam(model.parameters(), 0.1)
scheduler = LinearLR(optimizer, start_factor=0.3, end_factor=1.0, total_iters=10)
lrs = train(model, optimizer, scheduler, cfg)
```

```python
plt.plot(lrs)
```

<center><img src="https://cdn.jsdelivr.net/gh/AllenWrong/BlogCDN/img/output_29_1.png"/></center>

## ExponentialLR

ÿ��һ���ͽ���˥����˥��������Ϊgamma��������ѧϰ�� = ��ǰѧϰ�� * gamma

- gamma: ˥������

```python
optimizer = optim.Adam(model.parameters(), 0.1)
scheduler = ExponentialLR(optimizer, gamma=0.9)
lrs = train(model, optimizer, scheduler, cfg)
```

```python
plt.plot(lrs)
```

<center><img src="https://cdn.jsdelivr.net/gh/AllenWrong/BlogCDN/img/output_33_1.png"/></center>

## CosineAnnealingLR

�����˻�˥������

- T_max: lr�䶯����С��������2T_max�����Ҫ��֤�����ļ���epochѧϰ���ǲ��ϼ�С�ġ���ôT_maxӦ�����������Ĺ�ϵ��epoch = (2k+1)T_max

- eta_min: ��С��ѧϰ��

```python
optimizer = optim.Adam(model.parameters(), 1e-4)
scheduler = CosineAnnealingLR(optimizer, T_max=6, eta_min=1e-5)
lrs = train(model, optimizer, scheduler, cfg)
```

```python
plt.plot(lrs)
```

<center><img src="https://cdn.jsdelivr.net/gh/AllenWrong/BlogCDN/img/output_37_1.png"/></center>

## ReduceLROnPlateau

����Scheduler���Ը���ָ�꣬��ĳ��ָ�겻������������ʱ��ͽ���ѧϰ��˥����

- mode: min����max������acc֮���ָ����max������loss֮���ָ����min
- factor: ˥��������
- patience: ��patience��epoch�ڸ��ٵ�ָ�겻��������˥��
- threshold: �Ը��ٵ�ָ���趨��������ֵ
- min_lr: ��С��ѧϰ��

```python
auc = [
    0.54, 0.6256, 0.7087, 0.8219, 0.8549, 
    0.8873, 0.9109, 0.918, 0.8899, 0.9478, 
    0.9325, 0.9518, 0.9597, 0.9571, 0.9679, 
    0.9471, 0.9666, 0.9725, 0.964, 0.9725, 
    0.9704, 0.9761, 0.9772, 0.9801, 0.9743,
    0.9758, 0.9746, 0.9745, 0.9798, 0.9823, 
    0.9826, 0.9805,0.9752, 0.9826, 0.9818, 
    0.9842
]
```

```python
model = nn.Linear(10, 1)
optimizer = optim.Adam(model.parameters(), 1e-3)
scheduler = ReduceLROnPlateau(optimizer, mode="max", factor=0.5, patience=3, threshold=0.001, min_lr=1e-5)

lrs = []
lrs.append(optimizer.state_dict()['param_groups'][0]["lr"])
for i in range(len(auc)):
    # train
    # valiadation
    optimizer.step()
    scheduler.step(auc[i])
    lrs.append(optimizer.state_dict()['param_groups'][0]["lr"])
```

```python
plt.plot(auc)
```

<center><img src="https://cdn.jsdelivr.net/gh/AllenWrong/BlogCDN/img/output_42_1.png"/></center>

```python
plt.plot(lrs)
```

<center><img src="https://cdn.jsdelivr.net/gh/AllenWrong/BlogCDN/img/output_43_1.png"/></center>

## CosineAnnealingWarmRestarts

���������������˻��ڿ�ʼ�׶Σ�ѧϰ�ʾͽ����˻�Ȼ�󵽴�T_0��ʱ�򣬽��е�0�����������Ժ�ÿ�� $T_{t+1}= T_t*T_{mult}$�����һ����������$T_t$��ʾ��t�μ��$T_t$ ��epoch�ٽ�����������������������С�T������Ϊ[10, 20, 40, 80]���Ӷ���������epoch������Ϊ[10, 10+20, 30+40, 70+80]

- T_0: ��һ����������epoch
- T_mult: T�����ı���
- eta_min: ��С��ѧϰ�ʣ�Ĭ����0

```python
cfg.epoch = 100
optimizer = optim.Adam(model.parameters(), 1e-3)
scheduler = CosineAnnealingWarmRestarts(optimizer, T_0=10, T_mult=2, eta_min=1e-5)
lrs = train(model, optimizer, scheduler, cfg)
```

```python
plt.plot(lrs)
```

<center><img src="https://cdn.jsdelivr.net/gh/AllenWrong/BlogCDN/img/output_47_1.png"/></center>

```python

```
