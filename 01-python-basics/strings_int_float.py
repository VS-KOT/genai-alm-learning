# =========================
# Strings
# =========================

my_message = "Hello World"
print(len(my_message), my_message)


# =========================
# Slicing
# =========================

print(my_message[:4], my_message[7:])


# =========================
# Lower & Upper Case
# =========================

print(my_message.lower(), my_message.upper())
print(my_message)


# =========================
# Count words / letters
# (Case-sensitive)
# =========================

print(my_message.count("Hello"))


# =========================
# Find
# Returns index of starting position
# =========================

print(my_message.find("World"))


# =========================
# Replace (Strings are immutable)
# =========================

new_message = my_message.replace("Hel", "hheell")
print(new_message)


# =========================
# Notes
# =========================
# Concat, slicing, and f-strings are related concepts
# but used in different scenarios.


# =========================
# Integers
# =========================

# Operators are same as C++ except:
# //  -> floor division
# /   -> float division

# Typecasting
print(int("100") + int("200"))


# =========================
# ASCII Value
# =========================

print(ord("a"))
