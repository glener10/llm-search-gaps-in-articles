#!/bin/bash

python gemini.py -i "example.pdf" -m gemini-2.0-flash &
python gemini.py -i "example.pdf" -m gemini-2.0-flash-lite &
python gemini.py -i "example.pdf" -m gemini-1.5-flash &
python gemini.py -i "example.pdf" -m gemini-2.5-flash-preview-05-20 &
wait