# import numpy as np

class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def print_job_sequence(jobs):
    # Sort jobs in descending order of profit
    jobs.sort(key=lambda job: job.profit, reverse=True)

    n = len(jobs)
    # Find the maximum deadline
    max_deadline = max(job.deadline for job in jobs)

    # Initialize result list and slot list
    result = ['X'] * max_deadline
    slot = [False] * max_deadline

    # Iterate through all jobs
    for i in range(n):
        # Find a free slot for this job (we start from the last possible slot)
        for j in range(min(max_deadline - 1, jobs[i].deadline - 1), -1, -1):
            if not slot[j]:
                result[j] = jobs[i].id
                slot[j] = True
                break

    # Print the result
    print("Job Sequence: ", end="")
    for job_id in result:
        if job_id != 'X':
            print(job_id, end=" ")
    print()

    # Calculate and print the total profit
    total_profit = 0
    for i in range(max_deadline):
        if slot[i]:
            for job in jobs:
                if job.id == result[i]:
                    total_profit += job.profit
                    break
    print("Total Profit:", total_profit)

if __name__ == "__main__":
    jobs = [
        Job('a', 2, 100),
        Job('b', 1, 19),
        Job('c', 2, 27),
        Job('d', 1, 25),
        Job('e', 3, 15)
    ]

    print("Job Sequencing with Deadlines:")
    print_job_sequence(jobs)
