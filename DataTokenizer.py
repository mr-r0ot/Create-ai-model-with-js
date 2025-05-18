import re
import json

# 1. Read the raw text file
def load_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# 2. Basic tokenization and normalization
def tokenize(text):
    # Lowercase
    text = text.lower()
    # Split on whitespace
    tokens = text.split()
    return tokens

# 3. Clean tokens (e.g., remove short tokens)
def clean(tokens, min_len=2):
    return [t for t in tokens if len(t) >= min_len]

# 4. Main processing pipeline
def process(path_in, path_out):
    raw = load_text(path_in)
    toks = tokenize(raw)
    toks = clean(toks)
    # Save to JSON
    with open(path_out, 'w', encoding='utf-8') as f:
        json.dump(toks, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(toks)} tokens to {path_out}")

if __name__ == '__main__':
    import sys
    in_file = sys.argv[1] if len(sys.argv) > 1 else 'data.txt'
    out_file = sys.argv[2] if len(sys.argv) > 2 else 'data.json'
    process(in_file, out_file)
