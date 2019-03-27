import platform
import uptime
from datetime import timedelta
import time
import subprocess
import os


# Funcion para medir la memoria usada por el bot
def memory_usage_ps():
    #out = subprocess.Popen(['ps', 'v', '-p',
    out = subprocess.Popen(['ps', '-o', 'pid,user,vsz,rss,comm,args',
                            str(os.getpid())], stdout=subprocess.PIPE).communicate()[0].split(b'\n')
    vsz_index = out[0].split().index(b'RSS')
    mem = float(out[1].split()[vsz_index]) / 1024
    return "{0:.2f}".format(mem)


# Funcion para construir el mensaje que devolverá
def uptime_string():
    # Machine info
    uname = platform.uname()
    uptime_seconds = uptime.uptime()
    # Delta uptime in human readable format
    uptime_string = str(timedelta(seconds=uptime_seconds))
    # Get memory usage with ps
    #memory = memory_usage_ps()
    # Make messsge
    string = ""
    string += "\U0001F4BB Running on " + uname[0] + " " + uname[2] + " " + uname[4] + "\n"
    string += "\U0000231B Uptime: " + uptime_string + "\n"
    #string += "\U0001F4CA Bot memory usage: " + memory + "MB"
    return string


# Funcion para consultar la EMT
def query_emt(parada):
    # Mensaje = logs_size_str
    emt_info = (subprocess.getoutput("pyemtvlc " + parada))
    return emt_info
