from flask import Flask
from lifxlan import BLUE, COLD_WHITE, CYAN, GOLD, GREEN, LifxLAN, \
    ORANGE, PINK, PURPLE, RED, WARM_WHITE, WHITE, YELLOW

app = Flask(__name__)

colors = {
    "red": RED,
    "orange": ORANGE,
    "yellow": YELLOW,
    "green": GREEN,
    "cyan": CYAN,
    "blue": BLUE,
    "purple": PURPLE,
    "pink": PINK,
    "white": WHITE,
    "cold_white": COLD_WHITE,
    "warm_white": WARM_WHITE,
    "gold": GOLD
}


@app.route('/broadcast/red')
def broadcast_red():
    lifxlan = LifxLAN()
    color = colors["red"]
    print(color)
    lifxlan.set_color_all_lights(color, rapid=True)
    return "room is now red"


@app.route('/broadcast/blue')
def broadcast_blue():
    lifxlan = LifxLAN()
    color = colors["blue"]
    print(color)
    lifxlan.set_color_all_lights(color, rapid=True)
    return "room is now blue"
