import threading
import time
import random
import tkinter as tk
import csv
import matplotlib.pyplot as plt

NUM_PHILOSOPHERS = 5
TIME_TO_RUN = 200

forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]
eat_count = [0] * NUM_PHILOSOPHERS
fork_status = ["0"] * NUM_PHILOSOPHERS  # 0 means no fork, 1 means own fork, 2 means borrowed fork
status = ["."] * NUM_PHILOSOPHERS

# CSV file setup
csv_file_path = "philosophers_data.csv"
csv_columns = ["PhilosopherID", "SecondWhenAte"]

root = tk.Tk()
root.title("Dining Philosophers")

philosopher_labels = []
for i in range(NUM_PHILOSOPHERS):
    philosopher_labels.append(tk.Label(root, text=f"Philosopher {i}:"))
    philosopher_labels[i].grid(row=i, column=0, padx=10, pady=10)

eating_time_labels = []
for i in range(NUM_PHILOSOPHERS):
    eating_time_labels.append(tk.Label(root, text="0"))
    eating_time_labels[i].grid(row=i, column=1, padx=10, pady=10)

fork_status_labels = []
for i in range(NUM_PHILOSOPHERS):
    fork_status_labels.append(tk.Label(root, text="0   1"))
    fork_status_labels[i].grid(row=i, column=2, padx=10, pady=10)

status_labels = []
for i in range(NUM_PHILOSOPHERS):
    status_labels.append(tk.Label(root, text="mysli"))
    status_labels[i].grid(row=i, column=3, padx=10, pady=10)

time_label = tk.Label(root, text=f"Time Remaining: {TIME_TO_RUN} s")
time_label.grid(row=NUM_PHILOSOPHERS, column=0, columnspan=3, padx=10, pady=10)

def update_gui(philosopher_id):
    philosopher_labels[philosopher_id].config(text=f"Philosopher {philosopher_id}:")
    eating_time_labels[philosopher_id].config(text=str(eat_count[philosopher_id]))
    fork_status_labels[philosopher_id].config(text=fork_status[philosopher_id])
    status_labels[philosopher_id].config(text=status[philosopher_id])
    root.update()

def update_csv(philosopher_id, start_time):
    with open(csv_file_path, mode='a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writerow({"PhilosopherID": philosopher_id, "SecondWhenAte": int(time.time() - start_time)})

def generate_line_chart(csv_file_path):
    philosopher_data = {}

    # Wczytaj dane z pliku CSV
    with open(csv_file_path, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            philosopher_id = int(row['PhilosopherID'])
            second_when_ate = int(row['SecondWhenAte'])

            if philosopher_id not in philosopher_data:
                philosopher_data[philosopher_id] = {'time': [], 'meals': []}

            philosopher_data[philosopher_id]['time'].append(second_when_ate)
            philosopher_data[philosopher_id]['meals'].append(len(philosopher_data[philosopher_id]['time']))

    # Generuj wykres liniowy
    plt.figure(figsize=(10, 6))

    for philosopher_id, data in philosopher_data.items():
        plt.plot(data['time'], data['meals'], label=f'Philosopher {philosopher_id}')

    plt.xlabel('Time (seconds)')
    plt.ylabel('Total Meals')
    plt.title('Dining Philosophers - Total Meals Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

def philosopher(philosopher_id):
    global eat_count, fork_status, status

    start_time = time.time()
    while time.time() - start_time < TIME_TO_RUN:
        status[philosopher_id] = "mysli"
        update_gui(philosopher_id)
        time.sleep(random.uniform(10, 15))
        status[philosopher_id] = "czeka"
        update_gui(philosopher_id)
        left_fork = forks[philosopher_id]
        right_fork = forks[(philosopher_id + 1) % NUM_PHILOSOPHERS]

        left_fork.acquire()
        fork_status[philosopher_id] = "1"
        if right_fork.acquire(blocking=False):
            fork_status[philosopher_id] = "1   1"
            status[philosopher_id] = "je"
            eat_count[philosopher_id] += 1
            update_gui(philosopher_id)
            right_fork.release()

            time.sleep(random.uniform(1, 10))
            left_fork.release()
            fork_status[philosopher_id] = "0   1"
            status[philosopher_id] = "zjadł"
            update_gui(philosopher_id)
        else:
            left_fork.release()
            fork_status[philosopher_id] = "0   0"
            update_gui(philosopher_id)
        update_csv(philosopher_id, start_time)
        update_gui(philosopher_id)
    update_gui(philosopher_id)

def update_time():
    global TIME_TO_RUN
    current_time = int(time.time() - start_time)
    remaining_time = TIME_TO_RUN - current_time
    if remaining_time < 0:
        remaining_time = 0
    time_label.config(text=f"Time Remaining: {remaining_time} s")
    if remaining_time > 0:
        root.after(1000, update_time)
    else:
        generate_line_chart('philosophers_data.csv')
        root.after(10000000, root.quit)

# Clear CSV file if it exists
with open(csv_file_path, mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()

philosopher_threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(NUM_PHILOSOPHERS)]

for thread in philosopher_threads:
    thread.daemon = True
    thread.start()

start_time = time.time()
update_time()

root.mainloop()
