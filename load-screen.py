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
 'summing', 'pseudo-summing', 'quantum summing', 'quantum scumming', 'thrimbaling',
 'de-thrimbaling', 'pseudo-thrimbaling', 'un-dethrimbaling', 're-dethrimbaling', 're-thrimbaling',
 'un-thrimbaling', 'undoing', 'save scumming', 'pseudo save-scumming', 'committing',
 'de-committing', 'attempting quantum committal of', 'attempting quantum de-committal of',
 'de-fragging', 're-fragging', 'un-fragging', 'fragging', 'un-defragging', 'quantum defragging',
 'quantum un-defragging', 'pseudo-defragging', 'pseudo-refragging', 'fucking with',
 'un-fucking', 'unscrewing', 're-screwing', 'rescuing', 'de-scrambling', 'unscrambling', 
 'under-scrambling', 'undercooking', 'cooking', 'preparing', 'unpreparing', 'disarming',
 'quantum-disarming', 'quantum scrambling', 'quantum dilating', 'dialing into', 
 'phoning', 'describing', 'generating configs for', 'generating trust for',
 'establishing trust in', 'governing', 'detecting', 'undetecting', 're-detecting', 
 'pseudo-detecting', 'super-detecting', 'undeleting save files for', 'deleting save files for',
 'redacting saved state of', 'redacting', 'un-redacting', 're-redacting', 're-re-redacting',
 'penetrating', "setting state 'ungovernable' for", 'setting up', 'tearing down',
 'making amends for', 'making peace with', 'making excuses for', 'super-positioning',
 'un-superpositioning', 'believing', 'unbelieving', 'trusting', 'untrusting',
 'being wary of', 'becoming suspicious of', 'reducing suspicious output of',
 'determining veracity of', 'determining trust in', 'finding out more about',
 'delivering', 'undelivering', 're-delivering', 'un-redelivering', 'submerging',
 'gently poking', 'gently assessing', 'asserting', 'unasserting', 'reasserting',
 'pushing', 'pulling', 'poking', 'hyperstretching',

   ]

object_property_list = ['unnecessary', 'lengthy', 'foolish', 'unbalanced', 'undiscoverable',
'unknowable', 'tiny', 'little', 'miniscule', 'nano-scale', 'pico-scale', 'giga-scaled',
'psuedo-strange', 'pseudo-quantum', 'pseudo-alerted', 'pseudo-smelly', 'pseudo-stinky',
'pseudo-tiny', 'pseudo-unknowable', 'pseudo-unbalanced', 'psuedo', 'rooted', 'unrooted',
'unhinged', 're-hinged', 'webhooked', 'load API for', 'root API for', 'secret API for',
'secret', 'secret path to', 'secret door into', 'secret butt stuff with', 'quantum API for',
'unfraggable', 'unfuckwithable', 'unponderable', 'unloadable', 'unlocated', 'relocated',
'redacted', 'un-redacted', 're-redacted', 'super-redacted', 'super-relatable', 'quintessential',
'relative', 'unrelated', 'unrelatable', 'fuckwithable', 'wild', 'silly', 'orphaned',
'widowed', 'widowered', 'resounding', 'formidable', 'bulky', 'fragged', 're-fragged',
'de-fragged', 'un-fragged', 'delta-wave', 'alpha-wave', 'zeta-wave', 'zeta-band',
'epsilon', 'diameterized', 'demilitarized', 'deduced', 'reduced', 'undue', 'undone',
'interesting', 'uninteresting', 'antithetical', 'un-antithetical', 'undiscovered',
'undiscoverable', 'scrambled', 'assessed', 'containable', 'containerized', 'uncontainerized',
'detected', 'undetected', 'superdetected', 'duplicated', 'sub-duplicated', 're-duplicated',
'unduplicated', 'duplicitous', 'untrustworthy', 'trustworthy', 'secured', 'un-secured',
'collated', 'un-collated', 'supercollated', 'hypercollated', 'superimposed',
'hyper-imposed', 'quantum disposition of', 'native habitat of', 'ionized', 're-ionized',
'un-deionized', 'hyperbolized', 'impenetrable', 'penetrable', 'super-positioned',
'supposable', 'theoretical', 'theorized', 'untheorized', 're-theorized', 'fingered',
'sleepy', 'folksy', 'dopey', 'doofed', 'mangled', 'marbled', 'ionic', 'unbelievable',

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
    print(str.capitalize(action_list[d1]) + " " + object_property_list[d2] + " " + object_list[d3] + "...")
    time.sleep(5)

# Calling the function as an infinite while loop
while __name__ == '__main__':
    loader()