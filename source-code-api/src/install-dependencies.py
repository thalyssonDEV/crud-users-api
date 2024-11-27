def install_dependencies() -> None:
    import subprocess

    # Comando para instalar pacotes
    command_path = "pip install flask httpie requests"

    # Executa o comando
    subprocess.run(command_path, shell=True, check=True)