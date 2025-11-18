def up(s): return s.upper()
def lo(s): return s.lower()
def ti(s): return s.title()

fmt={"UP":up,"LO":lo,"TI":ti}
t=input("Enter text: ")
c=input("Enter command (UP/LO/TI): ")
print("Formatted:",fmt[c](t))
