import os

def list_files(start_path, indent=0, output=[]):
    try:
        for item in os.listdir(start_path):
            path = os.path.join(start_path, item)
            output.append('    ' * indent + '|-- ' + item)
            if os.path.isdir(path):
                list_files(path, indent + 1, output)
    except PermissionError:
        output.append('    ' * indent + '|-- [Permission Denied]')

# المستخدم يكتب المسار أو يسيبه فاضي عشان ياخد المسار الحالي
user_path = input("اكتب مسار المجلد (أو اضغط Enter للمسار الحالي): ").strip()
if not user_path:
    user_path = os.getcwd()

output_lines = [f"📁 Structure of: {user_path}", ""]

list_files(user_path, output=output_lines)

# أطبع النتيجة في التيرمنال
print("\n".join(output_lines))

# واحفظها في ملف
with open("tree.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print("\n✅ تم حفظ هيكل المشروع في ملف tree.txt")
