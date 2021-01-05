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
        for i in range(len(text)):
            # Erst hier .lower und Groß- und Kleinschreibung beizubehalten
            if text[i].lower() == start_word:
                index = i + 1

        if index is not -1:
            if end_word == '':
                for i in range(index, len(text)):
                    ausgabe.append(text[i])
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
        return list(set(array))

    def assamble_array(self, array1, array2):
        new_array = []
        for item in array1:
            value1, number1 = self.get_value_number(self, item)
            try:
                item1 = item.split(" ", 1)[1].lower()
            except:
                item1 = item.lower()
            for field in array2:
                value2, number2 = self.get_value_number(self, field)
                try:
                    item2 = field.split(" ", 1)[1].lower()
                except:
                    item2 = field.lower()
                # print(f"value1: {item1}, {number1}, {value1};    value2: {item2}, {number2}, {value2}")
                if item1 == item2 or item1.rstrip(item1[-1]) == item2 or item1 == item2.rstrip(item2[-1]):
                    if item1[-1] == "e":
                        item1 += "n"
                    if value1 == value2:
                        final_value = value1
                        final_number = number1 + number2
                        if final_number >= 1000 and final_value == "g":
                            final_value = "kg"
                            final_number /= 1000
                    else:
                        final_value = ""
                        final_number = -1
                    if final_number != -1:
                        new_array.append(str(final_number) + final_value + " " + item1.capitalize())
                    else:
                        new_array.append(item1.capitalize())
                else:
                    if self.is_enthalten(self, item1, array2):
                        new_array.append(item1.capitalize())
                    if self.is_enthalten(self, item2, array1):
                        new_array.append(item2.capitalize())

        return self.delete_duplications(self, new_array)

    def is_enthalten(self, item, array):
        item = item.lower()
        valid = True
        for position in array:
            try:
                item_position = position.split(" ", 1)[1].lower()
            except:
                item_position = position.lower()
            if item_position == item or item_position.rstrip(item_position[-1]) == item or item_position == item.rstrip(item[-1]):
                valid = False
        return valid

    def get_value_number(self, item):
        first_value = item.split(' ', 1)[0]
        value = ""
        number = 1
        if "kg" in first_value:
            try:
                first_value.replace("kg", "")
                value = "g"
                number = int(first_value) * 1000
            except:
                pass
        elif "g" in first_value:
            try:
                first_value1 = first_value.replace("g", "")
                value = "g"
                number = int(first_value1)
            except:
                pass
        else:
            try:
                number = int(first_value)
            except:
                pass
        return value, number

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
