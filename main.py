import csv
calls_sum_dict = dict()
def Polaczenia(self):
    with open('phoneCalls.csv', 'r') as fin:
        # csv.DictReader uses first line in file for column headings by default
        reader = csv.reader(fin, delimiter=";")  # comma is default delimiter
        headers = next(reader)
        for row in reader:
            from_subscr = int(row[0])
            if from_subscr not in calls_sum_dict:
                calls_sum_dict[from_subscr] = 0
            # value = int(row[3])
            value = 1
            calls_sum_dict[from_subscr] += value

def pobierz_najczesciej_dzwoniacego(self):
    return max(self.calls_sum_dict.items(), key= lambda x: x[1])

if __name__ == '__main__':
print(Polaczenia(input()).pobierz_najczesciej_dzwoniacego())
