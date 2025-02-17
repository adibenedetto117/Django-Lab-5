# Django-Lab-5
## By Anthony DiBenedetto

This simple Django app provides two routes:  
- `/`  Returns a JSON response `{ "Message": "Hello World!" }`.  
- `/page/`  Displays an HTML page with **Hello World!** in bold.  

## **How to Run**
Make sure you have **Python** installed and a virtual environment with Django.

### **Steps**
1. Clone the repo:  
   ```sh
   git clone https://github.com/adibenedetto117/Django-Lab-5.git
   ```
2. Navigate to the project:  
   ```sh
   cd Django-Lab-5
   ```
3. Create a virtual environment (if not already set up):  
   ```sh
   python -m venv venv
   ```
4. Activate the virtual environment:  
   - **Mac/Linux**:  
     ```sh
     source venv/bin/activate
     ```
   - **Windows**:  
     ```sh
     venv\Scripts\activate
     ```
5. Install Django:  
   ```sh
   pip install django
   ```
6. Apply migrations:  
   ```sh
   python manage.py migrate
   ```
7. Start the server:  
   ```sh
   python manage.py runserver
   ```

### **Access the App**
- **JSON Response**: Open `http://127.0.0.1:8000/`
- **HTML Page**: Open `http://127.0.0.1:8000/page/`

### **Stop the Server**
Press **CTRL + C** in the terminal.

