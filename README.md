# 💡 Deepseek R1 Chatbot

This project is a **chatbot powered by the Deepseek R1 model**, built using **Streamlit**. It leverages the **Ollama API** to process user inputs and generate real-time responses. 🚀  

---

## 📌 Features
- ✅ **Interactive chatbot** with Streamlit  
- ✅ **AI responses** using the Deepseek R1 model  
- ✅ **Local execution** with Ollama API  
- ✅ **Real-time conversation support**  

---

## 🛠️ Installation & Setup

### **1️⃣ Install Dependencies**
First, ensure you have **Python** and **Git** installed. Then, create a virtual environment and install the required dependencies:

```sh
# Create a virtual environment (optional)
python -m venv myenv
source myenv/bin/activate  # macOS/Linux
myenv\Scripts\activate     # Windows

# Install required packages
pip install streamlit requests

### **2️⃣ Install Ollama and Deepseek R1 Model**
Make sure you have Ollama installed. You can install it using:

sh
Kopyala
Düzenle
# Install Ollama (if not installed)
winget install Ollama  # Windows
brew install ollama    # macOS
Now, download and run the Deepseek R1 model:

sh
Kopyala
Düzenle
ollama pull deepseek-r1
ollama serve
This will start the Ollama API at http://localhost:11434.

### **3️⃣ Run the Project**
Now, you can start the Streamlit application:

sh
Kopyala
Düzenle
streamlit run app.py
Once the server starts, open the generated URL in your browser and start chatting! 🎉

🔗 Technologies Used
Python 🐍
Streamlit 🖥️
Ollama API 🌍
Deepseek R1 Model 🤖
💡 Contributing
If you’d like to contribute:

Fork the repository 🍴
Add a feature or fix a bug 🛠️
Submit a Pull Request (PR)! 🚀
📄 License
This project is licensed under the MIT License. 🎓

yaml
Kopyala
Düzenle

---

### **How to Add this README to Your GitHub Repository**
After creating the `README.md` file, you can add it to your GitHub repo using:

```sh
git add README.md
git commit -m "Added README file 📜"
git push origin main
