from pathlib import Path

# 1. Функция очистки 
def clean_text(text):
    lines = text.splitlines()
    clean_lines = []
    for line in lines:
        line = line.strip()  # убираем пробелы по краям
        if line != "":       # пропускаем пустые строки
            clean_lines.append(line)
    return "\n".join(clean_lines) # собираем обратно в текст

# 2. Настройка путей
corpus_dir = Path("corpus")
cleaned_dir = Path("cleaned")
cleaned_dir.mkdir(exist_ok=True)

# 3. Поиск файлов 
files = list(corpus_dir.glob("*.txt"))
print(f"Найдено файлов: {len(files)}")
for f in files:
    print(" -", f.name)

documents = []
total_chars = 0

print("\n--- Обработка документов ---")

# 4. Чтение и очистка
for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    
    # Проверяем на пустоту ДО очистки
    if text.strip() == "":
        print(f"Пропущен пустой файл: {file_path.name}")
        continue

    # Очищаем текст
    text = clean_text(text)
    
    # Считаем символы
    chars = len(text)
    total_chars += chars
    
    # Предупреждение, если текст слишком короткий
    if chars < 50:
        print(f"Внимание: короткий документ {file_path.name} ({chars} символов)")
    
    # Сохраняем в список словарей 
    documents.append({
        "source": file_path.name,
        "text": text
    })
    
    # Сохраняем очищенную копию 
    output_path = cleaned_dir / file_path.name
    output_path.write_text(text, encoding="utf-8")
    
    print(f"{file_path.name}: {chars} символов")

# 5. Сводка корпуса 
print("=== СВОДКА КОРПУСА ===")
print(f"Всего документов: {len(documents)}")
print(f"Общий объем: {total_chars} символов")

# Ищем самый длинный и самый короткий
if documents:
    longest = max(documents, key=lambda d: len(d["text"]))
    shortest = min(documents, key=lambda d: len(d["text"]))
    print(f"Самый длинный: {longest['source']} ({len(longest['text'])} симв.)")
    print(f"Самый короткий: {shortest['source']} ({len(shortest['text'])} симв.)")