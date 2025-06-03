# simple_backup_script_python
# 🔄 Backup Script

## 🇵🇱 Opis

Ten skrypt tworzy automatyczne kopie zapasowe plików z wybranego folderu, zapisując je jako pliki ZIP z datą i godziną. Przydatny do prostych lokalnych backupów.

### ✅ Funkcje
- Tworzy archiwum ZIP z plikami z danego folderu
- Nazwa archiwum zawiera znacznik czasu
- Harmonogram uruchamiania co 30 sekund (można zmienić)
- Obsługa błędów (brak plików, brak dostępu)

### 🛠️ Wymagania
- Python 3.8+
- schedule

### 🚀 Uruchomienie
1. Uzupełnij ścieżki `file` i `fileTo` w `main.py`
2. Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

# 🔄 Backup Script

## 🇬🇧 English

This Python script automatically creates ZIP backups of files from a selected folder. Each backup includes a timestamp in the filename.

### ✅ Features
- Creates ZIP archive from all files in a folder
- Archive name includes date and time
- Automatically runs every 30 seconds (configurable)
- Error handling for missing files and access issues

### 🛠️ Requirements
- Python 3.8+
- `schedule` module

### 📦 Installation
1. Edit paths in `main.py`:
   - `file` → source folder to back up
   - `fileTo` → destination folder for ZIPs
2. Install required modules:
```bash
pip install -r requirements.txt
```
