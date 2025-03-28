# 🎮 Guess the Number Game (GUI Version)

A fun number-guessing game built using **Python** and **Tkinter** with a user-friendly interface.  
Try to guess the correct number between **1 and 100**! 🔢✨  

---

## 🚀 Features
✅ **Interactive UI** – Built with Tkinter for a smooth gaming experience  
✅ **Keyboard Support** – Press **Enter** to submit a guess instead of clicking the button  
✅ **Hint Animation** – The hint message smoothly fades in for better visibility  
✅ **Restart Anytime** – Restart the game at any moment without needing to win  
✅ **Win Message in UI** – Displays a win message in the interface when you guess correctly  

---

## 📥 How to Download and Run the Project

### Clone the Repository
```
git clone https://github.com/yourusername/guess-the-number.git
```

### Navigate to the Project Folder

```
cd guess-the-number
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Run the Game
```
python app.py
```

## 🌍 Deploying the App Online (Heroku)
If you want to deploy this app on Heroku, follow these steps:

Login to Heroku
```
heroku login
```

Create a New App
```
heroku create your-app-name
```

Push the Code to Heroku
```
git add .
git commit -m "Initial commit"
git push heroku main
```

Run the App
```
heroku ps:scale web=1
heroku open
```

📌 Requirements
Python 3.x, Tkinter (Built-in with Python) and Flask (For web integration)
