class Engine:
    def __init__(self,cc):
        self.capacity=cc

    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Car:
    def __init__(self,name,cc):
        # super().__init__(cc)
        self.engine=Engine(cc)
        self.name=name 
        # print("sel",self)
        # print("sel.cc",self.cc)

    def run(self):
        self.engine.start()
        print("Car is running")

c1=Car("BMW",2000)
c1.run()