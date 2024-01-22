# 1. Class Exercise:
# Create a Python class representing a Hospital account with methods to schedule visit
# and remove schedule.
import datetime
class HospitalAccount:
    def __init__(self,patient):
        self.patient=patient
        self.schedule = []
    def schedule_visit(self,date,doctor):
        details_visit={"date": date, "doctor": doctor}
        self.schedule.append(details_visit)
        return f"Visit scheduled {date},with doctor Dr.{doctor} , of patient {self.patient}"
    def remove_schedule(self,date):
        for i in self.schedule:
            if i["date"] == date:
                self.schedule.remove(i)
                print(f"Visit scheduled in {date} removed")
k=HospitalAccount("Ruslan")
print(k.schedule_visit(datetime.datetime(2023,10,10,17,23,15),"Arman"))
k.remove_schedule(datetime.datetime(2023,10,10,17,23,15))

