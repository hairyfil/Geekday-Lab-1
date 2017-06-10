import os
from flask import Flask

BLUE = "#00ccff"
COLOR = BLUE

app = Flask(__name__)

@app.route('/')
def mainmenu():

    Page_Header     = "<HTML><HEAD></HEAD><BODY bgcolor={}><CENTER><br><br><hr><H1>Main Menu</H1><hr>\n<br><br>".format(COLOR)
    Page_Footer     = "<hr></BODY></HTML>\n"
    Page_Mid        = """<TABLE>\n<TH>Session #</TH>\n<TH>Session Title</TH>\n<TH>Time</TH>\n<TH>Presenter</TH>\n<TH>Session Description</TH>\n</TR>\n"""
    Page_FloorPlan  = """<br><br><hr><H2>FLOORPLAN</H2><img src="static/floorplan.jpg"><br><br>"""

    file = open("sessions.txt", "r")

    for line in file.readlines():
        currentline = line.split(",")
        Page_Mid += "<TR>\n"
        Page_Mid += "<TD>" + currentline[0] + "</TD>\n"
        Page_Mid += "<TD>" + currentline[1] + "</TD>\n"
        Page_Mid += "<TD>" + currentline[2] + "</TD>\n"
        Page_Mid += "<TD>" + currentline[3] + "</TD>\n"
        Page_Mid += "<TD>" + currentline[4] + "</TD>\n"

    Page_Mid += "</TR></TABLE>\n"

    file.close()

    return Page_Header + Page_Mid + Page_FloorPlan + Page_Footer

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
