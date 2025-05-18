

    const model = {};
    function buildModel() {
      for (let i = 0; i < tokens.length - 2; i++) {
        const key = `${tokens[i]} ${tokens[i+1]}`;
        if (!model[key]) model[key] = [];
        model[key].push(tokens[i+2]);
      }
    }
    buildModel();

    function randomKey() {
      const keys = Object.keys(model);
      return keys[Math.floor(Math.random() * keys.length)];
    }

    function backoffKey(result) {
      const last = result[result.length - 1];
      const candidates = Object.keys(model).filter(k => k.endsWith(` ${last}`));
      if (candidates.length) return candidates[Math.floor(Math.random() * candidates.length)];
      return randomKey();
    }

    function ruleBasedResponse(input) {
      const txt = input.trim().toLowerCase();
      const greetings = ["سلام", "hi", "hello"];
      if (greetings.some(g => txt === g)) {
        return "سلام! چطور می‌توانم کمکتان کنم؟";
      }
      return null;
    }

    function generateResponse(input, maxLen = 30) {
      // بررسی قوانین اولیه
      const ruleResp = ruleBasedResponse(input);
      if (ruleResp) return ruleResp;

      // مدل مارکوف برای تولید متن
      const words = input.toLowerCase().replace(/[^\u0600-\u06FF\w\s]/g, ' ').split(/\s+/).filter(Boolean);
      let key;
      if (words.length >= 2) {
        key = `${words[words.length-2]} ${words[words.length-1]}`;
        if (!model[key]) key = randomKey();
      } else {
        key = randomKey();
      }

      const result = key.split(' ');
      for (let i = 0; i < maxLen; i++) {
        let choices = model[key];
        if (!choices || !choices.length) {
          key = backoffKey(result);
          choices = model[key] || [];
          if (!choices.length) break;
        }
        const next = choices[Math.floor(Math.random() * choices.length)];
        result.push(next);
        key = `${result[result.length-2]} ${result[result.length-1]}`;
      }
      return result.join(' ');
    }

    function generate() {
      const input = document.getElementById('userInput').value;
      if (!input.trim()) return;
      const resp = generateResponse(input);
      document.getElementById('response').textContent = resp;
    }