import os

def find_subthreshold_salaries(relative_path, threshold):
    """Find the workers with subthreshold salary."""
    script_path = os.path.dirname(__file__)
    abs_path = os.path.join(script_path, relative_path)
    try:
        with open(abs_path, encoding='utf-8') as f:
            workers_data = [line.strip().split(": ") for line in f]
            
            needed_workers_families = [worker[0] for worker in workers_data if float(worker[1]) < threshold]
            print(f"This workers has subthreshold salary: {needed_workers_families}")
            
            workers_salaries = [float(worker[1]) for worker in workers_data]
            print(f"The average salary: {sum(workers_salaries)/len(workers_salaries):.2f}")
    except IOError:
        print("Check the relative path")
    

# main
threshold = 20000.0
path = r"task-3\task-3.txt"
find_subthreshold_salaries(path, threshold)
