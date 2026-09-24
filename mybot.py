import random
import string

def make_project():
    print("=========================================")
    print("   SHIVANI'S SMART DEVELOPER TOOL 2026   ")
    print("=========================================")
    
    # 1. ऑटोमैटिक सुरक्षित पासवर्ड बनाना (सॉफ्टवेयर सिक्योरिटी के लिए)
    chars = string.ascii_letters + string.digits + "!@#"
    password = "".join(random.choice(chars) for i in range(10))
    
    print(f"\n[+] {password}")
    print("\n[+] status)
    print("=========================================")

make_project()
