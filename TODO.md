- []: Improve docker image
  - [X]: non-root user
- []: Manage emt error, p.e: when there is no "parada", only /emt
- []: Setup autodeploy Heroku (TravisCI)
- []: Divide CI in steps: lint, test, deploy
- []: Add test
- [X]: Fix this:
      ```
      C3PO.pybot, [31.03.19 10:18]
      /bin/sh: syntax error: unterminated quoted string

      Andoni, [31.03.19 10:18]
      /emt '
      ```

      ```
      Andoni, [31.03.19 10:22]
      /emt $((100+700))

      C3PO.pybot, [31.03.19 10:22]
      Parada: 800
      4 Pl. Ajuntament - LÍNEA DESVIADA
      8 Hosp. La Fe - LÍNEA DESVIADA
      9 La Torre - LÍNEA DESVIADA
      11 Patraix - LÍNEA DESVIADA
      16 Pl. Ajuntament - LÍNEA DESVIADA
      28 Mercat Central - LÍNEA DESVIADA
      70 La Fontsanta - LÍNEA DESVIADA
      71 la Llum - LÍNEA DESVIADA

      Andoni, [31.03.19 10:23]
      /emt 800 && id

      C3PO.pybot, [31.03.19 10:23]
      Parada: 800
      4 Pl. Ajuntament - LÍNEA DESVIADA
      8 Hosp. La Fe - LÍNEA DESVIADA
      9 La Torre - LÍNEA DESVIADA
      11 Patraix - LÍNEA DESVIADA
      16 Pl. Ajuntament - LÍNEA DESVIADA
      28 Mercat Central - LÍNEA DESVIADA
      70 La Fontsanta - LÍNEA DESVIADA
      71 la Llum - LÍNEA DESVIADA

      uid=1000(pyuser) gid=1000(pyuser)
      ```

- [X]: Fix this (prob pyemtvlc pkg problem):
      Andoni, [31.03.19 10:23]
      /emt 800 && uname

      Andoni, [31.03.19 10:24]
      /emt 8

      C3PO.pybot, [31.03.19 10:24]
      Parada: 8
      Traceback (most recent call last):
        File "/usr/local/bin/pyemtvlc", line 25, in <module>
          main()
        File "/usr/local/bin/pyemtvlc", line 20, in main
          msg = next_buses(numParada, numLinea)
        File "/usr/local/lib/python3.7/site-packages/utils/parser.py", line 54, in next_buses
          return generate_msg(info)
        File "/usr/local/lib/python3.7/site-packages/utils/parser.py", line 42, in generate_msg
          if info[0][0] is None:
      IndexError: list index out of range
