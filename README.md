# Network_Packet_Encoder
An application that stimulates a network with 1 source and 'n' sinks and generates best set of packet combinations to achieve minimum number of transmissions. This application demonstrates advantage of encoded transmission over un-encoded transmission.

The algorithm as implemented can be viewed in the Network_Packet_Encoder.py. The program has one driver function and two helper functions as follows:

    random input(n count, p count)
This function takes the neighboring node count as n count and packet count as p count. It then models a dummy network with n + 1 nodes (+1 is for source node) by randomly generating packet numbers for each node n 2 [1; n count] and assigning it to send list or received list for the node. The send list represents the packets the node is expecting to receive next and the received list indicated the packets the node has already received. The method returns the simulated network model in form of three lists:

send  || Size: n count by S (1 row corresponding to each node)

recvd || Size: n count by R (1 row corresponding to each node)

queue || Size: p count by 1 (Note: S + R = p count)

    getCount(recvd, send, queue, n count, encoded)
This function takes as input the network model and outputs the target nodes along with the encoded packet numbers. The argument encoded indicates the mode of operation for the function.

If encoded = True the algorithm operates in multi-cast mode and tries to encode the packets to minimize the number of transmissions.

If encoded = False the algorithm operates in uni-cast mode and sends packets to each neighbor one at a time.

For both modes the function maintains a count of the number of transmissions and returns the count.

    test run(n count, p count)
This is the driver function which takes in the inputs for n count and p count and generates the
desired network simulation and transmission comparison.

Run the program using the command - 
    
    "python3 Network_Packet_Encoder.py 10 20".
>10 and 20 are sample inputs.
>10 is the number of neighbours(n count).
>20 is the number of packets in the system(p count).
