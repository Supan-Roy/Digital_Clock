from tkinter import Tk, Label, Frame
import time
import requests

# Weather
API_KEY = "db78aafd22380f9bd49c55d0365211f5"  # Powered by OpenWeatherMap
CITY = "Bagerhat"

def get_temperature():
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        temp = data['main']['temp']
        return f"{round(temp)}°C"
    except:
        return "N/A"

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    current_day = time.strftime("%A")
    current_date = time.strftime("%B %d, %Y")
    temperature = get_temperature()

    d_clock.config(text=current_time)
    d_date.config(text=f"{current_day}, {current_date}")
    d_temp.config(text=f"{CITY} | 🌡 {temperature}")

    root.after(100, update_time)

root = Tk()
root.title("Digital Clock")
root.geometry("750x320")
root.configure(bg="#121212")
root.eval('tk::PlaceWindow . center')

clock_frame = Frame(root, bg="#1f1f2e", bd=10, relief="ridge")
clock_frame.pack(expand=True, fill="both", padx=20, pady=20)

d_clock = Label(clock_frame, font=("Segoe UI", 72, "bold"), bg="#1f1f2e", fg="#00ffcc", pady=10)
d_clock.pack()

d_date = Label(clock_frame, font=("Agency FB", 25, "bold"), bg="#1f1f2e", fg="#ff66ff")
d_date.pack()

d_temp = Label(clock_frame, font=("Segoe UI", 18, "bold"), bg="#1f1f2e", fg="#ffaa00")
d_temp.pack()

update_time()
root.mainloop()
