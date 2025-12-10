# Autoсlicker keyborad (Linux & Windows)

[English](#english) | [Русский](#russian)

<a name="english"></a>
## English

A simple, cross-platform GUI application to automatically simulate key presses at a set interval. Built with Python and Tkinter.

### Features

*   **Cross-Platform**: Works on Linux and Windows.
*   **GUI Interface**: User-friendly interface (Tkinter) to configure settings.
*   **Customizable**:
    *   Select the key to spam ("Base key").
    *   Select the toggle key to start/stop ("Start/Stop key").
    *   Adjust the interval between key presses (in milliseconds).
*   **Multilingual Support**: Interface language can be changed (supported languages defined in `translations.csv`).

### Requirements

*   **Python 3.x**
*   **Linux**: Requires `xdotool` for key simulation.
*   **Windows**: Requires `pyautogui`.

### Installation

#### 1. Clone the repository
```bash
git clone https://github.com/hack0770/autoclilcker-linux-and-windows.git
cd autoclilcker-linux-and-windows
```

#### 2. Install System Dependencies

**Linux (Debian/Ubuntu/Arch/etc):**
You need to install `xdotool` and `tkinter` (if not already installed).

*   Debian/Ubuntu:
    ```bash
    sudo apt install xdotool python3-tk
    ```
*   Arch Linux:
    ```bash
    sudo pacman -S xdotool tk
    ```

**Windows:**
No extra system dependencies are usually needed besides Python.

#### 3. Install Python Dependencies
It is recommended to use a virtual environment.

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### Usage

#### Running the Application

You can run the application using Python directly:

```bash
python main.py
```

Alternatively, use the provided scripts:

*   **Linux**: `./KeySpammer_Linux.sh` (Make sure it is executable: `chmod +x KeySpammer_Linux.sh`)
*   **Windows**: Double-click `KeySpammer_Windows.bat`

#### How to Use

1.  **Language**: Select your preferred language from the top-right dropdown.
2.  **Base Key**: Choose the key you want to simulate pressing repeatedly.
3.  **Start/Stop Key**: Choose the hotkey validation to toggle the spamming on and off.
4.  **Interval**: Enter the delay between key presses in milliseconds (e.g., `100` for 0.1 seconds).
5.  **Start**: Press the **Start/Stop Key** you selected to begin spamming. Press it again to stop.

### Configuration

*   **keys.txt**: Add or remove available keys for the dropdown menus in this file. Each key should be on a new line.
*   **translations.csv**: Edit this CSV file to add new languages or modify existing translations.

---

<a name="russian"></a>
## Русский

Простое кроссплатформенное GUI-приложение для автоматической симуляции нажатий клавиш с заданным интервалом. Написано на Python с использованием Tkinter.

### Возможности

*   **Кроссплатформенность**: Работает на Linux и Windows.
*   **Графический интерфейс (GUI)**: Удобный интерфейс (Tkinter) для настройки параметров.
*   **Настраиваемость**:
    *   Выбор клавиши для спама («Base key»).
    *   Выбор клавиши переключения старт/стоп («Start/Stop key»).
    *   Настройка интервала между нажатиями (в миллисекундах).
*   **Мультиязычность**: Язык интерфейса можно изменить (поддерживаемые языки определены в `translations.csv`).

### Требования

*   **Python 3.x**
*   **Linux**: Требуется `xdotool` для симуляции клавиш.
*   **Windows**: Требуется `pyautogui`.

### Установка

#### 1. Клонирование репозитория
```bash
git clone https://github.com/hack0770/autoclilcker-linux-and-windows.git
cd autoclilcker-linux-and-windows
```

#### 2. Установка системных зависимостей

**Linux (Debian/Ubuntu/Arch/etc):**
Необходимо установить `xdotool` и `tkinter` (если они еще не установлены).

*   Debian/Ubuntu:
    ```bash
    sudo apt install xdotool python3-tk
    ```
*   Arch Linux:
    ```bash
    sudo pacman -S xdotool tk
    ```

**Windows:**
Обычно никаких дополнительных системных зависимостей, кроме Python, не требуется.

#### 3. Установка Python зависимостей
Рекомендуется использовать виртуальное окружение.

```bash
# Создание виртуального окружения
python -m venv venv

# Активация виртуального окружения
# Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Установка зависимостей
pip install -r requirements.txt
```

### Использование

#### Запуск приложения

Вы можете запустить приложение напрямую через Python:

```bash
python main.py
```

Или использовать готовые скрипты:

*   **Linux**: `./KeySpammer_Linux.sh` (Убедитесь, что файл исполняемый: `chmod +x KeySpammer_Linux.sh`)
*   **Windows**: Двойной клик по `KeySpammer_Windows.bat`

#### Как пользоваться

1.  **Language (Язык)**: Выберите предпочитаемый язык в выпадающем списке справа сверху.
2.  **Base Key (Клавиша спама)**: Выберите клавишу, которую нужно нажимать автоматически.
3.  **Start/Stop Key (Клавиша старт/стоп)**: Выберите горячую клавишу для включения и выключения спама.
4.  **Interval (Интервал)**: Введите задержку между нажатиями в миллисекундах (например, `100` для 0.1 секунды).
5.  **Start (Старт)**: Нажмите выбранную **Start/Stop Key**, чтобы начать спам. Нажмите её снова, чтобы остановить.

### Конфигурация

*   **keys.txt**: В этом файле можно добавлять или удалять доступные клавиши для выпадающих списков. Каждая клавиша должна быть на новой строке.
*   **translations.csv**: Редактируйте этот CSV-файл для добавления новых языков или изменения существующих переводов.

## Author / Автор

hack0770
