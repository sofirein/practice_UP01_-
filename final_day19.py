import os
import glob
import random
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Загрузка модели... Подождите.")
# TF-IDF creates semantic vectors based on text structure without needing PyTorch
vectorizer = TfidfVectorizer()

# 2. Ищем файлы с чанками
chunks = []
files = glob.glob("chunks/*.txt")

# Проверка на наличие файлов, чтобы избежать ошибок пустого списка
if not files:
    print("Ошибка: папка 'chunks' пуста или не найдена!")
    exit()

# Берем случайные 10-15 файлов, чтобы не грузить память (по требованию нужно минимум 10)
random.shuffle(files)
for file_path in files[:12]:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()
        
        # Отделяем имя файла от номера чанка
        name = os.path.basename(file_path) # budget_basics_chunk_0.txt
        
        if "_chunk_" in name:
            parts = name.split("_chunk_")     # ['budget_basics', '0.txt']
            source = parts[0] + ".txt"
            chunk_id = parts[1].replace(".txt", "")
        else:
            source = name
            chunk_id = "0"
        
        # Сохраняем данные в словарь
        chunks.append({
            "source": source,
            "chunk_id": chunk_id,
            "text": text
        })

print(f"Загружено чанков: {len(chunks)}\n")

# 3. Собираем тексты и обучаем векторную модель
texts = [chunk["text"] for chunk in chunks]
chunk_vectors = vectorizer.fit_transform(texts)

# 4. Задаем вопросы пользователя (по методичке нужно минимум 3)
questions = [
    "Как накопить деньги на отпуск?",
    "Что такое правило 50 на 30 на 20?",
    "Как перестать тратить деньги на всякую ерунду?"
]

# 5. Ищем ответы
for q in questions:
    print("-" * 50)
    print("Вопрос:", q)
    
    # Получаем вектор вопроса
    q_vector = vectorizer.transform([q])
    
    # Считаем сходство между вопросом и всеми чанками
    scores = cosine_similarity(q_vector, chunk_vectors)[0].tolist()
    
    # Ищем максимум
    best_score = max(scores)
    best_index = scores.index(best_score)
    best_chunk = chunks[best_index]
    
    # Выводим результат
    print("Источник:", best_chunk["source"])
    print("Номер чанка:", best_chunk["chunk_id"])
    print("Текст:", best_chunk["text"])
    print("Сходство:", round(best_score, 4))
    print()
