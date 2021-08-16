room = {'CS101':'3004','CS102':'4501','CS103':'6755','NT110':'1244','CM241':'1411'}
instructor={'CS101':'Haynes','CS102':'Alavarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
meeting = {'CS101':'8:00am','CS102':'9:00am','CS103':'10:00am','NT110':'11:00am','CM241':'1:00pm'}
print("Enter a course number ")
courseNo=input()
print("The Details for the course "+str(courseNo)+" are:")
print("Room "+str(room.get(courseNo)))
print("Instructor: "+str(instructor.get(courseNo)))
print("Time: "+str(meeting.get(courseNo)))