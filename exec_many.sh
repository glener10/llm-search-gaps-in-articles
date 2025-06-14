#!/bin/bash

python gemini.py -i "example.pdf" -m gemini-2.0-flash -o example_output.txt &
python gemini.py -i "example.pdf" -m gemini-2.0-flash-lite -o example_output.txt &
python gemini.py -i "example.pdf" -m gemini-1.5-flash -o example_output.txt &
python gemini.py -i "example.pdf" -m gemini-2.5-flash-preview-05-20 -o example_output.txt &
wait