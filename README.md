<div align="center">

# 📁 Tayronuk File Sorter  
**Organize your chaos in milliseconds.**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Automation-File%20Management-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Open%20Source-Yes-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" />
</p>

</div>

---

## 🚀 Overview

**Tayronuk File Sorter** is a lightweight Python automation tool that eliminates file clutter by automatically organizing files into categorized folders based on file type.

Ideal for cleaning up **Downloads**, **Desktop**, or any directory that gets messy over time.

---

## ✨ Key Features

- 🧠 **Smart Sorting** — Automatically categorizes files by extension  
- 🛠️ **Customizable Rules** — Easily add or modify supported file types  
- 🔒 **Safety Checks** — Skips directories and avoids moving the script itself  
- ⚡ **Fast & Lightweight** — Uses only Python’s standard library

---

## 📂 Project Structure

```text
Tayronuk-File-Sorter/
│
├── main.py
│
└── example/
    ├── Images/
    ├── Documents/
    ├── Videos/
    ├── Music/
    ├── Archives/
    ├── Executables/
    └── Others/
```

## 🛠️ Installation & Usage

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/tayronuk/Tayronuk-File-Sorter.git](https://github.com/tayronuk/Tayronuk-File-Sorter.git)
    cd Tayronuk-File-Sorter
    ```

2.  **Run the script**
    ```bash
    python main.py
    ```

## ⚙️ Configuration (Pro Tip)

By default, the script sorts the `example` folder. To sort your **real Downloads folder**, edit `main.py`:

```python
# --- CONFIGURATION ---
# TARGET_FOLDER = "example"  <-- Comment this out

# Uncomment this line:
TARGET_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")

```
<div align="center"> <sub>Built with ❤️ by Tayronuk</sub> </div>
