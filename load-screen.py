# Import necessary functions
import random
import time

# Define lists of funny technobabbly load screen terms
action_list = ['booting', 'cracking', 'hyperadjusting', 'importing telemetry for',
 'cyberhammering', 'figuring out', 'adjusting malfeasance in', 'puttering about with',
 'monkeying with', 'unfluffing', 'tenderizing', 'reticulating', 'iterating',
 're-iterating', 'de-iterating', 'calculating', 'foraging for', 'importing configs from',
 'faffing about with', 'delineating', 'calculating atomic weight for', 
 'establishing emotional bond with', 'maintaining good relations with',
 'synergizing', 'repairing strained relationship with', 'eating', 'digesting',
 'hiding footprints of', 'de-masticating', 'pulling index for', 'non-euclidifying',
 'rooting', 'un-rooting', 'sowing', 'techno-spraying', 'pounding', 'apologizing for',
 'cyber-oiling', 'quantum lubricating', 'quantum de-escalating', 'explaining things to',
 'finding excuses for', 'maintaining phase array within', 'ejecting', 
 'recycling', 'auditioning', 'quantum tangentifying', 'enlightening', 'obscuring',
 'rectifying', 'bringing home', 'calling for', 'on hold with', 'establishing neural uplink to',
 'phasing neural uplink for', 'contacting', 'beaming', 'artificing', 'pinging',
 'smothering', 'load balancing', 'unbalancing load for', 'calcuating ideal loading message for',
 'finding the square root of', 'formatting', 'attempting to run Doom with', 
 'using', 'abusing', 'establishing boundaries for', 'distancing oneself from', 
 'codifying', 'conditioning', 'cross-training', 'specializing', 'certifying', 
 'carbon-dating', 'allowing', 'airing out', 'engaging', 'engaging with', 
 'engaging engagement for', 'guillotining', 'defenestrating', 'yanking on', 
 'finding', 'finding out about', 'learning about', 'teaching someone about',
 'training', 'bootstrapping', 'orphaning', 'widowing', 'widowering', 'winnowing',
 'flattering', 'flattening', 'fattening', 'forge-welding', 'making amends with',
 'befriending', 'unfriending', 'unloading', 'trashing', 'recycling', 'upcycling',
 'unflattering', 'unflattening', 'unfattening', 'nattering on about', 'going on about',
 'blathering to', 'blathering about', 'blathering on about', 'continuing to blather about',
 'teaching chess to', 'teaching ping-pong to', 'unpinging', 'de-pinging', 'degloving', 
 'de-blathering', 'de-bloating', 'bloating', 'unbloating', 'rebloating', 'sub-bloating',
 'hyperscaling', 'nanoscaling', 'nanopinging', 'nanoforging', 'nano-dithering', 
 'quantum dithering', 'quantum scaling', 'explaining The Room to', 'explaining The Matrix to',
 'explaining quantum theory to', 'explaining Twilight to', 'explaining human emotion to',
 'logging emotional state of', 'logging win-loss ratio of', 'logging quantum dithering for',
 'knowing', 'finding known knowns of', 'unlearning', 'unknowing', 'relearning',
 'establishing squishiness of', 'establishing fluffiness of', 'establishing alibi for',
 'establishing LLC for', 'establishing legal case for', 'establishing possibility of',
 'denying any knowledge of', 'denying any affection for', 'denying proximity to',
 'establishing proxmimity to', 'distancing child processses from', 'digitizing',
 'de-digitizing', 'invigorating', 'unvigorating', 'establishing lactose tolerance of',
 'quantum unvigorating', 'quantum revigorating', 'pseudo-encrypting', 'pseudo-decrypting',
 'telling secrets to', 'attempting to reason with', 'establishing governability for',
 'setting conditions for', 'processing', 'pseudo-processing', 'nano-processing', 
 'quantum processing', 'quantum diving into', 'farting around with', 'taking the piss out of',
 'de-codifying', 'quantum encoding', 'pseudo-encoding', 'pseudo-decoding', 'pseudo-bloating',
 'ossifying', 'de-ossifying', 'pseudo-ossifying', 'nano-ossifying', 'being rude to',
 'stretching', 'pseudo-stretching', 'quantum stretching', 'oscillating', 'de-oscillating',
 'un-oscillating', 'nano-oscillating', 'pseudo-oscillating', 'establishing 1337ne55 of',
 'establishing credibility of', 'questioning credibility of', 'denying credibility of',
 'denying membership to', 'denying citizenship to', 'coming clean about', 'coming clean about feelings regarding',
 'putting good vibes out for', 'putting bad vibes out for', 'vibe-checking', 
 'blowing gently on', 'brushing up against', 'avoiding contact with', 'incorporating',
 'decorporating', 'disapparating', 'determining rhizomal composition of', 
 'determining properties of', 'determining culpability of', 'determining purpose of',
 'determining length of', 'determining configuration for', 'establishing naughtiness of',
 'determining height of', 'determining width of', 'determining volume of', 
 'determining weight of', 'determining quantum state of', 'data-mining', 
 'extorting', 'debriefing', 'un-debriefing', 're-debriefing', 'anti-debriefining',
 'creating new sub-routine for', 'creating', 'un-creating', 'recreating', 'de-creating',
 'evaluating nutritional content of', 'evaluating quantum content within', 'evaluating pseudo-encryption standards for',
 'giving root access to', "giving membership of group 'wheel' to", 'exercising',
 'exorcising', 'exacerbating', 'un-exacerbating', 'de-exacerbating', 're-exacerbating',
 'quantum tunneling', 'observing', 'un-observing', 're-observing', 'un-re-observing',
 'escalating', 'de-escalating', 're-escalating', 'un-escalating', 'un-de-escalating', 
 'translating', 'de-translating', 're-translating', 'un-retranslating', 'un-detranslating',
 'quantum translating', 'quantum de-translating', 'quantum re-translating', 'restraining',
 'applying constraints to', 'unapplying constraints on', 'disapplying quantum constraints for',
 'applying floral preference to', 'applying qauntum preference to', 'applying escalation preferences to',
 'unhinging', 'hinging', 're-hinging', 'changing', 'pseudo-channeling', 
 'channeling', 're-channeling', 'de-channeling', 'un-channeling', 'quantum channeling',
 'summing', 'pseudo-summing', 'quantum summing', 
  ]

object_property_list = ['unnecessary', 'lengthy', 'foolish', 'unbalanced', 'undiscoverable',
'unknowable', 'tiny', 'little', 'miniscule', 'nano-scale', 'pico-scale', 'giga-scaled',
'psuedo-strange', 'pseudo-quantum', 'pseudo-alerted', 'pseudo-smelly', 'pseudo-stinky',
'pseudo-tiny', 'pseudo-unknowable', 'pseudo-unbalanced', 'psuedo', 'rooted', 'unrooted',
'unhinged', 
 
]

object_list = ['load arguments', 'toughnut.dll', 'property', 'theory', 'dithers',
'foray', 'flowerchild'
]

# Main function to generate fun loading messages. Pulls a random number for the
# index of both the action list and the object list, then joins those two random
# numbers to create a silly loading message.
def loader():
    d1 = random.randint(0,int(len(action_list) - 1))
    d2 = random.randint(0,int(len(object_property_list) - 1))
    d3 = random.randint(0,int(len(object_list) - 1))
    print(str.capitalize(action_list[d1]) + " " + object_property_list[d2] + " " + object_list[d3])
    time.sleep(5)

# Calling the function as an infinite while loop
while __name__ == '__main__':
    loader()