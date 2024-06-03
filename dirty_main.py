from datetime import *
from pyjokes import *
from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(date.today())
    print(get_joke())
