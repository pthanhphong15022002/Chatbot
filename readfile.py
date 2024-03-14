import pandas as pd
import tkinter as tk

def display_answer(question):
    answer = df.loc[df['Câu hỏi'] == question]['Câu trả lời'].values
    if len(answer) > 0:
        answer_label.config(text=answer[0])
    else:
        answer_label.config(text="Không tìm thấy câu trả lời cho câu hỏi này")

def on_select(event):
    selected_item = event.widget.get()
    display_answer(selected_item)

# Đọc dữ liệu từ tệp Excel
df = pd.read_excel("Data.xlsx")

# Tạo giao diện người dùng
root = tk.Tk()
root.title("Hiển thị câu trả lời")

question_label = tk.Label(root, text="Chọn câu hỏi:")
question_label.pack()

questions = df['Câu hỏi'].tolist()
question_var = tk.StringVar(root)
question_var.set(questions[0])
question_dropdown = tk.OptionMenu(root, question_var, *questions, command=display_answer)
question_dropdown.pack()

answer_label = tk.Label(root, text="", wraplength=300)
answer_label.pack()

root.mainloop()
