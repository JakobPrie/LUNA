import datetime
INTERVALL = 2 # so oft wegen Silvester

def run(luna, profile):
    now = datetime.datetime.now()
    users = luna.local_storage["users"]

    if now.month == 12 and now.day == 24:
        for user in users:
            user["wartende_benachrichtigungen"].append("Frohe Weihnachten, {}!".format(user["name"]))
    elif now.month == 1 and now.day == 1:
        for user in users:
            user["wartende_benachrichtigungen"].append("Ein erfolgreiches neues Jahr wünsch ich dir, {}!".format(user["name"]))

    for user in users:
        try:
            geburtsdatum = user['date_of_birth']
            month = int(geburtsdatum['month'])
            day = int(geburtsdatum['day'])
            if now.month == month and now.day == day:
                user["wartende_benachrichtigungen"].append("Alles gute zum Geburtstag, {}!".format(user["name"]))
                for other_user in luna.local_storage["users"]:
                    if other_user != user:
                        other_user["wartende_benachrichtigungen"].append("Denk dran, {} hat heute Geburtstag!".format(user["name"]))
        except KeyError:
            '''Do nothing'''

        # "fremde" Geburtstage laden
        with open(luna.path + '/resources/users/' + user[name] + '/other_informations/birthdays.json', 'r') as config_file:
            foreign_birthdays = json.load(config_file)
        for item in foreign_birthdays:
            geburtsdatum = item['date_of_birth']
            month = int(geburtsdatum['month'])
            day = int(geburtsdatum['day'])
            if now.month == month and now.day == day:
                for user in luna.local_storage["users"]:
                    user["wartende_benachrichtigungen"].append("Denk dran, {} hat heute Geburtstag!".format(item))
