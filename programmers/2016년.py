def solution(a, b):
    import datetime
    dayList = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    answer = dayList[datetime.date(2016, a, b).weekday()]

    return answer
