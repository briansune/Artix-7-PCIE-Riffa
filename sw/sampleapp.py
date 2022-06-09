import array
import riffa
import timeit

amt = 100
sent = 0
recv = 0

lst = []
for i in range(amt):
    lst.append(i*2)

dataSend = array.array('I', lst)
dataRecv = array.array('I', [0] * amt)

print(riffa.fpga_list())
fd = riffa.fpga_open(0)
print(fd)

start_time = timeit.default_timer()
sent = riffa.fpga_send(fd, 0, dataSend, amt, 0, True, 0)
print("Elapsed time (us):", (timeit.default_timer() - start_time) * 1e6)

start_time = timeit.default_timer()
recv = riffa.fpga_recv(fd, 0, dataRecv, 0)
print("Elapsed time (us):", (timeit.default_timer() - start_time) * 1e6)

riffa.fpga_close(fd)
print(dataSend)
print(dataRecv)
