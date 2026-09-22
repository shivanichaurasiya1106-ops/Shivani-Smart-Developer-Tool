import random
import string

def make_project():
    print("=========================================")
    print("   SHIVANI'S SMART DEVELOPER TOOL 2026   ")
    print("=========================================")
    
    # 1. ऑटोमैटिक सुरक्षित पासवर्ड बनाना (सॉफ्टवेयर सिक्योरिटी के लिए)
    chars = string.ascii_letters + string.digits + "!@#"
    password = "".join(random.choice(chars) for i in range(10))
    
    print(f"\n[+] आपकी प्रोफाइल के लिए सुरक्षित पासवर्ड जनरेट हो गया है: {password}")
    print("\n[+] स्टेटस: प्रोजेक्ट सफलता पूर्वक रन हो चुका है! 🥳🎉")
    print("=========================================")

make_project()