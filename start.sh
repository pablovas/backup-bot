# python zipper.py && node send.js && node erase.js
#!/bin/bash

# Executa o arquivo Python
python zipper.py

# Verifica se o arquivo Python foi executado com sucesso
if [ $? -eq 0 ]; then
    # Executa o arquivo JavaScript para envio
    node send.js
    
    # Verifica se o arquivo JavaScript de envio foi executado com sucesso
    if [ $? -eq 0 ]; then
        # Executa o arquivo JavaScript de exclusão
        node erase.js
    else
        echo "Falha ao executar o arquivo send.js"
    fi
else
    echo "Falha ao executar o arquivo zipper.py"
fi