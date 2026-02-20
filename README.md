# 🌊 PyFlow - Python Code Editor & Visualizer

**PyFlow** is a modern, feature-rich web application that allows you to write, execute, and visualize Python code with beautiful, colorful flowcharts. Perfect for learning, teaching, and understanding code logic flow.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 👨‍💻 Creator

**Name:** Isha Javed  
**Email:** ishabajwa001@gmail.com  
**Project:** PyFlow - Interactive Python Code Visualizer

---
## Project Demo

Watch the demo video showcasing PyFlow’s features, including code visualization and flowchart generation:
🎥 https://www.youtube.com/watch?v=BDV1FvNiHoA

---

## ✨ Features

### 🎨 **Colorful Flowchart Visualization**
- **Vibrant Color-Coded Nodes:**
  - 🟢 **Green** - Start nodes
  - 🔴 **Red** - End nodes
  - 🔵 **Blue** - Operations (assignments, calculations)
  - 🟠 **Orange** - Input/Output (print, input statements)
  - 🟣 **Purple** - Conditions (if/else, while loops)
  - 🟪 **Purple Variant** - Subroutines (functions)

- **User-Friendly Labels:** Descriptive labels instead of raw code
- **Complete Logic Mapping:** Visualizes loops, conditions, branches, and flow control
- **Interactive Controls:** Pan, zoom in/out, and reset view
- **Responsive Grid Background:** Technical aesthetic with subtle grid overlay

### 💻 **Code Editor**
- **Syntax Highlighting:** Powered by Ace Editor with Dracula theme
- **Auto-Save:** Your code is automatically saved to local storage
- **Python Mode:** Full Python syntax support
- **Clean Interface:** Distraction-free coding environment

### ⚡ **Real-Time Execution**
- **Instant Results:** Execute Python code and see output immediately
- **Error Handling:** Clear error messages for debugging
- **Safe Execution:** Server-side sandboxed execution
- **Terminal-Style Output:** Monospace font with dark terminal aesthetic

### 🎯 **Modern UI/UX**
- **Dark Theme:** Easy on the eyes with a cosmic gradient background
- **Glassmorphism Effects:** Modern, premium design elements
- **Responsive Layout:** Works on desktop, tablet, and mobile
- **Smooth Animations:** Polished micro-interactions and transitions
- **Mobile Menu:** Collapsible navigation for smaller screens

---

## 🛠️ Tech Stack

### Backend
- **Flask** - Lightweight Python web framework
- **PyFlowchart** - Python to flowchart DSL conversion
- **Python 3.8+** - Core language

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with custom properties
- **JavaScript (ES6+)** - Interactive functionality
- **Ace Editor** - Professional code editor
- **Flowchart.js** - SVG flowchart rendering
- **svg-pan-zoom** - Interactive flowchart navigation
- **Ionicons** - Beautiful icon library

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```

3. **Open in Browser**
   Navigate to: **http://localhost:5001**

---

## 🚀 Usage Guide

### 1️⃣ **Editor Page**
- Write or paste your Python code in the editor
- Click **Run** to execute your code
- View output in the terminal-style output panel
- Code is auto-saved to local storage

### 2️⃣ **Flowchart Page**
- Automatically generates from your saved code
- Click **Regenerate** to refresh the flowchart
- Use zoom controls (bottom-right) to navigate:
  - **+** Zoom in
  - **-** Zoom out
  - **⟲** Reset view
- Pan by clicking and dragging the flowchart

### 3️⃣ **About Page**
- View creator information
- Project details and contact

---

## 📁 Project Structure

```
PyFlow/
│
├── app.py                 # Flask backend & API endpoints
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
│
├── static/
│   ├── css/
│   │   └── style.css     # All styling & themes
│   └── js/
│       └── main.js       # Frontend logic & interactivity
│
└── templates/
    ├── base.html         # Base template with navbar
    ├── index.html        # Editor page
    ├── flowchart.html    # Flowchart visualization page
    └── about.html        # About/creator page
```

---

##  Troubleshooting

### Flowchart not generating
- Ensure your Python code has valid syntax
- Check the browser console for errors
- Try clicking the **Regenerate** button

### Code not executing
- Verify Flask server is running (check terminal)
- Check for Python syntax errors in your code
- Ensure port 5001 is not blocked by firewall

### Editor not loading
- Clear browser cache and reload
- Check if Ace Editor CDN is accessible
- Verify JavaScript is enabled in browser

---

## 📝 License

This project is open source and available for educational purposes.

---

##  Acknowledgments

- **Ace Editor** - Code editor component
- **Flowchart.js** - Flowchart rendering library
- **PyFlowchart** - Python to flowchart conversion
- **Flask** - Web framework
- **Ionicons** - Icon library

---

## 📧 Contact

For questions, suggestions, or feedback:

**Isha Javed**  
📧 Email: ishabajwa001@gmail.com

---


