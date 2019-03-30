# pyEMTbot-docker
[![Build Status](https://travis-ci.org/andoniaf/pyemtvlc-bot.svg?branch=master)](https://travis-ci.org/andoniaf/pyemtvlc-bot)

Imagen de docker que contiene un bot de telegram para consultar la EMT (Valencia).

<img src="https://andoniaf.github.io/assets/images/2018/06/pyemtbot_tg_example.jpg" width="340" >

## Modo de uso (Pdte de actualizar con los nuevos cambios) 
- Arrancar el contenedor con:
  ```
  docker run -d -e TG_TOKEN=$YOUR_BOT_TOKEN andoniaf/pyemt-bot:latest
  ```
