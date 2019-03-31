# pyEMTbot-docker
[![Build Status](https://travis-ci.org/andoniaf/pyemtvlc-bot.svg?branch=master)](https://travis-ci.org/andoniaf/pyemtvlc-bot)

Imagen de docker que contiene un bot de telegram para consultar la EMT (Valencia).

[Pruébame aquí!](https://telegram.me/emtvlcbot)

<img src="https://raw.githubusercontent.com/andoniaf/pyemtvlc-bot/master/imgs/demo_bot02.jpg" width="340" >

## Uso de la imagen Docker
- Arrancar el contenedor con nuestro token:
  ```
  docker run -d -e TG_TOKEN=$YOUR_BOT_TOKEN andoniaf/pyemtvlc-bot:latest
  ```
