from classical_solver import classical_solver
import event_model_modified as em
import validator_lite as vl
import json
import matplotlib.pyplot as plt   
from validator_lite import *

# Get an event
f = open("velojson/1.json")
json_data = json.loads(f.read())
event = em.event(json_data)
f.close()


# Get all tracks by using the classical method and print them
print("Invoking classical solver...")
classical = classical_solver()
classical_tracks = classical.solve(event)
print("Found", len(classical_tracks), "tracks")

# Validate the event
#vl.validate_print([json_data], [classical_tracks])
#print('RE long>5GeV, [0-1]:', vl.validate_efficiency([json_data], [classical_tracks], 'long>5GeV'))
#print('CF long>5GeV, [0-1]:', vl.validate_clone_fraction([json_data], [classical_tracks], 'long>5GeV'))
#print('GF of all tracks, [0-1]:', vl.validate_ghost_fraction([json_data], [classical_tracks])) 

# Obtaining the length of the reconstructed tracks

hits_length = []
for i in range(len(classical_tracks)):
	single_track = classical_tracks[i].hits
	hits_length.append(len(single_track))



# Export the data so I can represent it using gnuplot

file1 = open('file_hist.dat','w')
bins = np.zeros((24),dtype='uint8')


for i in range(2,27,1): 
    for element in hits_length: 
        if element == i:
            bins[i-2] = bins[i-2] + 1

bins = str(bins)            
file1.write(bins)
file1.close()

