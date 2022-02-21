import json

def combine_constitution():
    constitution_file = open("data/constitution.json")
    constitution_json = json.load(constitution_file)
    constitution_file.close()
    
    for part in range(1, 23):
        part_file = open("part"+str(part)+".json")
        part_json = json.load(part_file)

        constitution_json["parts"][str(part)] = part_json
        part_file.close()

    for schedule in range(1, 9):
        schedule_file = open(str(schedule)+"schedule.json")
        schedule_json = json.load(schedule_file)

        constitution_json["schedules"][str(schedule)] = schedule_json
        schedule_file.close()
    
    constitution_file = open("data/constitution.json", 'w')
    json.dump(constitution_json, constitution_file)
    constitution_file.close()

if __name__ == "__main__":
    combine_constitution()