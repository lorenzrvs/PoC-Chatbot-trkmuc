import json
import xml.etree.ElementTree as ET
from datetime import datetime


def keyfind(input_dict, value):
    for key, val in input_dict.items():
        if val == value: return key
    return "None"


def timecheck(stunde, vorlesungsstunde, minute, vorlesungsminute):
    if stunde < vorlesungsstunde:
        return 1
    elif stunde == vorlesungsstunde and minute <= vorlesungsminute:
        return 1
    else:
        return 0


def vlAbfrage(intent):
    wochentag = datetime.today().weekday()  # gibt den Wochentag aus. 0 = Montag 1 = Dienstag usw.
    zeit = str(datetime.now())
    stunde = int(zeit[
                 11:13]) + 2  # sliced den Timecode auf die Stunde. +2 um auf MEZ zu kommen. Hinweis: potenzielle Gefahr wegen Sommer-/Winterzeit!
    minute = int(zeit[14:16])  # sliced den Timecode auf die Minute.

    tree = ET.parse('Vorlesungsplan.xml')
    root = tree.getroot()

    tagdict = dict()
    tagdict[0] = "Montag"
    tagdict[1] = "Dienstag"
    tagdict[2] = "Mittwoch"
    tagdict[3] = "Donnerstag"
    tagdict[4] = "Freitag"

    ersterTermin = dict()
    x = 0
    y = 0
    vlAnzahl = root.findall((".//*[@vlName='%s']" % intent))

    for Vorlesung in root.findall(
            'Vorlesung'):  # weist den variablen die jeweiligen Werte der aktuell itterierten Vorlesung zu.
        uhrzeit = Vorlesung.find('Uhrzeit').text
        name = Vorlesung.find("Name").text
        semester = Vorlesung.find("Semester").text
        vorlesungstag = Vorlesung.find("Wochentag").text
        vorlesungsstunde = int(uhrzeit[0:2])
        vorlesungsminute = int(uhrzeit[3:5])

        if name == intent:
            for Vorlesung in root.findall('Vorlesung'):
                check = timecheck(stunde, vorlesungsstunde, minute, vorlesungsminute)  # Gleicht die Zeitpunkte ab.

                if name == intent:  # unabhängig davon welche VL gerade itteriert wird, wird der Vorlesungstag im dict abgespeichert.
                    ersterTermin[x] = vorlesungstag
                    x += 1

                if name == intent and wochentag < keyfind(tagdict,
                                                          vorlesungstag):  # aktueller Tag < Tag der Vorlesung -> gib diese als nächste aus.
                    antwort = ("Die nächste " + name + " Vorlesung ist am " + vorlesungstag + " um " + str(
                        vorlesungsstunde) + ":" + str(vorlesungsminute))
                    y = 1
                    break

                elif name == intent and wochentag == keyfind(tagdict,
                                                             vorlesungstag) and check == 1:  # aktueller tag = Vorlesungstag -> prüfe, ob Uhrzeit < oder >
                    antwort = ("Die nächste " + name + " Vorlesung ist am " + vorlesungstag + " um " + str(
                        vorlesungsstunde) + ":" + str(vorlesungsminute))
                    y = 1
                    break

        if y == 1:
            break

    if y == 0:
        for Vorlesung in root.findall("Vorlesung"):
            name = Vorlesung.find("Name").text
            vorlesungstag = Vorlesung.find("Wochentag").text
            uhrzeit = Vorlesung.find('Uhrzeit').text
            vorlesungsstunde = int(uhrzeit[0:2])
            vorlesungsminute = int(uhrzeit[3:5])

            if name == intent:
                antwort = ("Die nächste " + name + " Vorlesung ist am " + vorlesungstag + " um " + str(
                    vorlesungsstunde) + ":" + str(vorlesungsminute))
                break

    return antwort


def lambda_handler(event, context):
    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText"
            }
        }
    }
    print(event)
    intent = str(event["currentIntent"]["slots"]["VorlesungsType"])
    response["dialogAction"]["message"]["content"] = vlAbfrage(intent)

    return response