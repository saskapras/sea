# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: SupportQueue
import os
import sys

ANSI_COLORS = {
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
}

def colorize(text, color, use_color=True):
    if not use_color:
        return text
    return ANSI_COLORS[color] + text + ANSI_COLORS['reset']

def print_colored(text, color, use_color=True):
    if not use_color:
        print(text)
        return
    print(f"{ANSI_COLORS[color]}{text}{ANSI_COLORS['reset']}")

def setup_color_env():
    if os.name == 'nt':
        try:
            from colorama import init
            init()
        except ImportError:
            pass
    if not os.environ.get('SUPPORT_QUEUE_COLOR'):
        return True
    return False

def get_color_support():
    try:
        import curses
        curses.setupterm()
        return curses.tigetflag('colors') == curses.TERM_FLAG_CCOLOR
    except Exception:
        return True

def disable_color():
    os.environ['SUPPORT_QUEUE_COLOR'] = '0'
    return False

def enable_color():
    os.environ.pop('SUPPORT_QUEUE_COLOR', None)
    return True
