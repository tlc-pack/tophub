# TVM-Distro
Pre-tuned op parameters for autotvm

## Benchmark
This repo hosts the pretuned parameters for the benchmark listed in https://github.com/dmlc/tvm/wiki/Benchmark

## Update Procedure
1. Make your update to the existing file, save it with name of next version  
   (i.e. Update `v0.05.log` and save it to `v0.06.log`)
2. Update the `PACKAGE_VERSION` in [tophub.py](https://github.com/dmlc/tvm/blob/master/python/tvm/autotvm/tophub.py) in the TVM repo.

