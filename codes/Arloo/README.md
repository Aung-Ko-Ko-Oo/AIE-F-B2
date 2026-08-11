# 🥔 Arloo Annotation Tool

## Library Installation

```
pip install flask
pip install pyyaml
```

## --help

```
PS C:\Users\yktnl\Downloads\aat> python .\arloo.py --help
usage: arloo.py [-h] {web,gui,init} ...

🥔 Arloo Annotation Tool — Lightweight POLAR dataset annotator

positional arguments:
  {web,gui,init}  Operation mode
    web           Run web interface (Flask)
    gui           Run desktop GUI (Tkinter)
    init          Create sample config and text files

options:
  -h, --help      show this help message and exit

Examples:
  python arloo.py init
  python arloo.py web --annotator "kyawkyaw" --input sample_texts.txt
  python arloo.py web --annotator "kyawkyaw" --input data.csv --port 8080
  python arloo.py gui --annotator "kyawkyaw" --input sample_texts.txt
  python arloo.py web --annotator "kyawkyaw"  # Start empty, add sentences interactively

PS C:\Users\yktnl\Downloads\aat>
```

## Initialization

ဒီနည်းကတော့ ပထမဆုံး Arloo Annotation Tool ကို run မယ်ဆိုရင် အသုံးပြုလို့ ရပါတယ်။ ကိုယ့်ဆီမှာ configuration file လည်း မပြင်ရသေးဘူး။ Text corpus လည်း မရှိသေးဘူးဆိုတဲ့ အခြေအနေပါ။ အောက်ပါအတိုင်း run လိုက်ရင် example configuration ဖိုင်နဲ့ example text corpus ဖိုင်ကို အော်တိုဆောက်ပေးသွားပါလိမ့်မယ်။  

```
PS C:\Users\yktnl\Downloads\aat> python .\arloo.py init
✅ Created: arloo_config.yaml
✅ Created: sample_texts.txt

📋 Next steps:
   1. Edit arloo_config.yaml to customize fields (optional)
   2. Add your texts to sample_texts.txt (one per line)
   3. Run: python arloo.py web --annotator "your-name" --input sample_texts.txt
   4. Open http://localhost:5000 in your browser

PS C:\Users\yktnl\Downloads\aat>
```

## arloo_config.yaml

အော်တို ဆောက်ပေးသွားတဲ့ configuration file ဖြစ်တဲ့ `arloo_config.yaml` ဖိုင်ကတော့ အောက်ပါအတိုင်းပါ။  

```yaml
# Arloo Annotation Tool Configuration
# ====================================
# Edit this file to add, remove, or modify annotation fields.
# Field types: auto_id, text, binary
# For text fields: set multiline: true for textarea, false for single-line
# For separator: use ||| to separate multiple values within a field
# For binary fields: optionally set group to organize them in the UI

project:
  name: "POLAR Myanmar Annotation"
  language: "mya"

# ID pattern uses {language}, {annotator}, {index} placeholders
id_pattern: "{language}_{annotator}_{index}"

fields:
  # --- Metadata Fields ---
  - name: id
    type: auto_id
    readonly: true
    description: "Auto-generated unique ID"

  - name: source
    type: text
    multiline: true
    separator: "|||"
    description: "URL or source of the text. Use ||| to separate multiple sources."
    placeholder: "https://example.com/article|||Article title"

  - name: text
    type: text
    multiline: true
    description: "The main text to annotate"
    placeholder: "Enter or paste text here..."

  - name: key_phrase
    type: text
    multiline: true
    separator: "|||"
    description: "Key phrases. Use ||| to separate multiple phrases."
    placeholder: "key-phrase-1|||key-phrase-2|||key-phrase-3"

  # --- Sub-Task 1 & 2: Polarization Type ---
  - name: polarization
    type: binary
    group: "Sub-Task 1 & 2: Polarization Type"

  - name: political
    type: binary
    group: "Sub-Task 1 & 2: Polarization Type"

  - name: racial/ethnic
    type: binary
    group: "Sub-Task 1 & 2: Polarization Type"

  - name: religious
    type: binary
    group: "Sub-Task 1 & 2: Polarization Type"

  - name: gender/sexual
    type: binary
    group: "Sub-Task 1 & 2: Polarization Type"

  - name: other
    type: binary
    group: "Sub-Task 1 & 2: Polarization Type"

  # --- Sub-Task 3: Severity ---
  - name: stereotype
    type: binary
    group: "Sub-Task 3: Severity"

  - name: vilification
    type: binary
    group: "Sub-Task 3: Severity"

  - name: dehumanization
    type: binary
    group: "Sub-Task 3: Severity"

  - name: extreme_language
    type: binary
    group: "Sub-Task 3: Severity"

  - name: lack_of_empathy
    type: binary
    group: "Sub-Task 3: Severity"

  - name: invalidation
    type: binary
    group: "Sub-Task 3: Severity"

```

