from flask import Flask, request

app = Flask(__name__)

MAX_SPEED = 100

def set_motor_speed(speed):
    # For now, just print (safe testing)
    print(f"[MOTOR COMMAND] Left: {speed[0]}, Right: {speed[1]}")

@app.route("/")
def home():
    return """
    <h1>Robot Controller</h1>
    <p><a href="/move?y=1">Forward</a></p>
    <p><a href="/move?y=0">Stop</a></p>
    <p><a href="/move?y=-1">Backward</a></p>
    """

@app.route("/move")
def move():
    y = float(request.args.get("y", 0))

    speed_val = int(y * MAX_SPEED)
    speed = [speed_val, speed_val, 0, 0]

    set_motor_speed(speed)

    return f"Command sent: {y}"

app.run(host="0.0.0.0", port=5000)
