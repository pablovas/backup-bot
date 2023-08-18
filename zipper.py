import os
import zipfile

def zip_folders(selected_folders, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for folder in selected_folders:
            for root, _, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, os.path.dirname(folder))
                    zipf.write(file_path, arcname)

def main():
    selected_folders = []
    while True:
        folder = input("Digite o caminho da pasta a ser zipada (ou 'sair' para encerrar): ")
        if folder.lower() == 'sair':
            break
        if os.path.exists(folder) and os.path.isdir(folder):
            selected_folders.append(folder)
        else:
            print("Caminho inválido ou pasta não encontrada. Tente novamente.")

    if selected_folders:
        zip_filename = os.path.expanduser('~/selected_folders.zip')
        zip_folders(selected_folders, zip_filename)
        print(f"Pastas zipadas com sucesso! Arquivo ZIP salvo em: {zip_filename}")
    else:
        print("Nenhuma pasta selecionada. Encerrando.")

if __name__ == "__main__":
    main()
