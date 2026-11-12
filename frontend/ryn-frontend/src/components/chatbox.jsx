import { useState } from "react";
import axios from "axios";

function ChatBox() {
  const [messages, setMessages] = useState([
    { from: "bot", text: "Hi, I'm Ryn! Ask me anything 🤖" },
  ]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    const newMessages = [...messages, { from: "user", text: input }];
    setMessages(newMessages);

    try {
      const res = await axios.post("http://localhost:5000/chat", {
        message: input,
      });
      setMessages([...newMessages, { from: "bot", text: res.data.response }]);
    } catch (err) {
      console.error(err);
      setMessages([...newMessages, { from: "bot", text: "Error getting response 😢" }]);
    }

    setInput("");
  };

  const resetChat = async () => {
    try {
      await fetch("http://localhost:5000/reset", { method: "POST" });
      setMessages([{ from: "bot", text: "Hi, I'm Ryn! Ask me anything 🤖" }]);
    } catch (err) {
      console.error("Failed to reset chat:", err);
    }
  };

  return (
    <div>
      <div className="chat-container">
        {messages.map((msg, i) => (
          <div key={i} className={msg.from}>
            {msg.text}
          </div>
        ))}
      </div>

      <div className="input-box">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Type your message..."
        />
        <button onClick={sendMessage}>Send</button>
        <button onClick={resetChat} style={{ marginLeft: "10px" }}>Reset</button>
      </div>
    </div>
  );
}

export default ChatBox;
