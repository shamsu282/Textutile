
# 🛠️ Django TextUtils – Text Analyzer Web App

**TextUtils** is a simple Django-based web application that lets users perform various text transformation operations such as removing punctuation, converting text to uppercase, eliminating newlines, removing numbers, and getting rid of extra spaces.

## 🚀 Features

- ✅ Remove Punctuation  
- 🔠 Convert Text to Uppercase  
- 📤 Remove Newlines  
- 🔢 Remove Numbers  
- ➖ Remove Extra Spaces  

## 📂 Project Structure

```
├── phase1/
│   ├── views.py
│   └── templates/
│       ├── index.html
│       └── analyze.html
├── urls.py
└── manage.py
```

## 🔧 How it Works

1. Visit the homepage (`/`)
2. Enter text in the input box.
3. Select one or more text processing options.
4. Submit and see the transformed text on the result page.

## 🔌 Routes

- `/` – Homepage with input form
- `/analyze` – Processes and displays analyzed text
- `/admin/` – Django admin interface

## 🛠️ Technologies Used

- Python
- Django
- HTML (templates)

## 🏁 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/textutils.git
   cd textutils
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

5. Open your browser and go to `http://127.0.0.1:8000`

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).
