"""
Script to fragment a given ipv6 packet

Using fragement6() function of scapy to generate fragments 
"""
__author__=='Ravi Kiran Chadalawada'
__email__ = "rchadala@usc.edu"
__status__ = "Prototype"


from scapy.all import *

sip = '1234:5678:9ABC:DEF1:2345:6789:ABCD:EF12'
dip = '1234:5678:9ABC:DEF1:2345:6789:ABCD:EF34'

def make_ipv6_fragments():
	payload = 'ravikiranc' * 1000
	pkt = IPv6(src=sip,dst=dip)/IPv6ExtHdrFragment(offset = 0, id=12345)/UDP(sport=1500,dport=1501)/payload

	frags = fragment6(pkt,1000) # 1000 is the intended size of each packet

	counter = 1

	for fragment in frags:
		print(str(counter))
		print("=================================")
		fragment.show()
		counter += 1


if __name__=="__main__":
	make_ipv6_fragments()
