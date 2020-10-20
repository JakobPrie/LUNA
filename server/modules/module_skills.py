def isValid(text):
    return False


class skills:
    def __init__(self):
        pass

    def get_enumerate(self, array):
        # print(array)
        new_array = []  # array=['Apfel', 'Birne', 'Gemüse', 'wiederlich']
        for item in array:
            new_array.append(item.strip(' '))

        # print(new_array)
        ausgabe = ''
        # print('Länge: {}'.format(len(new_array)))
        if len(new_array) == 0:
            pass
        elif len(new_array) == 1:
            ausgabe = array[0]
        else:
            for item in range(len(new_array) - 1):
                ausgabe += new_array[item] + ', '
            ausgabe = ausgabe.rsplit(', ', 1)[0]
            ausgabe = ausgabe + ' und ' + new_array[-1]
        return ausgabe

    def get_text_beetween(self, start_word, text, end_word='', output='array'):
        ausgabe = []
        index = -1
        start_word = start_word.lower()
        text = text.replace(".", "")
        text = text.split(' ')
        print(start_word)
        print("-----------")
        for i in range(len(text)):
            print(text[i])
            if text[i].lower() == start_word:
                print("gefundend!!!")
                index = i + 1

        print(index)
        if index is not -1:
            if end_word == '':
                while index < len(text):
                    print(ausgabe)
                    ausgabe.append(text[index])
                    index += 1
            else:
                founded = False
                while index <= len(text) and not founded:
                    if text[index] is end_word:
                        founded = True
                    else:
                        ausgabe.append(text[index])
                        index += 1
        if output is 'array':
            return ausgabe
        elif output is 'String':
            ausgabe_neu = ''
            for item in ausgabe:
                ausgabe_neu += item + ' '
            return ausgabe_neu

    def delete_duplications(self, array):
        new_array = list(set(array))
        return new_array

    """
    def assamble_new_items(array, new_items):
        new_array = []
        for item in new_items:
            # Name des items von der Anzahl trennen
            if len(item.split(' ')) > 1:
                # Durch die 1 in der runden Klammer, wird nur beim ersten Space
                # das Wort getrennt. Das ist daher von Vorteil, da wir so später
                # beim Zusammenfügen der Anzahl und des Namens nicht jedes Wort
                # einzeln hinzufügen müssen
                item_name = item.split(' ', 1)[1]
            else:
                item_name = item

            for field in array:
                if len(field.split(' ')) > 1:
                    field_name = field.split(' ', 1)[1]
                else:
                    field_name = field

                # Die folgende if-Abfrage ist notwendig, um auch "Banane" und "Bananen"
                # zusammen zu zählen
                weight = False
                if field_name.lower().rstrip(field_name.lower()[-1]) == item_name.lower():
                    item_name = item_name + "n"
                if field_name.lower() == item_name.lower():
                    # Festlegen der Anzahl des jeweiligen Feldes der beiden Arrays und
                    # des letzten Buchstaben, den wir später noch brauchen werden
                    n_anz = item.split(' ', 1)[0]
                    try:
                        n_item = item.split(' ', 1)[1]
                    except:
                        n_item = item
                    a_anz = field.split(' ', 1)[0]

                    if ('g ' in a_anz or 'kg ' in a_anz) and ('g ' in n_anz or 'kg ' in n_anz):
                        print("Gewichtsindex gefunden")
                        print("g or kg founded")
                        weight = True
                    if 'kg ' in field:
                        a_anz = a_anz * 1000
                        field = field.replace('kg ', ' ')
                    if 'kg ' in item:
                        n_anz = n_anz * 1000
                        item = item.replace('kg ', ' ')
                    print("a_anz und n_anz:")
                    print(a_anz)
                    print(n_anz)
                field = field.replace('g ', ' ')
                item = item.replace('g ', ' ')
                print("Feld und item:")
                print(field)
                print(item)
                print("\n")

            last_letter = item[-1]
            # Bisher war die jeweilige Anzahl (z.B. 2) noch als String (also
            # Zeichen) und nicht als int (also Zahl) gespeichert. Man kann
            # aber nur mit Zahlen rechnen, daher versuche ich anschließend
            # die Strings in Integer zu konvertieren. "try" wird benötigt,
            # da zum Beispiel bei "Creme Legere" das 1. Feld nach dem split
            # keine Zahl, sondern ein Wort ist
            try:
                n_anz = int(n_anz)
            except:
                # keine Zahl? Dann gibt es von dem Item nur eines
                n_anz = 1

            try:
                a_anz = int(a_anz)
            except:
                a_anz = 1

            if type(n_anz) != int:
                n_item = item

            new_anz = n_anz + a_anz
            if not weight:
                print("------------> Es handelt sich ---- NICHT ------ um g or kg")
                item = str(new_anz) + " " + n_item
                if last_letter == "e":
                    item = item + "n"
            else:
                print("------------> Es handelt sich um g or kg")
                identifier = 'g '
                if new_anz >= 1000:
                    new_anz = new_anz / 1000
                    identifier = 'kg '
                item = str(new_anz) + identifier + n_item
            print(item)


        new_array.append(item)
        # folgende Zeile löscht Dopplungen, die durch das Zusammenfügen von "Banane" und "Bananen" zu stande kommt
        new_array = self.delete_duplications(new_array)

        print(f"new_array: {new_array}")
        return new_array
        """

    def assamble_new_items(self, array, new_items):
        new_array = []
        for item in new_items:
            # Name des items von der Anzahl trennen
            if len(item.split(' ')) > 1:
                # Durch die 1 in der runden Klammer, wird nur beim ersten Space
                # das Wort getrennt. Das ist daher von Vorteil, da wir so später
                # beim Zusammenfügen der Anzahl und des Namens nicht jedes Wort
                # einzeln hinzufügen müssen
                item_name = item.split(' ', 1)[1]
            else:
                item_name = item

            for field in array:
                if len(field.split(' ')) > 1:
                    field_name = field.split(' ', 1)[1]
                else:
                    field_name = field

                # Die folgende if-Abfrage ist notwendig, um auch "Banane" und "Bananen"
                # zusammen zu zählen
                if field_name.lower().rstrip(field_name.lower()[-1]) == item_name.lower():
                    item_name = item_name + "n"
                if field_name.lower() == item_name.lower():
                    # Festlegen der Anzahl des jeweiligen Feldes der beiden Arrays und
                    # des letzten Buchstaben, den wir später noch brauchen werden
                    n_anz = item.split(' ', 1)[0]
                    try:
                        n_item = item.split(' ', 1)[1]
                    except:
                        n_item = item
                    a_anz = field.split(' ', 1)[0]
                    last_letter = item[-1]
                    # Bisher war die jeweilige Anzahl (z.B. 2) noch als String (also
                    # Zeichen) und nicht als int (also Zahl) gespeichert. Man kann
                    # aber nur mit Zahlen rechnen, daher versuche ich anschließend
                    # die Strings in Integer zu konvertieren. "try" wird benötigt,
                    # da zum Beispiel bei "Creme Legere" das 1. Feld nach dem split
                    # keine Zahl, sondern ein Wort ist
                    try:
                        n_anz = int(n_anz)
                    except:
                        # keine Zahl? Dann gibt es von dem Item nur eines
                        n_anz = 1

                    try:
                        a_anz = int(a_anz)
                    except:
                        a_anz = 1

                    if type(n_anz) != int:
                        n_item = item

                    new_anz = n_anz + a_anz
                    item = str(new_anz) + " " + n_item

                    if last_letter == "e":
                        item = item + "n"

            new_array.append(item)
            # folgende Zeile löscht Dopplungen, die durch das Zusammenfügen von "Banane" und "Bananen" zu stande kommt
            new_array = self.delete_duplications(new_array)
        return new_array

    def assamble_array(self, array):
        print(f"Beim Start von assamble_array: {array}")
        temp_array = []
        temp_array0 = array
        for item in temp_array0:
            item = item.replace('1', '')
            item = item.replace('2', '')
            item = item.replace('3', '')
            item = item.replace('4', '')
            item = item.replace('5', '')
            item = item.replace('6', '')
            item = item.replace('7', '')
            item = item.replace('8', '')
            item = item.replace('9', '')
            item = item.replace('0', '')
            item = item.strip()
            temp_array.append(item)
        duplications = self.delete_duplications(temp_array)
        temp3_array = []
        if len(duplications) >= 1:
            temp2_array = self.assamble_new_items(array, duplications)
            for item in temp2_array:
                try:
                    anz = int(item.split(' ', 1)[0])
                except:
                    anz = 1
                anz -= 1

                if anz == 1:
                    item = item.split(' ')[1]
                else:
                    item = str(anz) + " " + item.split(' ', 1)[1]
                temp3_array.append(item)

        return temp3_array
