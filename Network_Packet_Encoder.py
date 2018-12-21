import sys
import random
from copy import deepcopy

def getCount(recvd, send, queue, n_count, encoded=True):
    
    count = 0
    while len(queue):
        
        current = [queue.pop(0)]
        neighbours = set()
        
        # Identify neighbours who need the current packet as their next packet
        for each in range(n_count):
            if len(send[each]) and send[each][0] == current[0]:
                neighbours.add(each)
                send[each].pop(0)
        if not len(neighbours):
            continue
        count += 1
        
        # Send without encoding
        if not encoded:
            print("Sending unencoded packets " + str(current) + " to neighbours " + str(neighbours))
            for packet in current:
                for each in neighbours:
                    recvd[each].add(packet)
            continue
        
        # Identify packets from the remaining neighbours' next required packets,
        # which can be encoded with the current packet
        for each in range(n_count):
            if each in neighbours or not len(send[each]):
                continue
            p_i = send[each][0]
            
            possible = True
            for element in current:
                if element not in recvd[each]:
                    # This neigbour does not have the packet identified in the previous step, so it
                    # cannot decode this. Move on to the next option
                    possible = False
                    break
            if not possible:
                continue
            
            for one_neighbour in neighbours:
                if p_i not in recvd[one_neighbour]:
                    # The potential packet which can be encoded is not held by the other designated recipients
                    # of the first packet. Hence, encoding is not possible.
                    possible = False
                    break
            if not possible:
                continue
            
            current.append(p_i)
            neighbours.add(each)
            send[each].pop(0)
        
        # Transmit the encoded packet
        print("Sending encoded packets " + str(current) + " to neighbours " + str(neighbours))
        for packet in current:
            for each in neighbours:
                recvd[each].add(packet)
            
    return count

def random_input(n_count, p_count):
    print("Generating random inputs..... ")
    send = []
    recvd = []
    queue = []

    for _ in range(n_count):
        send.append([])
        recvd.append(set())
        
    for packet in range(p_count):
        for n in range(n_count):
            if random.sample(range(1, 1001), 1)[0] % 2:
                send[n].append(packet)
            else:
                recvd[n].add(packet)
        queue.append(packet)
        

    for each in send:
        random.shuffle(each)
    
    print("Inputs generated")
    return recvd, send, queue

def test_run(n_count, p_count):
    recvd, send, queue = random_input(n_count, p_count)
    encoded = getCount(deepcopy(recvd), deepcopy(send), deepcopy(queue), n_count, True)
    unencoded = getCount(deepcopy(recvd), deepcopy(send), deepcopy(queue), n_count, False)
    print("\n***** Transmission simulation done ******\n")
    print("Total number of transmissions needed without encoding = " + str(unencoded))
    print("Total number of transmissions needed with encoding = " + str(encoded))
    print("percentage gain = " + str(((unencoded-encoded)*100/unencoded)) + "%")
    if p_count < n_count:
        print("Please note that this algorithm is designed for situations where the packet count is a little greater than the neighbour count")
        print("Packet count = " + str(p_count))
        print("Neighbour count = " + str(n_count))


if sys.version_info[0] < 3:
    print("Please use python3")
    exit()

args = sys.argv
if len(args) != 3:
    print(len(args), "Please enter 2 arguments. The first is the neighbour count, the second is the packet count")
    exit()

try:
    n_count = int(sys.argv[1])
    p_count = int(sys.argv[2])
except:
    print("Please enter valid numbers")
    exit()
    
test_run(n_count, p_count)

