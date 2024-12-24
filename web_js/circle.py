import tkinter as tk
import time

def start_animation():
    global running, radius  # Հռչակում ենք գլոբալ փոփոխականները
    running = True
    radius = 50  # Սկզբնական շառավիղ
    max_radius = 100
    min_radius = 30
    delta = 2  # Շառավիղի փոփոխման չափ

    def animate():
        global radius  # Նշում ենք, որ օգտագործում ենք գլոբալ radius
        nonlocal delta  # Նշում ենք, որ օգտագործում ենք ոչ լոկալ delta
        if running:
            canvas.delete("circle")
            # Նկարում է շրջանագիծը
            canvas.create_oval(150 - radius, 150 - radius, 150 + radius, 150 + radius, fill="blue", tags="circle")
            radius += delta

            # Շառավիղի սահմանների ստուգում
            if radius >= max_radius or radius <= min_radius:
                delta *= -1  # Փոխում է ուղղությունը

            root.update()
            time.sleep(0.03)  #Անիմացիայի արագությունը
            animate()

    animate()

def stop_animation():
    global running
    running = False

# Պատուհանի ստեղծում
root = tk.Tk()
root.title("Circle Animation")
root.geometry("300x300")

running = False
radius = 50

# Կտավի ստեղծում
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# Կոճակների ստեղծում
start_button = tk.Button(root, text="Start", command=start_animation)
start_button.pack(side=tk.LEFT, padx=20, pady=10)

exit_button = tk.Button(root, text="Exit", command=lambda: (stop_animation(), root.destroy()))
exit_button.pack(side=tk.RIGHT, padx=20, pady=10)

root.mainloop()
