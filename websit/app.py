from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ===============================
# MySQL Configuration
# ===============================
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'jayaraj@2006'  # <-- change this
app.config['MYSQL_DB'] = 'fullstack_db'

mysql = MySQL(app)

# ===============================
# Home Route
# ===============================
@app.route('/')
def home():
    return render_template("index.html")

# ===============================
# Add User
# ===============================
@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        username = data['username']
        email = data['email']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO users (username, email) VALUES (%s, %s)",
            (username, email)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({"message": "User Added Successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})

# ===============================
# Get Users
# ===============================
@app.route('/get_users', methods=['GET'])
def get_users():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        cur.close()

        users = []
        for row in rows:
            users.append({
                "id": row[0],
                "username": row[1],
                "email": row[2]
            })

        return jsonify(users)

    except Exception as e:
        return jsonify({"error": str(e)})

# ===============================
# Run App
# ===============================
if __name__ == "__main__":
    app.run(debug=True)
