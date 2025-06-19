#!/bin/bash

#gemini-2.0-flash
# python3 gemini.py -i "1.pdf" -m gemini-2.0-flash -o outputs/a_responsabilidade_civil_das_instituicoes.txt &
# python3 gemini.py -i "2.pdf" -m gemini-2.0-flash -o outputs/post_quantum_cryptography.txt &
# python3 gemini.py -i "3.pdf" -m gemini-2.0-flash -o outputs/a_responsabilidade_das_instituicoes_financeiras_nas_fraudes.txt &
# python3 gemini.py -i "4.pdf" -m gemini-2.0-flash -o outputs/tecnologia_de_pagamento_instantaneo_pix_criminalidades.txt &
# python3 gemini.py -i "5.pdf" -m gemini-2.0-flash -o outputs/a_consumer_centric_approach.txt &
# python3 gemini.py -i "6.pdf" -m gemini-2.0-flash -o outputs/cemlas.txt &
# python3 gemini.py -i "7.pdf" -m gemini-2.0-flash -o outputs/central_bank.txt &

#gemini-2.0-flash-preview
python3 gemini.py -i "1.pdf" -m gemini-2.5-flash-preview-05-20 -o outputs/a_responsabilidade_civil_das_instituicoes.txt &
python3 gemini.py -i "2.pdf" -m gemini-2.5-flash-preview-05-20 -o outputs/post_quantum_cryptography.txt &
python3 gemini.py -i "3.pdf" -m gemini-2.5-flash-preview-05-20 -o outputs/a_responsabilidade_das_instituicoes_financeiras_nas_fraudes.txt &
python3 gemini.py -i "4.pdf" -m gemini-2.5-flash-preview-05-20 -o outputs/tecnologia_de_pagamento_instantaneo_pix_criminalidades.txt &
python3 gemini.py -i "5.pdf" -m gemini-2.5-flash-preview-05-20 -o outputs/a_consumer_centric_approach.txt &
python3 gemini.py -i "6.pdf" -m gemini-2.5-flash-preview-05-20 -o outputs/cemlas.txt &
python3 gemini.py -i "7.pdf" -m gemini-2.5-flash-preview-05-20 -o outputs/central_bank.txt &
wait