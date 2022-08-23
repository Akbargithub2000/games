import random

count = 0
chance = 10
comp_count = 0
user_count = 0
lst = ['s', 'w', 'g']

while count<chance:
    inp = input('Choose from Snake/Water/Glass(s/w/g)').lower()
    rand = random.choice(lst)

    if inp==rand: print('A tie')

    elif inp=='s':
        if rand == 'g':
            comp_count += 1
            print(f'Computer won with choice {rand}')
        else:
            user_count += 1
            print(f'You won with choice {inp}')

    elif inp == 'w':
        if rand == 's':
            comp_count += 1
            print(f'Computer won with {rand}')
        else:
            user_count += 1
            print(f'You won with choice {inp}')

    elif inp == 'g':
        if rand == 'w':
            comp_count += 1
            print(f'Computer won with choice {rand}')
        else:
            user_count += 1
            print(f'You won with choice {inp}')

    else:
        print('You entered wrong input')

    count += 1
    print(f'You have {chance-count} left out of {chance}')

print('Your score {user_count} Computer score {comp_count}')
print('Good Bye')