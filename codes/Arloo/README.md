# Arloo Annotation Tool

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


