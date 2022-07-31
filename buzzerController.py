from flask import Flask, render_template
import serial

#open serial port
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

app = Flask(__name__)
@app.route('/')
#initial start up when the website is first accessed
def startup():
    return render_template('index.html', buzzerState = "off")

@app.route("/<toggle>")
def toggle_buzzer(toggle):
    buzzerState = "OFF"
    if toggle == "on":
        buzzerState = "ON"
        ser.write(b'1')
    elif toggle == "off":
        buzzerState = "OFF"
        ser.write(b'0')
    templateData = {
        'buzzerState': buzzerState
        }
    #pass the data to HTML
    return render_template('index.html', **templateData)

#Main function to set up the serial com, the websever, and start the service
if __name__ == "__main__":
    ser.flush()
    app.run(host='0.0.0.0', port=8080, debug=True)
