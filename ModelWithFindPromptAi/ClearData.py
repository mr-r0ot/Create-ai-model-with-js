import pandas as pd
import sys
import json
import csv
from langdetect import detect, DetectorFactory

# Ensure consistent language detection
DetectorFactory.seed = 0

def load_csv(path):
    return pd.read_csv(
        path,
        encoding='utf-8-sig',
        delimiter=',',
        quoting=csv.QUOTE_ALL, 
        dtype=str              
    )

def clean_text(text):
    if pd.isna(text):
        return ""

    return text.strip()

def detect_language(text):
    try:
        return detect(text)
    except:
        return 'unknown'

def transform_to_jsonl(df, out_path):
    with open(out_path, 'w', encoding='utf-8') as f:
        for _, row in df.iterrows():
            question = clean_text(row.get('question', ''))
            answer = clean_text(row.get('answer', ''))
            if not question or not answer:
                continue
            record = {
                'prompt': question,
                'completion': answer,
                'lang_question': detect_language(question),
                'lang_answer': detect_language(answer)
            }
            f.write(json.dumps(record, ensure_ascii=False) + '\n')

if __name__ == '__main__':
    try:
        input_csv = sys.argv[1]
    except:
        input_csv = 'data.csv'               # مسیر فایل ورودی
    try:
        output_jsonl = sys.argv[2]
    except:
        output_jsonl = 'processed_data.jsonl'  # مسیر فایل خروجی

    df = load_csv(input_csv)
    transform_to_jsonl(df, output_jsonl)
    print(f"✅ Datas Saved In: {output_jsonl}")
