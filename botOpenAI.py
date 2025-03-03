import openai
from config import OPEN_AI_KEY

# Set your OpenAI API key
client = openai.OpenAI(api_key = OPEN_AI_KEY)
messages = [
    {"role": "system", "content": """
     kamu adalah Hutao dari Genshin Impact! Disini kamu sebagai admin bot karakter review ini. 
     - Jika ada input yang menanyakan build atau review karakter, arahkan ke /help. Dan jawab dengan candaan harga diri tinggi.
     - Jika ada input yang asal asalan arahkan ke /help dan kamu jawab dengan marah dan ngajak berantem.
     - Jika ada input yang berisi curhatan jawab dengan playful dan tetap ngasih semangat!."""},
]

def createSystemChat(text):
    messages.append({"role": "user", "content": text})
    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=messages
    )

    ai_response = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ai_response})
    
    print(f"message {len(messages)}")
    if len(messages) > 13:
        user_index = next((i for i, msg in enumerate(messages) if msg["role"] == "user"), None)
        if user_index is not None:
            del messages[user_index]            
        assistant_index = next((i for i, msg in enumerate(messages) if msg["role"] == "assistant"), None)
        if assistant_index is not None:
            del messages[assistant_index]

    return response.choices[0].message.content

# For Testing
# def chat():
#     conversation = []
#     print("Chatbot: Hello! Type 'exit' to end the chat.")

#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == "exit":
#             print("Chatbot: Goodbye!")
#             break

#         conversation.append({"role": "user", "content": user_input})

#         bot_reply = createSystemChat(user_input)
#         print(f"Chatbot: {bot_reply}")

#         conversation.append({"role": "assistant", "content": bot_reply})

# chat()

# Inisialisasi daftar pesan untuk menyimpan riwayat percakapan
# messages = [
#     {"role": "system", "content": "Kamu adalah asisten AI yang membantu pengguna dengan jawaban yang relevan."}
# ]

# while True:
#     # Input dari user
#     user_input = input("Anda: ")

#     # Jika user ingin keluar
#     if user_input.lower() in ["exit", "quit", "keluar"]:
#         print("Terima kasih! Sampai jumpa lagi.")
#         break

#     # Tambahkan input user ke riwayat percakapan
#     messages.append({"role": "user", "content": user_input})

#     # Panggil API OpenAI
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",  
#         messages=messages
#     )

#     # Ambil respons dari AI
#     ai_response = response.choices[0].message.content
#     print(f"AI: {ai_response}")

#     # Simpan respons AI ke dalam riwayat percakapan
#     messages.append({"role": "assistant", "content": ai_response})

#     # Batasi jumlah riwayat percakapan agar tidak terlalu panjang
#     if len(messages) > 10:
#         messages = messages[-10:]  # Hanya simpan 10 pesan terakhir
