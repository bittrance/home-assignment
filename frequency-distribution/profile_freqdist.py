#!/usr/bin/env python

import cProfile, freqdist, random

char_base = open('./random-gorp').read()

print 'frequency_naive on chars'

cProfile.run('freqdist.frequency_naive(char_base)')

print 'frequency_charonly on chars'

cProfile.run('freqdist.frequency_charonly(char_base)')

words = [ 
    'clamor', 'clamored', 'clamoring', 'clamp', 'clampdown',
    'clamped', 'clamping', 'clan', 'clandestine', 'clandestinely',
    'clang', 'clanged', 'clanging', 'clangor', 'clank', 'clanked',
    'clanking', 'clannish', 'clap', 'clapboard', 'clapboarded',
    'clapboarding', 'clapped', 'clapper', 'clapping', 'claptrap',
    'claret', 'clarification', 'clarified', 'clarify', 'clarifying',
    'clarinet', 'clarinetist', 'clarinettist', 'clarion',
    'clarioned', 'clarioning', 'clarity', 'clash', 'clashed',
    'clashing', 'clasp', 'clasped', 'clasping', 'classed', 'classic',
    'classical', 'classically', 'classicism', 'classicist',
    'classier', 'classiest', 'classifiable', 'classification',
    'classified', 'classify', 'classifying', 'classing', 'classmate',
    'classroom', 'classy', 'clatter', 'clattered', 'clattering',
    'clause', 'claustrophobia', 'claustrophobic', 'clavichord',
    'clavicle', 'claw', 'clawed', 'clawing', 'clay', 'clayey',
    'clayier', 'clayiest', 'clean', 'cleaned', 'cleaner', 'cleanest',
    'cleaning', 'cleanlier', 'cleanliest', 'cleanly', 'cleanse',
    'cleansed', 'cleanser', 'cleansing', 'cleanup', 'clear',
    'clearance', 'cleared', 'clearer', 'clearest', 'clearing',
    'clearinghouse', 'clearly', 'cleat', 'cleavage', 'cleave',
    'cleaved', 'cleaver', 'cleaving', 'clef', 'cleft', 'clemency',
    'clement', 'clench', 'clenched', 'clenching', 'clerestory',
    'clergy', 'clergyman', 'clergymen', 'clergywoman', 'clergywomen',
    'cleric', 'clerical', 'clerk', 'clerked', 'clerking', 'clever',
    'cleverer', 'cleverest', 'cleverly', 'clew', 'clewed', 'clewing',
    'cliche', 'cliched', 'click', 'clicked', 'clicking', 'client',
    'clientele', 'cliff', 'cliffhanger', 'climactic', 'climate',
    'climatic', 'climax', 'climaxed', 'climaxing', 'climb',
    'climbed', 'climber', 'climbing', 'clime', 'clinch', 'clinched',
    'clincher', 'clinching', 'cling', 'clingier', 'clingiest',
    'clinging', 'clingy', 'clinic', 'clinical', 'clinically',
    'clinician', 'clink', 'clinked', 'clinker', 'clinking', 'clip',
    'clipboard', 'clipped', 'clipper', 'clipping', 'clipt', 'clique',
    'cliquish', 'clitoral', 'cloak', 'cloaked', 'cloaking',
    'cloakroom', 'clobber', 'clobbered', 'clobbering', 'cloche',
    'clock', 'clocked', 'clocking', 'clockwise', 'clockwork' ]

print 'frequency_naive on words'

wordgen = [random.choice(words) for n in xrange(len(char_base))]

cProfile.run('freqdist.frequency_naive(wordgen)')