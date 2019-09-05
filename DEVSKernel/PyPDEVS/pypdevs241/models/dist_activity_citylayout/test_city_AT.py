import sys
sys.path.append("../../src/")
sys.path.append("dist_activity_citylayout/activity_tracking/")
from trafficModels import *
from generated_city import City
from simulator import Simulator
import time
if __name__ == '__main__':
    city = City()
    from mpi4py import MPI
    if MPI.COMM_WORLD.Get_size() == 1:
        city.setLocation(0, force=True)
    sim = Simulator(city)
    #sim.setVerbose(None)
    sim.setStateSaving('custom')
    #sim.setMemoization()
    sim.setMessageCopy('custom')
    sim.setTerminationTime(5000.0)
    sim.setSchedulerHeapSet()
    sim.setGVTInterval(2)
    sim.setActivityRelocatorCustom('relocator', 'CityRelocator')
    start = time.time()
    sim.simulate()
    print(('Arrived: ' + str(len(city.collector.state.cars)/468.0)))
    print(("Simulation time: " + str(time.time() - start)))

