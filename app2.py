import os
from flask import Flask

BLUE = "#33ccff"
COLOR = BLUE

app = Flask(__name__)

@app.route('/')
def mainmenu():

    Page_Header     = "<HTML><HEAD></HEAD><BODY bgcolor={}><CENTER><HR><H1>Main Menu</H1><HR>\n<br><br>".format(COLOR)
    Page_Footer     = "</BODY></HTML>\n"
    Page_Mid        = """<HR><TABLE>\n<TH>Session #</TH>\n<TH>Session Title</TH>\n<TH>Time</TH>\n<TH>Presenter</TH>\n<TH>Session Description</TH>\n</TR>\n"""
    Page_FloorPlan  = """<br><br><H2>FLOORPLAN</H2><img src="static/floorplan.jpg"><br><br>"""

    with open("sessions.txt", "r") as filestream:
        for line in filestream:
            currentline = line.split(",")
            Page_Mid += "<TR>\n"
            Page_Mid += "<TD>" + currentline[0] + "</TD>\n"
            Page_Mid += "<TD>" + currentline[1] + "</TD>\n"
            Page_Mid += "<TD>" + currentline[2] + "</TD>\n"
            Page_Mid += "<TD>" + currentline[3] + "</TD>\n"
            Page_Mid += "<TD>" + currentline[4] + "</TD>\n"

    Page_Mid += "</TR></TABLE>\n"

    return Page_Header + Page_Mid + Page_FloorPlan + Page_Footer

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
