
import re
s = "A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."
s1 = re.sub(r"\bdog\b", "cat", s, flags=re.IGNORECASE)
print(f"New sentence: {s1}")