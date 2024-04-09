# Convert Booleans to Integers in Python

# ✅ convert True and False to 1 and 0

bool_t = True
int_1 = int(bool_t)
print(int_1)  # 👉️ 1

bool_f = False
int_0 = int(bool_f)
print(int_0)  # 👉️ 0

# -----------------------------------------------

# ✅ convert 'true' and 'false' to 1 and 0

str_t = 'true'
int_1 = int(str_t.lower() == 'true')
print(int_1)  # 👉️ 1

str_f = 'false'
int_0 = int(str_f.lower() == 'true')
print(int_0)  # 👉️ 0