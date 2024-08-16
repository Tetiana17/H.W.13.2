class Counter:

   def __init__(self, current=1, min_value=0, max_value=10):
       self.current = current
       self.min_value = min_value
       self.max_value = max_value

   def set_current(self, start):
       #початкове значення лічильника
       if start < self.min_value or start > self.max_value:
           raise ValueError
       self.current = start

   def set_max(self, max_max):
       #нове максимальне значення
        self.max_value = max_max
        if self.current > max_max:
            self.current = max_max

   def set_min(self, min_min):
       #нове мінімальне значення
       self.min_value = min_min
       if self.current < min_min:
           self.current = min_min

   def step_up(self):
       #збільшує значення лічильника на 1
       if self.current >= self.max_value:
           raise ValueError
       self.current += 1

   def step_down(self):
       #зменшує значення лічильника на 1
       if self.current <= self.min_value:
           raise ValueError
       self.current -= 1

   def get_current(self):
       #повертає поточне значення лічильника
       return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'
