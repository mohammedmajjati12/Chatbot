async function func() {
    const input = document.getElementById("PW");
    const pw = input.value;

    const myMsg = document.createElement("div");
    myMsg.className = "msg me";
    myMsg.innerText = pw;
    chat.appendChild(myMsg);

    input.value = "";

    const typingMsg = document.createElement("div");
    typingMsg.className = "msg bot";
    typingMsg.innerText = "écrire...";
    chat.appendChild(typingMsg);

    chat.scrollTop = chat.scrollHeight;

    const response = await fetch("https://ai-chat-gx6hwa-production.up.railway.app/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ pw })
    });

    const data = await response.json();

    typingMsg.innerText = data.res;

    chat.scrollTop = chat.scrollHeight;
  }
