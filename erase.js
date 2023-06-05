const fs = require('fs');
const path = require('path');
const config = require('./config');

const zipFilesDir = config.homeDir;

fs.readdir(zipFilesDir, (err, files) => {
    if (err) {
      console.error('Erro ao ler o diretório:', err);
      return;
    }
    
    files.forEach(file => {
      const arquivo = path.join(zipFilesDir, file);
      const extensao = path.extname(arquivo);
  
        if (extensao === '.zip') {
            fs.unlink(arquivo, err => {
                if (err) {
                    console.error('Erro ao apagar o arquivo:', err);
                    return;
                }
                console.log(`Arquivo ${arquivo} apagado com sucesso.`);
            });
        }
    });
});