# Telegram Bot para Descargas

Este bot de Telegram, escrito en Python, permite descargar archivos directamente en la máquina donde se ejecuta. Está diseñado principalmente para usarse en un servidor doméstico, pero también se puede usar en tu máquina principal.

## Funcionalidades

El bot puede descargar:
- Links de torrents/magnets
- Links de Mega
- Links de YouTube
- Links de MediaFire

## Requisitos

- **Python**
- **pip**
- **qBittorrent**
- **JDownloader**

## Instalación de Python y pip

### Windows

1. Descarga e instala Python 3.12 desde la [página oficial de Python](https://www.python.org/downloads/).
2. Durante la instalación, marca la opción "Add Python to PATH".
3. Verifica la instalación abriendo el símbolo del sistema (cmd) y ejecutando:

    ```bash
    python --version
    ```

    ```bash
    pip --version
    ```

### macOS

1. Instala Homebrew si no lo tienes ya instalado:

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. Instala Python:

    ```bash
    brew install python
    ```

3. Verifica la instalación abriendo la terminal y ejecutando:

    ```bash
    python3 --version
    ```

    ```bash
    pip3 --version
    ```

### Linux

1. Instala Python y pip usando tu gestor de paquetes. Por ejemplo, en Debian/Ubuntu:

    ```bash
    sudo apt update
    sudo apt install python3.12 python3-pip
    ```

2. Verifica la instalación abriendo la terminal y ejecutando:

    ```bash
    python3 --version
    ```

    ```bash
    pip3 --version
    ```

## Instrucciones de Instalación del Bot

### Crear un Bot en Telegram

1. Abre Telegram y busca el bot llamado `BotFather`.
2. Inicia una conversación con `BotFather` y usa el comando `/start`.
3. Usa el comando `/newbot` para crear un nuevo bot.
4. Sigue las instrucciones para nombrar tu bot y obtener la API.

### Instalar qBittorrent

#### Opción 1: Docker

Recomiendo instalar qBittorrent en Docker. Sigue los pasos en la [página oficial de Docker](https://hub.docker.com/r/linuxserver/qbittorrent).

#### Opción 2: OpenMediaVault o CasaOS

- En OpenMediaVault, puedes usar la imagen de ejemplo proporcionada en los archivos del compose.
- En CasaOS, instala la app desde la AppStore.

Accede al cliente qBittorrent a través del navegador. Las credenciales predeterminadas son `admin` para el usuario y `adminadmin` para la contraseña. Si no puedes iniciar sesión, revisa el log del contenedor para encontrar una contraseña temporal. Una vez dentro, cambia la contraseña en los ajustes.

### Instalar JDownloader

#### Opción 1: Docker

Para JDownloader, puedes instalar la app de escritorio o, preferiblemente, seguir la instalación en Docker: [Docker JDownloader](https://github.com/jlesage/docker-jdownloader-2).

#### Opción 2: OpenMediaVault o CasaOS

- En CasaOS, instala la app desde la AppStore.
- En OpenMediaVault, usa los ejemplos proporcionados.

Regístrate en [MyJDownloader](https://my.jdownloader.org/login.html#logout) y verifica tu cuenta. Inicia sesión en la web de JDownloader local y asigna un nombre al dispositivo.

### Configurar y Ejecutar el Bot

1. Clona el repositorio:

    ```bash
    git clone https://github.com/IanRojo22/telegram_remote_download.git
    cd telegram_remote_download
    ```

2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

3. Crea un archivo `.env` en el directorio del proyecto con las siguientes variables:

    ```env
    TELEGRAM_TOKEN=TuApiTelegram
    QB_SERVER=http://IpDondeCorreQbittorrent:PuertoDondeCorreQbittorrent
    QB_USERNAME=UsuarioQbittorrent
    QB_PASSWORD=ContraseñaQbitTorrent
    JD_USERNAME=UsuarioJdownloader
    JD_PASSWORD=ContraseñaJdownloader
    JD_DEVICE_NAME=NombreDispositivoJdownloader
    ```

    Asegúrate de reemplazar los valores de las variables con tus credenciales y configuraciones reales.

4. Inicia el script:

    ```bash
    python3 bot.py
    ```

## Solución de Problemas

- **Problemas de autenticación en qBittorrent**: Verifica que las credenciales en el archivo `.env` sean correctas y que qBittorrent esté accesible desde la dirección IP y el puerto especificados.
- **Problemas de autenticación en JDownloader**: Asegúrate de que las credenciales de MyJDownloader sean correctas y que el nombre del dispositivo coincida con el configurado en la web local de JDownloader.
- **Errores de instalación de dependencias**: Asegúrate de tener pip y Python correctamente instalados. Si encuentras errores específicos, busca soluciones en la documentación oficial de las librerías.
- **Error `ModuleNotFoundError` para 'telegram'**: Asegúrate de que el módulo `python-telegram-bot` esté instalado y que no haya problemas con tu entorno virtual o variables de entorno.

