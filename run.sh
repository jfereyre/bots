#!/bin/bash

PYTHONPATH=$PYTHONPATH:`readlink -f pyPath` python3 ./test.py