from src.clock import Clock
from src.parse import parse

# c = Clock(notify=10.0)
# print(c.config.notify_me)

# c.run()

print(*parse("/%d/", "10/"))
