import pyodbc as odbc
import tkinter as tk
import openai

# Thông tin kết nối đến SQL Server
SERVER_NAME = 'PTHONG\SQLEXPRESS'
DATABASE_NAME = 'Chatbot'
DRIVER_NAME = 'SQL Server'

# Chuỗi kết nối
conn_str = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trusted_Connection=yes;
"""

# Đặt API key của OpenAI

# Kết nối đến cơ sở dữ liệu SQL Server
conn = odbc.connect(conn_str)

# try:
#     # Kết nối đến cơ sở dữ liệu
#     conn = odbc.connect(conn_str)

#     # Hiển thị danh sách các câu hỏi có parent_id = NULL
#     cursor = conn.cursor()
#     cursor.execute('SELECT Id, Question FROM Script WHERE parent_id IS NULL')
#     print("Danh sách câu hỏi có parent_id = NULL:")
#     for row in cursor.fetchall():
#         print(row)

#     while True:
#         # Nhập Id của câu hỏi từ người dùng
#         question_id = input("\nNhập Id của câu hỏi để hiển thị câu trả lời và danh sách câu hỏi mới (hoặc nhấn Enter để thoát): ")

#         # Kiểm tra nếu người dùng nhập rỗng (Enter) thì thoát vòng lặp
#         if not question_id:
#             break

#         # Thực thi truy vấn SELECT để lấy câu trả lời tương ứng
#         cursor.execute('SELECT Answer FROM Script WHERE Id = ?', (question_id,))
#         answer = cursor.fetchone()
#         if answer:
#             print("\nCâu trả lời:")
#             print(answer[0])

#             # Hiển thị danh sách câu hỏi mới có parent_id = question_id
#             cursor.execute('SELECT Id, Question FROM Script WHERE parent_id = ?', (question_id,))
#             new_questions = cursor.fetchall()
#             if new_questions:
#                 print("\nDanh sách câu hỏi mới:")
#                 for question in new_questions:
#                     print(question)
#             else:
#                 print("Không có câu hỏi mới cho Id này.")
#         else:
#             print("Không tìm thấy câu hỏi có Id tương ứng.")

# except odbc.Error as e:
#     print(f"Error: {e}")

# finally:
#     # Đóng kết nối
#     conn.close()

try:
    # Kết nối đến cơ sở dữ liệu
    conn = odbc.connect(conn_str)

    # Hiển thị danh sách các câu hỏi có parent_id = NULL
    cursor = conn.cursor()
    cursor.execute('SELECT Id, Question FROM Script WHERE parent_id IS NULL')
    print("Danh sách câu hỏi có parent_id = NULL:")
    for row in cursor.fetchall():
        print(row)

    while True:
        # Nhập Id của câu hỏi từ người dùng
        input_str = input("\nNhập Id của câu hỏi hoặc câu hỏi của bạn (hoặc nhấn Enter để thoát): ")

        # Kiểm tra nếu người dùng nhập rỗng (Enter) thì thoát vòng lặp
        if not input_str:
            break

        # Kiểm tra xem đầu vào có phải là số (Id) hay không
        if input_str.isdigit():
            # Nếu là số, thực hiện hiển thị câu trả lời và danh sách câu hỏi mới
            question_id = int(input_str)
            cursor.execute('SELECT Answer FROM Script WHERE Id = ?', (question_id,))
            answer = cursor.fetchone()
            if answer:
                print("\nCâu trả lời:")
                print(answer[0])

                # Hiển thị danh sách câu hỏi mới có parent_id = question_id
                cursor.execute('SELECT Id, Question FROM Script WHERE parent_id = ?', (question_id,))
                new_questions = cursor.fetchall()
                if new_questions:
                    print("\nDanh sách câu hỏi mới:")
                    for question in new_questions:
                        print(question)
                else:
                    print("Không có câu hỏi mới cho Id này.")
            else:
                print("Không tìm thấy câu hỏi có Id tương ứng.")
        else:
            # Nếu không phải là số, gửi yêu cầu tới GPT-3 để tạo câu trả lời
            response = openai.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=input_str,
                temperature=0.5,
                top_p=0.3,
                max_tokens=128
            )
            print("\nCâu trả lời của ChatGPT:")
            print(response.choices[0].text.strip())

except odbc.Error as e:
    print(f"Error: {e}")

finally:
    # Đóng kết nối
    conn.close()