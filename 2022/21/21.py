ll = open('./2022/21/test.txt').read().splitlines()
ll = open('./2022/21/input.txt').read().splitlines()

m = {}

class Monkey:
    def __init__(self, name, job) -> None:
        self.name = name
        self.job = job

    def yell(self):
        #print('yelling', self.name, self.job)
        j = self.job

        if self.name == 'root':
            a, b = j.split(' + ')

            if self.name == 'root':
                print('yelling', self.name, self.job, m[a].yell(), m[b].yell())
                print(a, 88521161883075)
            return m[a].yell()==m[b].yell()

        elif j.isnumeric():
            return int(j)
        elif '+' in j:
            a, b = j.split(' + ')
            return m[a].yell() + m[b].yell()
        elif '-' in j:
            a, b = j.split(' - ')
            return m[a].yell() - m[b].yell()
        elif '*' in j:
            a, b = j.split(' * ')
            return m[a].yell() * m[b].yell()
        elif '/' in j:
            a, b = j.split(' / ')
            return m[a].yell() // m[b].yell()

        return 0


for l in ll:
    n,j = l.split(': ')
    #print(n,j)
    m[n] = Monkey(n,j)

m['humn'].job = '100000000000000000'
print(m['root'].yell())