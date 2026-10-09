🤖 GenAI-app

GenAI-app adalah sebuah aplikasi web interaktif berbasis AI Agent. Aplikasi ini dirancang untuk menjawab pertanyaan dan memberikan informasi dengan memanfaatkan kecerdasan model Google Gemini, yang diperkuat dengan kemampuan mencari data aktual melalui internet (DuckDuckGo) dan Wikipedia.

Semua ini dibangun dalam antarmuka yang cepat dan ramah pengguna menggunakan Streamlit.

Link: https://genai-app-lxswst6panxqsj7kk57zmx.streamlit.app/

<img width="976" height="730" alt="Screenshot 2026-10-07 074446" src="https://github.com/user-attachments/assets/44c745b3-82fc-452d-a8b1-7a13b763b82c" />
<img width="1072" height="438" alt="Screenshot 2026-10-07 074509" src="https://github.com/user-attachments/assets/610780b6-b043-4c17-ae54-d06ac4d535d3" />
<img width="1008" height="861" alt="Screenshot 2026-10-07 074519" src="https://github.com/user-attachments/assets/acf4329b-0950-49ea-9dd1-485e21df6c39" />
<img width="959" height="778" alt="Screenshot 2026-10-07 074527" src="https://github.com/user-attachments/assets/0c9e22aa-447a-4722-ae6d-554c584e0754" />


🛠️ Library yang Digunakan

Aplikasi ini dibangun menggunakan ekosistem Python dengan library utama sebagai berikut:

Streamlit: Framework untuk membuat antarmuka web (UI) interaktif secara instan hanya dengan Python.

LangChain: Framework utama untuk membangun aplikasi berbasis Large Language Models (LLM). Di sini digunakan untuk mengatur alur Agent dan menyimpan memori percakapan (InMemoryChatMessageHistory, RunnableWithMessageHistory).

langchain-google-genai: Ekstensi LangChain untuk mengintegrasikan model AI Google Gemini (ChatGoogleGenerativeAI) sebagai "otak" utama aplikasi.

LangChain Community Tools:

DuckDuckGoSearchResults: Memungkinkan AI untuk melakukan pencarian di web secara real-time.

WikipediaQueryRun & WikipediaAPIWrapper: Memberikan akses ke AI untuk mencari artikel dan informasi langsung dari Wikipedia.

os: Modul bawaan Python untuk mengelola environment variables (seperti API Key).

📋 Prasyarat

Pastikan kamu sudah menginstal perangkat lunak berikut di komputermu:

Python (versi 3.8 atau lebih baru)

Google Gemini API Key. (Dapatkan secara gratis di Google AI Studio)

🚀 Instalasi & Konfigurasi

Ikuti langkah-langkah berikut untuk menjalankan aplikasi ini secara lokal:

Clone repositori ini:

git clone https://github.com/bimaindr/GenAi-app.git
cd GenAi-app


Instal library yang dibutuhkan:
Pastikan kamu berada di dalam direktori proyek, lalu jalankan:

pip install streamlit langchain langchain-community langchain-google-genai duckduckgo-search wikipedia


(Atau pip install -r requirements.txt jika kamu sudah membuat filenya).

Atur Environment Variables (API Key):
Kamu bisa mengatur API Key di dalam file kode langsung, atau lebih aman menggunakan terminal/file .env:

export GOOGLE_API_KEY="masukkan_api_key_gemini_kamu_di_sini"


Jalankan Aplikasi:
Jalankan perintah Streamlit berikut di terminal:

streamlit run app.py


(Ganti app.py dengan nama file utama Python kamu jika berbeda).

Akses Aplikasi:
Streamlit akan otomatis membuka tab baru di browsermu, atau kamu bisa mengaksesnya secara manual melalui URL http://localhost:8501.

🤝 Kontribusi

Saran, perbaikan, dan fitur baru sangat diterima. Silakan fork repositori ini dan buat Pull Request!

📝 Lisensi

Dibuat dengan oleh bimaindr.
