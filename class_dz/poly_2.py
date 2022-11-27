class Answer:
    def __init__(self, name, completed, max_score):
        self.name = name
        self.completed = completed
        self.max_score = max_score


class Gradate(Answer):
    def __init__(self, name, completed, max_score):
        super().__init__(name, completed, max_score)


class IamSpeed(Answer):
    def __init__(self, name, completed, max_score, time_to_solve, case_score, percent, time):
        super().__init__(name, completed, max_score)
        self.time_to_solve = time_to_solve
        self.case_score = case_score
        self.percent = percent
        self.time = time


class Participant:
    def __init__(self, name, task, total):
        self.name = name
        self.task = task
        self.total = total

    def que_score(self):
        for i in self.task:
            if i.completed and isinstance(i, Gradate):
                self.total += i.max_score
            if i.completed and isinstance(i, IamSpeed):
                self.total +=  case_score





def check_time_of_all(participants):
    all_time = []
    for i in participants:
        for j in i.task:
            if isinstance(j, IamSpeed) and j.completed:
                all_time.append(j.case_score)
    return min(all_time)


def set_score_FasterIsBetter(participants):
    min_ = check_time_of_all(participants)
    for p in participants:
        for t in p.task:
            if isinstance(t, IamSpeed):
                if t.completed and t.time <= t.time_to_solve:
                    if t.time == min_:
                        t.case_score = t.max_score
                    else:
                        t.case_score = t.max_score - (t.max_score * t.percent / 100) * (t.time - min_)
                else:
                    t.case_score = 0
