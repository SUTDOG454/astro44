from astroos.engines.aspects import detect_aspects
from astroos.engines.midpoints import midpoint_longitude
from astroos.engines.dignities_complete import compute_dignity
from astroos.research.backtest import walk_forward

def test_aspect_and_midpoint():
    a=[{'id':'sun','longitude':0,'speed':1},{'id':'moon','longitude':90,'speed':13}]
    assert detect_aspects(a)[0]['aspect']=='square'
    assert midpoint_longitude(350,10)==0

def test_complete_dignity():
    d=compute_dignity('sun',0,'day'); assert 'exaltation' in d['conditions']

def test_walk_forward():
    assert len(walk_forward(list(range(10)),4,2))==3
