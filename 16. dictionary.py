# Dictionary = A changable, unordered collention of unique key:value pairs first
#               Because they use hashing, allow us to access a value quickly

capital = {'bangladesh':'dhaka',
            'india':'delhi',
            'china':'beijing',
            'russia':'moscow'}

capital.update({'rajshai':'santahar',
                'dhaka':'dhamrai'})

capital.pop('russia')

#print(capital['bangladesh'])
#print(capital.get('india'))
#print(capital.items())

for key,value in capital.items():   #key = Country name and value = capital
    print(key,value)
