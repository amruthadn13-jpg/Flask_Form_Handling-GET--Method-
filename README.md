# Flask_Form_Handling-GET--Method-
# Flask Form Handling (GET Method)

## 📌 Project Overview

This project demonstrates how to create a simple web form using Flask and handle user input using the **GET method**.

It is part of my backend development learning journey.

---

## 🚀 Features

* HTML form to collect user input (name and age)
* Data sent using GET method
* Flask backend to process input
* Dynamic response displayed to user

---

## 🛠️ Technologies Used

* Python
* Flask
* HTML

---

## 📂 Project Structure

```
flask-form-get-method/
│
├── app.py
└── templates/
    └── form.html
```

---

## ⚙️ How It Works

1. User opens the home page.
2. Enters name and age in the form.
3. Form submits data using GET method.
4. Data is sent via URL:

   ```
   /result?username=Amrutha&age=20
   ```
5. Flask retrieves data using:

   ```
   request.args.get()
   ```
6. Displays the result on the browser.

---

## ▶️ How to Run the Project

1. Install Flask:

   ```
   pip install flask
   ```

2. Run the application:

   ```
   python app.py
   ```

3. Open browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

---

## 🧠 Concepts Learned

* Flask routing
* HTML forms
* GET method
* request.args in Flask
* Passing data between frontend and backend

---

## 🎯 Future Improvements

* Add POST method support
* Improve UI with CSS
* Add validation for inputs

---

## 👨‍💻 Author

Amrutha D N
