# 🕵️‍♂️ Steganography CLI Tool

### *Hide secrets in plain sight… because encryption alone is too mainstream.*

Ever wanted to **hide a message inside an image** like a movie hacker?
Well… welcome to the club. 😎

This project is a **simple Python-based steganography tool** that hides secret messages inside images using **LSB (Least Significant Bit) encoding**.

To the human eye, the image looks exactly the same.
But underneath the pixels… your **secret message is chilling quietly**.

---

# 🎯 What This Tool Does

This tool allows you to:

✔ Hide a message inside an image

✔ Extract the hidden message from an encoded image

✔ Use a clean **command-line interface (CLI)**

✔ Learn how **binary, pixels, and data encoding** work together

Basically:

```
Normal Image + Secret Message
            ↓
      Encoded Image
            ↓
Someone with the decoder can extract the message
```

No magic. Just **clever bit manipulation**.

---

# 🧠 What You Will Learn From This Project

This project was built while learning and experimenting with:

* Binary data representation
* ASCII → Binary conversion
* Image pixel manipulation
* LSB steganography
* Python CLI tools using `argparse`
* Modular Python project structure
* Basic GitHub project organization

If you're learning **Python or cybersecurity**, this is a great beginner project to understand how data can be hidden in media files.

---

# 📦 Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/steganography-tool.git
```

Move into the folder:

```
cd steganography-tool
```

Install dependencies:

```
pip install -r requirements.txt
```

The only dependency used:

```
Pillow
```

---

# ⚙️ How It Works

Every pixel in an image has **3 color channels**:

```
R (Red)
G (Green)
B (Blue)
```

Each channel is **8 bits**:

```
Example Pixel

R = 10110110
G = 11001001
B = 01101100
```

Instead of changing the whole color value, we only change the **last bit (LSB)**.

Example:

```
Original
R = 10110110

Hide bit = 1

New value
R = 10110111
```

The color change is **so tiny the human eye can't detect it**.

Each pixel stores:

```
3 bits
(R + G + B)
```

So an image with:

```
1000 pixels
```

can store:

```
3000 bits of secret data
```

Sneaky, right?

---

# 🔐 Encoding a Message

Hide a message inside an image.

```
python main.py encode -i input_image.png -m "Your secret message"
```

Example:

```
python main.py encode -i cat.png -m "Hello agent"
```

Output:

```
encoded.png
```

Your secret message is now hidden inside the image.

---

# 🔎 Decoding a Message

Extract the hidden message.

```
python main.py decode -i encoded.png
```

Output:

```
Hidden message: Hello agent
```

Mission accomplished.

---

# 🗂 Project Structure

```
steganography-tool
│
├── main.py        # CLI interface
├── encoder.py     # message hiding logic
├── decoder.py     # message extraction logic
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚠️ Important Notes

This is a **learning project** meant to demonstrate how steganography works.

It is **not designed for real-world secure communication**.

Reasons:

* Images can be recompressed
* Metadata may change
* Platforms like WhatsApp or Instagram compress images

Which would **destroy the hidden data**.

But as a **learning tool**, it's perfect.

---

# 🚀 Future Improvements

Possible upgrades:

* Support for **larger payloads**
* Randomized pixel encoding
* Password-based steganography
* Support for multiple image formats
* GUI version
* Detect hidden data

---

# 🧑‍💻 Author

Built as part of a **Python + cybersecurity learning journey**.

If you're also learning security tools, networking, or Python — feel free to fork the project and experiment.

---

# 🧪 Fun Thought

Your cat picture might not just be a cat picture.

It might be:

```
a cat
with secrets
inside the pixels
```

Steganography is basically **whispering through images**.

Pretty cool, right?
