from utils import part1, part2

if __name__ == '__main__':
    with open('data.txt','r') as data:
        data = [i.strip('\n').split() for i in data.readlines()]
    
    print(part1(data))
    print(part2(data))