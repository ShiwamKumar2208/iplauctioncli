# 🏏 IPL Auction Simulator (CLI + Web Speaker)

A real-time IPL-style auction simulator built from scratch using Python.

This project simulates a **multi-team IPL auction** with:

* Dynamic bidding system
* AI-driven team strategies
* Realistic price increments
* Optional web-based voice commentary



## 🚀 Features

### 🔥 Core Auction Engine

* Turn-based bidding (no fake mirroring)
* Dynamic bid increments:

  * ₹0.25 Cr (≤ 5 Cr)
  * ₹0.5 Cr (5–10 Cr)
  * ₹1 Cr (> 10 Cr)
* Proper auction flow:

  * Opening bids
  * Competitive bidding
  * Final hammer



### 🤖 AI Teams (8 Teams)

Each team has its own personality:

| Team | Strategy            |
| ---- | ------------------- |
| SRH  | Balanced (User)     |
| RCB  | Aggressive          |
| MI   | Star-focused        |
| CSK  | Experienced players |
| KKR  | All-rounders        |
| DC   | Youth               |
| GT   | Balanced            |
| PBKS | Random/chaotic      |



### 🧠 AI Behavior

* Value-based bidding (not random spam)
* Can bid beyond 10–20 Cr for top players
* Slight overpay for realism
* Strategy-based decision making
* Human-like randomness



### 🔊 Web Speaker (Optional)

* Python sends auction events to a local server
* Browser speaks events using native speech API
* Fully optional (auction runs without it)



## 📂 Project Structure

```
ipl-auction/
│
├── auction.py          # Main auction engine
├── ai.py               # AI decision logic
├── speaker.py          # Sends messages to web speaker
│
├── LOP/
│   └── LOP.json        # Player dataset
│
├── server.js           # Web speaker backend
├── index.html          # Browser speech UI
│
└── README.md
```



## ⚙️ Setup

### 1️⃣ Python setup

```bash
pip install requests
```



### 2️⃣ Node.js setup (for speaker)

```bash
npm init -y
npm install express
```



### 3️⃣ Run web speaker (optional)

```bash
node server.js
```



### 4️⃣ Serve frontend

```bash
python -m http.server 8000
```

Open:

```
http://localhost:8000/index.html
```



### 5️⃣ Run auction

```bash
python auction.py
```



## 🎮 Controls

| Input   | Action       |
| ------- | ------------ |
| `y`     | Bid          |
| `Enter` | Skip         |
| `q`     | Quit auction |



## 🧪 Example Flow

```
MI opens at 2.00 Cr
RCB raises to 2.25 Cr
CSK raises to 2.50 Cr
SRH raises to 2.75 Cr
KKR raises to 3.00 Cr
...
🏆 SOLD to MI for 9.50 Cr
```



## 🧠 Design Philosophy

This project is built with:

* Minimal dependencies
* Full control over logic
* Realistic simulation over randomness
* Expandable architecture



## 🔥 Future Plans

* [ ] WebSocket real-time UI
* [ ] Full auction dashboard
* [ ] Squad composition logic (team needs)
* [ ] Player demand / hype system
* [ ] RTM (Right To Match)
* [ ] Retentions



## 💀 Known Limitations

* No squad balance logic yet
* AI doesn't consider team composition (yet)
* CLI-based (UI coming next)



## 👤 Author

Built by someone who believes:

> *"If I can't build it, I don't understand it."*



## ⭐ If you like this

Star it, fork it, break it, improve it.



## ⚡ Reality Check

This is not just a script.

It’s the base of a:
👉 **full IPL auction simulation engine**


