






import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re
import time

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    return text.strip()

def get_page_content(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # حذف عناصر غیر ضروری
        for element in soup(["script", "style", "nav", "footer", "header", "aside", "form"]):
            element.decompose()
            
        text = soup.get_text()
        return clean_text(text)
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
        return None

def process_and_save(keyword, url, file_handle):
    content = get_page_content(url)
    if content:
        try:
            file_handle.write(content)
            file_handle.flush()  # ذخیره فوری در فایل
            print(f"Successfully saved content from {url}")
        except Exception as e:
            print(f"Error writing to file: {str(e)}")

def google_search(keywords, num_results=8):
    with open('data.txt', 'w', encoding='utf-8') as f:  # پاکسازی فایل قدیمی
        f.write("")

    with open('data.txt', 'a', encoding='utf-8') as f:  # حالت append
        for keyword in keywords:
            
            print(f"\nSearching for: {keyword}")
            try:
                search_results = search(
                    keyword,
                    num=num_results
                )
                
                for i, url in enumerate(search_results, 1):
                    print(f"Processing result {i}/{num_results}")
                    process_and_save(keyword, url, f)
                    time.sleep(1.5)  # تاخیر برای جلوگیری از بلاک شدن
                    if i>=6:
                        break
                    
            except Exception as e:
                print(f"Search failed for {keyword}: {str(e)}")
                error_msg = f"\n[ERROR] Failed to process {keyword}: {str(e)}\n"
                f.write(error_msg)
                f.flush()
                continue

if __name__ == "__main__":
    keywords = [
        "Artificial Intelligence",
        "Data Analysis",
        "Cybersecurity",
        "Cloud Computing",
        "Python programming",
        "Machine learning basics",
        "Web development trends",
        "Data science techniques",
        "سنت ایرانی",
        "How to speak with a human?",
        'Humans',
        "What is LLMs?",
        "Phyzic",
        "nasa"
    ]
    
    google_search(keywords)
    
    print("\nProcess completed. Check data.txt for results.")
