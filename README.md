# pyEMTbot-docker
Imagen de docker que contiene un bot de telegram para consultar la EMT (Valencia).

<img src="https://andoniaf.github.io/assets/images/2018/06/pyemtbot_tg_example.jpg" width="340" >

## Modo de uso
- Crear un fichero llamado `settings.py`:
  ```
  TOKEN = '' # Token del bot

  USERS = "" # Chat ID permitidos
  ADMIN = ""
  ```

- Arrancar el contenedor con:
  ```
  docker run -d -v ${PWD}/settings.py:/pyemtbot/settings.py andoniaf/pyemtbot:latest
  ```
