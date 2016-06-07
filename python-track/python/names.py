def format_names(names):
    for person in names:
        name_list = []
        for name in person:
            name_list.append(person[name])
        full_name = " ".join(name_list)
        print full_name

def format_people(people):
    for cat in people:
        print cat
        for index, person in enumerate(people[cat]):
            name_list = []
            length = 0
            for name in person:
                name_list.append(person[name])
                length += len(person[name])
            full_name = " ".join(name_list).upper()
            print index+1, "-", full_name, "-", length


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

format_names(students)
format_people(users)
