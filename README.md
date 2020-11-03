# Tophub
Pre-tuned autotvm configurations (parameters) for common neural networks.

## Benchmark Results
This repo hosts pre-tuned configurations

## How to update an existing package
1. Make your update to the existing file, save it with the name of the next version  
   (i.e. Update `v0.05.log` and save it to `v0.06.log`)
2. Update `PACKAGE_VERSION` in tophub.py in to use the new file.

## How to add a package for a new backend
1. Upload your log file as `xxx_v0.01.log`
2. Add the name to `PACKAGE_VERSION` in tophub.py to use the new file.
