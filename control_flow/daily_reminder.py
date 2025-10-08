## Personal Daily reminder.

# User prompt for task, its priority and time sensitivity.

task = input("Enter your task: ")
priority = input("What is the priority of the task? (high, medium, low): ")
time_bound = input("Is the task time bound? (yes or no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a HIGH priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a HIGH priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a MEDIUM priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a MEDIUM priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a LOW priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a LOW priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered. Please choose high, medium, or low.")
