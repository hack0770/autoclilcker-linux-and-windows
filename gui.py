import tkinter as tk
from tkinter import ttk, messagebox
from pynput.keyboard import Listener, Key
from keypresser import KeyPresser
import csv

def load_translations(language='en', file='translations.csv'):
    try:
        with open(file, encoding='utf-8') as f:
            return {row['key']: row[language] for row in csv.DictReader(f)}
    except Exception:
        return {'window_title': 'KS (Missing translations file)', 'language_label': 'Language:', 'base_key_label': 'Base key:',
                'start_key_label': 'Start/Stop key:', 'interval_label': 'Interval (ms):',
                'status_label_stopped': 'Stopped', 'status_label_running': 'Running',
                'error_on_press': 'Error'}

def load_keys(filename='keys.txt'):
    try:
        with open(filename, encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return list('abcde')

def get_languages(file='translations.csv'):
    try:
        with open(file, encoding='utf-8') as f:
            return [col for col in next(csv.reader(f)) if col != 'key']       
    except Exception:
        return 'missing'
class KeySpamApp:
    def __init__(self, root, language='en'):
        self.root = root
        self.language = language
        self.translations = load_translations(language)
        self.presser = KeyPresser()
        self.root.resizable(False, False)
        # AnimatioS
        self._animation_job = None
        self._pulse_state = False

        self.setup_ui()
        Listener(on_press=self.on_press).start()

    def setup_ui(self):
        self.root.title(self.translations['window_title'])

        # Color 
        self.colors = {
            'blue': '#0b63d6',      
            'cyan': '#38b6ff',
            'white': '#ffffff',     
            'white_light': '#eaf6ff',
            'text_dark': '#023e8a'
        }

        self.root.configure(bg=self.colors['white_light'])

        style = ttk.Style()
        style.theme_use('clam')
        # apply 
        style.configure('TLabel', font=("Segoe UI", 10), background=self.colors['white_light'], foreground=self.colors['text_dark'])
        style.configure('TButton', font=("Segoe UI", 10), background=self.colors['blue'], foreground=self.colors['white'])
        style.configure('TCombobox', font=("Segoe UI", 10), fieldbackground=self.colors['white'], background=self.colors['white'])
        style.configure('TEntry', font=("Segoe UI", 10), fieldbackground=self.colors['white'])

        # tenu 

        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # top-left 
        lang_frame = tk.Frame(main_frame, bg="#f0f0f0")
        lang_frame.grid(row=1, column=1, sticky="ne", padx=20, pady=(65, 0))

        lang_label = ttk.Label(lang_frame, text=self.translations['language_label'])
        lang_label.pack(side="left", padx=(0, 4))

        langs = get_languages()
        self.language_dropdown = ttk.Combobox(lang_frame, values=langs, state='readonly', width=8)
        self.language_dropdown.set(self.language)
        self.language_dropdown.pack(side="left")
        self.language_dropdown.bind("<<ComboboxSelected>>", self.change_language)
        for ev in ("<FocusIn>", "<Button-1>", "<Double-Button-1>", "<B1-Motion>"):
            self.language_dropdown.bind(ev, lambda e: self.language_dropdown.after(1, self.language_dropdown.selection_clear))
        self.language_label = lang_label

        # middle controls
        keys = load_keys()
        control_frame = tk.Frame(main_frame, bg="#f0f0f0")
        control_frame.grid(row=1, column=0, sticky="w", pady=10)

        # key side
        keys_frame = tk.Frame(control_frame, bg="#f0f0f0")
        keys_frame.pack()

        self.base_key_label = ttk.Label(keys_frame, text=self.translations['base_key_label'])
        self.base_key_label.grid(row=0, column=0, padx=5)
        self.base_key_dropdown = ttk.Combobox(keys_frame, values=keys, state='readonly', width=8)
        self.base_key_dropdown.set('f')
        self.base_key_dropdown.grid(row=1, column=0, padx=5)

        self.start_key_label = ttk.Label(keys_frame, text=self.translations['start_key_label'])
        self.start_key_label.grid(row=0, column=1, padx=5)
        self.start_key_dropdown = ttk.Combobox(keys_frame, values=keys, state='readonly', width=8)
        self.start_key_dropdown.set('alt')
        self.start_key_dropdown.grid(row=1, column=1, padx=5)

        for box in [self.base_key_dropdown, self.start_key_dropdown]:
            for ev in ("<FocusIn>", "<Button-1>", "<Double-Button-1>", "<B1-Motion>"):
                box.bind(ev, lambda e, box=box: box.after(1, box.selection_clear))

        # interval entry below key
        interval_frame = tk.Frame(control_frame, bg="#f0f0f0")
        interval_frame.pack(pady=(10, 0))

        self.interval_label = ttk.Label(interval_frame, text=self.translations['interval_label'])
        self.interval_label.pack(side="left", padx=(0, 6))
        self.interval_entry = ttk.Entry(interval_frame, justify="center", width=10)
        self.interval_entry.insert(0, "100")
        self.interval_entry.pack(side="left")

        # status 
        self.status_label = ttk.Label(main_frame, text=self.translations['status_label_stopped'],
                                      font=("Segoe UI", 11, "bold"), foreground="#444")
        self.status_label.grid(row=1, column=1, sticky="ne", padx=20, pady=30)

        # author label left
        self.author_label = ttk.Label(main_frame, text="Author: hack0770",
                                      font=("Segoe UI", 9), foreground="#666")
        self.author_label.grid(row=2, column=0, sticky="w", padx=10, pady=(5, 0))

    def on_press(self, key):
        try:
            key_pressed = key.name if isinstance(key, Key) else key.char
            if key_pressed == self.start_key_dropdown.get():
                (self.start_spamming if not self.presser.running else self.stop_spamming)()
        except Exception as e:
            print(self.translations['error_on_press'], e)
            self.update_status(self.translations['error_on_press'], 'error')

    def start_spamming(self):
        try:
            interval = int(self.interval_entry.get())
            self.presser.configure(self.base_key_dropdown.get(), interval)
            self.presser.start()
            self.update_status(self.translations['status_label_running'], 'running')
        except Exception as e:
            print("Start error:", e)
            self.update_status(self.translations['error_on_press'], 'error')

    def stop_spamming(self):
        self.presser.stop()
        self.update_status(self.translations['status_label_stopped'], 'stopped')

    def update_status(self, text, status='stopped'):
        colors = {'running': 'green', 'error': 'red', 'stopped': '#444'}
        self.status_label.config(text=text, foreground=colors.get(status, '#444'))
        # start stop pulsing 
        if status == 'running':
            self._start_animation()
        else:
            final_color = colors.get(status, '#444')
            self._stop_animation(final_color)

    def _animate_status(self):
        """Toggle status label color and reschedule animation."""
        # toggle pulse state
        self._pulse_state = not self._pulse_state
        color = '#66cc66' if self._pulse_state else 'green'
        try:
            self.status_label.config(foreground=color)
            self._animation_job = self.root.after(500, self._animate_status)
        except Exception:
            # widget destroyed 
            self._animation_job = None

    def _start_animation(self):
        if self._animation_job is None:
            self._pulse_state = False
            self._animate_status()

    def _stop_animation(self, final_color='#444'):
        if self._animation_job is not None:
            try:
                self.root.after_cancel(self._animation_job)
            except Exception:
                pass
            self._animation_job = None
        try:
            self.status_label.config(foreground=final_color)
        except Exception:
            pass

    def change_language(self, _):
        self.language = self.language_dropdown.get()
        self.translations = load_translations(self.language)

        self.root.title(self.translations['window_title'])
        self.language_label.config(text=self.translations['language_label'])
        self.base_key_label.config(text=self.translations['base_key_label'])
        self.start_key_label.config(text=self.translations['start_key_label'])
        self.interval_label.config(text=self.translations['interval_label'])
        self.update_status(self.translations['status_label_stopped'])

if __name__ == "__main__":
    root = tk.Tk()
    KeySpamApp(root)
    root.mainloop()
