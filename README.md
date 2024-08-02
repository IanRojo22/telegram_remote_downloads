# Telegram Bot para Descargas

Este bot de Telegram, escrito en Python, permite descargar archivos directamente en la máquina donde se ejecuta. Está diseñado principalmente para usarse en un servidor doméstico, pero también se puede usar en tu máquina principal.

## Funcionalidades

El bot puede manejar:
- Links de torrents/magnets
- Links de Mega
- Links de YouTube
- Links de MediaFire

## Requisitos

- **qBittorrent**
- **JDownloader**

## Instrucciones de Instalación

### Crear un Bot en Telegram

1. Abre Telegram y busca el bot llamado `BotFather`.
2. Inicia una conversación con `BotFather` y usa el comando `/start`.
3. Usa el comando `/newbot` para crear un nuevo bot.
4. Sigue las instrucciones para nombrar tu bot y obtener el token de API.

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

Regístrate en [MyJDownloader](https://my.jdownloader.org/login.html#logout) y verifica tu cuenta. Inicia sesión en la web de JDownloader local y asigna un nombre a la máquina.

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

4. Inicializa el script:

    ```bash
    python3 bot.py
    ```

## Uso

- Inicia el bot en Telegram enviando el comando `/start`.
- Envía un magnet link, un enlace torrent, o un enlace de YouTube, MediaFire, o Mega para agregarlo a qBittorrent o JDownloader.
