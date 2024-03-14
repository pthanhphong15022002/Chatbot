import pandas as pd
import tkinter as tk

def display_answers():
    question_1 = question_var_1.get()
    if question_1:
        answer_1 = df[df['Câu hỏi 1'] == question_1]['Câu trả lời 1'].iloc[0]
        answer_label_1.config(text=answer_1)
        question_2_options = df[df['Câu hỏi 1'] == question_1]['Câu hỏi 2'].tolist()
        question_var_2.set(question_2_options[0]) if question_2_options else question_var_2.set('')

def on_select(event):
    question_2 = question_var_2.get()
    if question_2:
        answer_2 = df[(df['Câu hỏi 1'] == question_var_1.get()) & (df['Câu hỏi 2'] == question_2)]['Câu trả lời 2'].iloc[0]
        answer_label_2.config(text=answer_2)

# Đọc dữ liệu từ tệp Excel
df = pd.read_excel("Book2.xlsx")

# Tạo giao diện người dùng
root = tk.Tk()
root.title("Hiển thị câu trả lời")

# Câu hỏi 1
question_label_1 = tk.Label(root, text="Chọn câu hỏi 1:")
question_label_1.pack()

questions_1 = df['Câu hỏi 1'].unique().tolist()
question_var_1 = tk.StringVar(root)
question_var_1.set(questions_1[0])
question_dropdown_1 = tk.OptionMenu(root, question_var_1, *questions_1, command=display_answers)
question_dropdown_1.pack()

# Câu trả lời 1
answer_label_1 = tk.Label(root, text="", wraplength=300)
answer_label_1.pack()

# Câu hỏi 2
question_label_2 = tk.Label(root, text="Chọn câu hỏi 2:")
question_label_2.pack()

question_var_2 = tk.StringVar(root)
question_dropdown_2 = tk.OptionMenu(root, question_var_2, '', command=on_select)
question_dropdown_2.pack()

# Câu trả lời 2
answer_label_2 = tk.Label(root, text="", wraplength=300)
answer_label_2.pack()

root.mainloop()
