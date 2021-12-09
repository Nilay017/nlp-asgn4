import json
from human_eval.data import write_jsonl, read_problems

problems = read_problems()
# print(problems)
with open("human_eval_problems.json", 'w') as file:
    list_probs = []
    for task_id in problems:
        list_probs.append(problems[task_id])
    file.write(json.dumps(list_probs))

with open("../data/conala/conala-corpus/conala-test.json", 'w') as file:
    list_probs = []
    id = 0
    for task_id in problems:
        prob = {}
        prob["intent"] = problems[task_id]["prompt"]
        prob["snippet"] = "dummy"
        prob["question_id"] = id
        id += 1
        list_probs.append(prob)
    file.write(json.dumps(list_probs))

num_samples_per_task = 200

# samples = [
#     dict(task_id=task_id, completion=generate_one_completion(problems[task_id]["prompt"]))
#     for task_id in problems
#     for _ in range(num_samples_per_task)
# ]
# write_jsonl("samples.jsonl", samples)