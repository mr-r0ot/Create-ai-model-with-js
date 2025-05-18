# crete-ai-model-with-js
Create Ai Model(SLM) in js and use it (Only js syntax and no libraries or frameworks)


## Running Steps
# 1. Data Extract
running 'DataExtractor.py' (you can replace keywords in code), data save to data.txt
# 2. Data Tokenize
running 'DataTokenizer.py' , new data save to data.json
# 3. Move data.json to html(js) code
copy data.json and create 
```
<script>
const tokens = [
put data.json here
]
</script>
```
# 4. add SLMai.js to code
write
```
<script src="SLMai.js"></script>
```
# 5. Create input box
Create a input box with id 'userInput'
# 6. Create send button
with onclick 'generate()'
# 7. Create a div or other
with id 'response'



## you can change all id in SLMai.js file or see alghorithm
## With love from Mohammad Taha Gorji
