# Readme zur BA "Entwicklung eines Python basierten Chatbots für Fälle mit wenig Anwendungsdaten"

Lorenz Ritter von Stein - August 2022 

BESCHREIBUNG

Dieses Projekt erweitert einen in Amazon Lex erstellten Chatbot um die Möglichkeit einen Vorlesungsplan zu durchsuchen.  
Diese Readme beschreibt die nötigen Schritte und Voraussetzungen. 

VORAUSSETZUNGEN

 - Es wird ein (potenziell kostenpflichtiger) AWS Account benötigt. 
 - Ein grundlegender Chatbot sollte bereits in Amazon Lex angelegt sein (Wichtig: dieses Projekt nutzt die Lex Console V1)

INHALTE

- lamda_function.py

- Vorlesungsplan.xml

- VorlesungsSuche.zip (Enthält das Pythonfile und den Vorlesungsplan im XML-Format)

SCHRITTE

1) Erstelle in Amazon Lex einen neuen Intent (Beispielsname: "Vorlesungssuche")
2) Erstelle einige sample utterances, die die Nutzer des Bots fragen könnten wenn sie wissen wollen wann 
   die nächste Vorlesung ist (Beispiel: "Wann ist die nächste {Vorlesungstype} Vorlesung?")
Achte dabei darauf, dass du möglichst viele verschiedene Varianten diese Frage zu stellen abdeckst.
   Erstelle im Bereich "Slots" einen neuen Slot (Beispielname: "VorlesungsType"), damit Lex erkennt, dass es sich 
   bei dem genannten Textabschnitt um einen Parameter handelt, den er später an Lambda übergeben muss. (Weitere Infos in der Dokumenation zu Amazon Lex)
   
3) Im Abschnitt "Fulfillment" in der V1 Konsole von Lex den Punkt "AWS Lambda Function" auswählen.
4) Wechsel zu AWS Lambda und durchlaufe die Schritte zum Erstellen einer neuen Funktion. Wähle dabei Python 3.8 als 
Progammiersprache aus.
   
5) Nachdem du die Funktion erstellt hast, wähle auf der linken Seite das Stammverzeichnis aus und klicke anschließend rechts auf "Hochladen von"
lade nun die in diesem Projekt abgelegte .zip Datei hoch. Wähle zum Speichern "Deploy" aus und wechsel wieder zu Lex
   
6) Wähle bei "Lambda function" die eben in AWS Lambda erstellte Funktion aus. Wähle außerdem im Feld "Version or alias" die Option "latest"
7) Der Bot sollte jetzt in der Lage sein auf die Frage "Wann ist meine nächste Informatikvorlesung?" mit der nächst möglichen Vorlesung und dem dazugehörigen Tag + Uhrzeit zu antworten.
Du kannst die Funktion rechts im Bereich "Test Chatbot" ausprobieren. Stelle dafür sicher, dass du vorher auf "Build" klickst. 
Bitte beachte: Damit die Funktion funktioniert, muss ein slot type mit entsprechenden Values angelegt werden. Beispiel: Slot Type "Mögliche Vorlesungen" mit den Values "Informatik" "Videoproduktion" 
und "Produktfotografie" nutze auch hier jeweils Synonyme, um sicherzugehen, dass der Userinput korrekt zugeordnet werden kann.

Weitere Infos zu slot types findest du hier: https://docs.aws.amazon.com/lex/latest/dg/gs2-create-bot-slot-types.html


Dokumentation zur Einrichtung des Bots in Lex: 
https://docs.aws.amazon.com/lex/latest/dg/gs2-create-bot-create.html

Dokumentation für AWS Lambda:
https://docs.aws.amazon.com/lambda/latest/dg/welcome.html#welcome-first-time-user






