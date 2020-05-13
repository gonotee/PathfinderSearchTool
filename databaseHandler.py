import mysql.connector
import json

class spellSearchHandler():

    # CONSTANTS
    numberOfFormElements = 10

    # The local variable to hold the results of the form (Dictionary)
    formResults = {}

    # Takes a dictionary of results from a form at saves it to the local variable
    def attachForm(self, result):
        if "name" or "level" in result:
            print("Form Accepted")
            for key, values in result.items():
                self.formResults[key] = values
        else:
            return False

    # Assigns default values to values in attached form that are empty strings and adds wildcards to certain values
    # Defaults are a wildcard %
    # Certain values (name, description) are given wildcard values at the beginning and end so query searches for values
    #   that have the search term in them and not just exact matches
    def cleanseForm(self):
        form = self.formResults.items()
        newForm = {}
        for key, values in form:
            if values == "":
                newForm[key] = "%"
            else:
                newForm[key] = values

            if key == "name" or key == "description" or key == "actions" or key == "duration" or key == "target" or key == "tradition" and newForm[key] != "%":
                newForm[key] = "%" + newForm[key] + "%"


        self.formResults = newForm
        form = self.formResults.items()
        for key, values in form:
            print(key + " " + values)

    def executePreparedStatement(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Dpass0509yt!",
            database="pathfinder"
        )
        try:
            mycursor = mydb.cursor(prepared=True)
            stmt = "SELECT * FROM pathfinder.`spells-pf2-v2` WHERE name LIKE ? AND level LIKE ? AND text LIKE ? AND actions LIKE ? AND duration LIKE ? AND targets LIKE ? AND traditions LIKE ?"
            name = str(self.formResults.get("name"))
            level = str(self.formResults.get("level"))
            text = str(self.formResults.get("description"))
            actions = str(self.formResults.get("actions"))
            traits = str(self.formResults.get("traits"))
            range = str(self.formResults.get("range"))
            duration = str(self.formResults.get("duration"))
            targets = str(self.formResults.get("target"))
            traditions = str(self.formResults.get("tradition"))
            mycursor.execute(stmt, (name, level, text, actions, duration, targets, traditions,))
            myresult = mycursor.fetchall()
            print(mydb)
            for row in myresult:
                print(row)
            return myresult
        finally:
            mydb.close()

    def executePreparedSpellFind(self, searchTerm):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Dpass0509yt!",
            database="pathfinder"
        )
        try:
            mycursor = mydb.cursor(prepared=True)
            stmt = "SELECT * FROM pathfinder.`spells-pf2-v2` WHERE name = ?"
            name = searchTerm
            mycursor.execute(stmt, (name,))
            myresult = mycursor.fetchall()
            print(mydb)
            for row in myresult:
                print(row)
            return myresult
        finally:
            mydb.close()







