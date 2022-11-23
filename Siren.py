# POC | SIREN.PY | Untapped Potential of Sound | 
# Generating Sound using network traffic.
#┌────────────┐
#│Scapy.sniff │
#└──────┬─────┘           Protocol Extractor (Func)
#       │
#       │PacketSumm  ┌──────────────┬──┬─────────────────┐
#       │            │┼─────────────┤  ├────────────────┼│    packetProtocols (Class)
#       └────────────►│ProtocolSplit├──┤ProtocolHandler │┼─────────────────────────┐
#                    │┼─────────────┤  ├────────────────┼│                         │
#                    └──────────────┴──┴─────────────────┘                         │
#                                                                                  │
#                            Packet Synthesizer                                    │
#                     ┌───────────────────────────────────┐                        │
#                     │                                   │                        │
#                     │                                   │                        │
#                     │                                   │                        │
#                     │                                   │◄───────────────────────┘
#                     │                                   │
#                     │                                   │
#                     │                                   │
#                     │                                   │
#                     │                                   │
#                     │                                   │
#                     │                                   │
#                     └───────────────────────────────────┘



import scapy.all as scapy
from playsound import playsound
import time
#from playsound import playsound
#from pippi import dsp
# Contains the different protocols a packet has.
class classPacketProtocol:
        def __init__(self) -> None: # Initlized during packet reading
            self.L1
            self.L2
            self.L3
            self.L4
            self.L5
            self.L6
            self.L7


# My current aim is to create some sort of sound where the pitches are differentiable by the protocols they originate from.
# Potentially can use pippi (https://github.com/luvsound/pippi/) to alter pitches and tempo depending on different factors, is out of scope for this proof of concept tho
# 
#   Splits up betwee 
#
# Inital Logic for future additions.
#

def PacketSynthesizer(packetProtocols):
    #https://docs.oracle.com/cd/E19455-01/806-0916/ipov-10/index.html
        # Called Once transport layer is reached (Done for readability, not the most efficiency)
    def transportLayer(packetProtocols, networkinterface):
        if "TCP" in packetProtocols.L3:
            if "HTTP" in packetProtocols.L3:
                playsound('Sounds/Piano11.mp3', False)
            elif "DHCP" in packetProtocols.L3:
                playsound('Sounds/Piano15.mp3', False)
            elif "BGP" in packetProtocols.L3:
                playsound('Sounds/Piano18.mp3', False)
            elif  "HTTPS" in packetProtocols.L3:
                playsound('Sounds/Piano122.mp3', False)
            elif  "TLS" in packetProtocols.L3:
                playsound('Sounds/Piano17.mp3', False)
            else:
                playsound('Sounds/Piano13.mp3', False)
        elif "UDP" in packetProtocols.L3:
            if "DNS" in packetProtocols.L3:
                playsound('Sounds/Piano11.mp3', False)
            elif "SSDP" in packetProtocols.L3:
                playsound('Sounds/Piano19.mp3', False)
            if "SSDP" in packetProtocols.L3:
                playsound('Sounds/Piano114.mp3', False)
            else:
                playsound('Sounds/Piano125.mp3', False)
        else: 
            print("not fully implemented (POC)")

    if packetProtocols.L1 == "Ether ":
        match packetProtocols.L2:
            case " IP ":
                transportLayer(packetProtocols, "IP")
            case "ARP":
                playsound('Sounds/Piano125.mp3', False)
            case "ICMP":
                playsound('Sounds/Piano113.mp3', False)
    elif packetProtocols.L1 == "Token Ring":
        print("Not Implemented")
    else:
        print("Not fully implemented (POC)")

#
# An more efficent and effective way most likely exists. Spend an hour or so digging for potential methods of extracting the different protocols.
# Potential methods that didn't seem to work for the general case (needed) were sprintsf (https://scapy.readthedocs.io/en/latest/api/scapy.packet.html#scapy.packet.Packet.sprintf) and filtering using berkeley packet filter
#
def protocolExtractor(scapyPacket):
        # Un-able to find an easy way to extract each protocol so using a split method instead. Slightly hacky, likely there is a more efficent way to do so using scapy
    packetProtocols = classPacketProtocol
    def protocolHandler(protocol,layer):
        # Loads the Classes
        if "Raw" in packetSplit[i]:
            #call the synthesier
            PacketSynthesizer(packetProtocols)
        else:
            match layer:
                case 0:
                    packetProtocols.L1 = protocol
                case 1:
                    packetProtocols.L2 = protocol
                case 2:
                    packetProtocols.L3 = protocol
                case 3:
                    packetProtocols.L4 = protocol
                case 4:
                    packetProtocols.L5 = protocol
                case 5:
                    packetProtocols.L6 = protocol
                case 6: 
                    packetProtocols.L7 = protocol

    packetSplit = scapyPacket.split("/") # Splits up the layers
    # Loops through the split array
    for i in range(len(packetSplit)):
            protocolHandler(packetSplit[i], i)


    # Potential ideas are to use the protocol layers to equate to musictheory 
sniff = scapy.sniff(prn=lambda x:protocolExtractor(x.summary()))
