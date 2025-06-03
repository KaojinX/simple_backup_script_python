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
