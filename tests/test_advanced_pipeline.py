from astroos.predictive.primary_directions import symbolic_primary_direction
from astroos.synastry.angles import whole_sign_houses
from astroos.intelligence.temporal_model import sequence_windows

def test_primary_direction_contract():
 r=symbolic_primary_direction('sun',90,'mc','sun'); assert r['arc_degrees']==90

def test_houses(): assert len(whole_sign_houses(10))==12

def test_windows(): assert len(sequence_windows(list(range(10)),3,1))==7
