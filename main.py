# Creates an object of scheduler type and kickstarts the project
from inputParser import InputParser
from src.azure.scheduler import Scheduler


def main():
    obj = Scheduler()
    obj.create()


if __name__ == '__main__':
    main()
