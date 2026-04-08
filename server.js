const express = require("express");
const app = express();

app.use(express.json());

// 🔥 FIX: allow browser access
app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Headers", "*");
  next();
});

let lastText = "";

// receive text from python
app.post("/speak", (req, res) => {
  lastText = req.body.text;
  console.log("SPEAK:", lastText);
  res.sendStatus(200);
});

// send to browser
app.get("/last", (req, res) => {
  res.json({ text: lastText });
  lastText = "";
});

// homepage (optional)
app.get("/", (req, res) => {
  res.send("🎤 Auction Speaker Running");
});

app.listen(3000, () => {
  console.log("🚀 Server running on http://localhost:3000");
});