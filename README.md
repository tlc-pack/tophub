# TVM-Distro
Pre-tuned autotvm configurations (parameters) for common neural networks.

## Benchmark Results
This repo hosts pre-tuned configurations for the benchmark listed in https://github.com/dmlc/tvm/wiki/Benchmark

## How to update an existing package
1. Make your update to the existing file, save it with the name of the next version  
   (i.e. Update `v0.05.log` and save it to `v0.06.log`)
2. Update `PACKAGE_VERSION` in [tophub.py](https://github.com/dmlc/tvm/blob/master/python/tvm/autotvm/tophub.py) in the TVM repo to use the new file.

## How to add a package for a new backend
1. Upload your log file as `xxx_v0.01.log`
2. Add the name to `PACKAGE_VERSION` in [tophub.py](https://github.com/dmlc/tvm/blob/master/python/tvm/autotvm/tophub.py) in the TVM repo to use the new file.
