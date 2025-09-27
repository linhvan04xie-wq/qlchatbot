import requests

def chat_with_bot():
    user_id = "u1"

    while True:
        message = input("Bạn: ")
        if message.lower() in ["exit", "quit", "bye"]:
            print("Thoát chat!")
            break

        response = requests.post(
            "http://localhost:5000/chat",
            json={"userId": user_id, "message": message}
        )

        if response.status_code == 200:
            data = response.json()
            print("Bot:", data["reply"])
        else:
            print("❌ Lỗi:", response.text)

if __name__ == "__main__":
    chat_with_bot()
