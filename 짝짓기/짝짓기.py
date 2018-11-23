import random

class Persons(dict):
    def __init__(self, name):
        self.name = name
        self.suki = list()
    
    def shuffle(self):
        random.shuffle(self.suki)
    
    def add_suki(self, *name):
        for _name in name:
            self.suki.append(_name)
    
    def to_line(self):
        return "".join([name] + self.suki)
    
    def __str__(self):
        return "{} : {}".format(self.name, str(self.suki))
    
class People(dict):
    def __init__(self, *persons):
        self.persons = persons
        self.names = [hito.name for hito in self.persons]
        super().__init__((persons.name, persons.suki) for persons in self.persons)

    def put(self, people):
        othername = set(people.names)
        for persons in self.persons:
            persons_name = set(persons.suki)
            for name in list(othername - persons_name):
                persons.add_suki(name)
    
    def shuffle(self):
        for persons in self.persons:
            persons.shuffle()
 
    
    def __str__(self):
        str_l = list()
        for persons in self.persons:
            str_l.append(persons.name + " ".join(persons.suki))
            return " ".join(str_l)


class Match:
    def __init__( self, boys, girls):
        self.boys = boys
        self.girls = girls

        self.couple= dict()

        self.boylikes = dict()
        self.girlike = dict()

        for name, likes in self.boys.items():
            self.boylikes[name] = dict((name, score) for score, name in enumerate(likes))
        for name, likes in self.girls.items():
            self.girlike[name] = dict((name, score) for score, name in enumerate(likes))
    
    def __call__(self):
        return self.match()

    def is_better(self, girl, boyfriend, newboy):
        return self.girlike[girl][boyfriend] > self.girlike[girl][newboy]

    def match(self):
        singleBoy = list(self.boys.keys())
        trycount = dict( (name, 0) for name in self.boys.keys())
        couple = {}

        while singleBoy:
            boy = singleBoy.pop(0)
            girl = self.boys[boy][trycount[boy]]
            trycount[boy] += 1
            if girl in couple:
                boyfriend = couple[girl]
                if self.is_better(girl, boyfriend, boy):
                    singleBoy.append(boyfriend)
                    couple[girl] = boy
                else:
                    singleBoy.append(boy)
            else:
                couple[girl] = boy
        
        return [(boy, girl) for girl, boy in couple.items()]


def main():
    with open("남자이름.txt", encoding="utf-8") as fboynames, open("여자이름.txt", encoding="utf-8") as fgirlname:
        boynames = [Persons(name.replace("\n","")) for name in fboynames]
        girlname = [Persons(name.replace("\n","")) for name in fgirlname]

        boys = People(*boynames)
        girls = People(*girlname)

        boys.put(girls)
        girls.put(boys)

        boys.shuffle()
        girls.shuffle()
        
        print("\n남자이름 : 여자순위")
        for boy in boynames:
            print(boy)
        
        print("\n여자이름 : 남자순위")
        for girl in girlname:
            print(girl)
        
        print(boys)

        print("\n결과")
        matcher = Match(boys, girls)
        for couple in matcher.match():
            print("{} {}".format(*couple))
    


if __name__ == "__main__":
    main()
    print("1801127김민수")
