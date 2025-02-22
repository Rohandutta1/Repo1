from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"

    # Get server time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    server_time = ist_time.strftime("%Y-%m-%d %H:%M:%S.%f")

    # Run top command and get output
    top_output = subprocess.getoutput("top -b -n 1")

    # Display output
    return f"""
    <pre>
    Name: Rohan Dutta
    Username: {username}
    Server Time (IST): {server_time}

    TOP output:
    {top_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
