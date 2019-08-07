# TVM-Distro
Pre-tuned autotvm configurations (parameters) for common neural networks.

## Benchmark Results
This repo hosts pre-tuned configurations for the benchmark listed in https://github.com/dmlc/tvm/wiki/Benchmark

## Update Procedure
The steps to update a log file for a backend are:
1. Make your update to the existing file, save it with the name of next version  
   (i.e. Update `v0.05.log` and save it to `v0.06.log`)
2. Update the `PACKAGE_VERSION` in [tophub.py](https://github.com/dmlc/tvm/blob/master/python/tvm/autotvm/tophub.py) in the TVM repo to use the new file.
