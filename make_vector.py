import sys
import re
import numpy as np
import os
from itertools import groupby
from more_itertools import chunked


def make_pitch2num(pitch_dict):
    compared_pitches = road_dictionaryfile(pitch_dict)
    length = len(compared_pitches)
    pitch2num = dict(zip(compared_pitches,list(range(length))))
    return pitch2num


def road_dictionaryfile(file_name,compared_pitches=[]):
    with open(file_name, 'r') as fp:
        for columns in fp:
            compared_pitches.append(columns.rstrip())
        return compared_pitches


def split_list_with_note(textfile_name,pitches=[]):
    texts = road_textfile(textfile_name)
    len_and_pits,part_lengths = make_parts(texts)
    len_and_pits_per_parts = split_part_with_z(len_and_pits,part_lengths,'Z')
    return len_and_pits_per_parts


def split_list_with_times(textfile_name,pitches=[]):
    texts = road_textfile(textfile_name)
    times = make_times(texts)
    len_and_pits,part_lengths = make_parts(texts)
    len_and_pits_per_parts = split_part_with_z(len_and_pits,part_lengths,'Z')
    return len_and_pits_per_parts



def road_textfile(file_name,datas=[]):
    with open(file_name, 'r') as fp:
        for columns in fp:
            each_parts = columns.rstrip()
            texts = re.split('[,]',each_parts)
            datas.append(texts)
    return datas 


def make_times(texts,times=[]):
    count = 1
    for idx,pitches in enumerate(texts):
        if idx == 0 or (idx%3 == 0):
            times.append(pitches)
    return times 


def make_parts(texts,pitch_freqs=[]):
    lengths=[]
    new_parts=[]
    count = 1
    for idx,pitches in enumerate(texts):
        if idx == 1 or (idx%3 == 1):
            lengths.append(len(pitches))
            for i,pitch in enumerate(pitches):
                if pitches[i-1] == pitches[i]:
                    count += 1
                else:
                    pitch_freqs.append(count)
                    pitch_freqs.append(pitches[i-1])
                    count = 1
            if len(pitch_freqs) > 3:
                continue
    new_parts = list(chunked(pitch_freqs,2))
    return new_parts,lengths

def split_part_with_z(pitches,lengths,compared_string):
    splitted_pitches=[]
    outputs = []
    z_lengths = [] 
    z_counter = 0
    length = len(pitches)
    for idx,pitch in enumerate(pitches):
        if compared_string in pitch:
            z_lengths.append(idx)
    z_lengths.append(length)

    max_z_length = len(z_lengths)
    for i,z_l in enumerate(z_lengths):
        if i > 0 and i < max_z_length:
            splitted_pitches.append(pitches[z_lengths[i-1]:z_lengths[i]:1])
    return splitted_pitches


def split_multi_pitch(pitches):
    split_number = "[CDEFGAHB]#*[0-9]"
    ps_lengths = []
    new_pitches = []
    new_parts = []
    for i,ps in enumerate(pitches):
        if len(ps[1]) > 3:
            ps_lengths.append(len(ps[1]))
            multi_pitches = split_multi_strings(ps[1],ps_lengths)
            del ps[1]
            ps.append(multi_pitches)
            new_pitches.append(ps[0])
            new_pitches.append(ps[1])
        else:
            new_pitches.append(ps[0])
            new_pitches.append(ps[1])
    return new_pitches


def split_multi_strings(string,lengths):
    split_number = "[CDEFGAHB]#*[0-9]"
    splitted_notes = []
    length_counter = 0
    for chord in re.findall(split_number,string):
        splitted_notes.append(chord)
        length_counter += len(chord)
        if length_counter == (length for length in lengths):
            pass
    return splitted_notes


def make_pitch_to_numbers(pitches,pitch2num):
    notes = []
    new_notes = []
    pitch_and_nums = convert_pitch_num(pitches,pitch2num)
    splitted_part_pitches = delete_not_extla_element(pitch_and_nums)
    integrated_lengths = integrate_pitch_length(splitted_part_pitches)
    return integrated_lengths


def convert_pitch_num(pitches,note2num,idxes=[]):
    for idx,pitch in enumerate(pitches):
        if pitch == '_':
            pitches[idx] == pitch
        elif type(pitch) is str and pitch != 'R' and pitch != '-':
            del pitches[idx]
            if pitch in note2num.keys():
                index = note2num.get(pitch)
                pitches.insert(idx,index)
        elif type(pitch) is int or type(pitch) is list:
            pitches[idx] == pitch
    del pitches[0]
    return pitches
    
    

def delete_not_extla_element(parts):
    compared_numbers = list(range(130))
    numbers = []
    newest_parts = []
    for i,p in enumerate(parts):
        if p == 'Z':
            del parts[i]
            del parts[i-1]
        elif p == 'R':
            del parts[i]
            del parts[i-1]
    
    for i,p in enumerate(parts):
        if p == '-':
            del parts[i]
            del parts[i-1]
    return parts
   

def integrate_pitch_length(pitches):
    new_pitches = list(chunked(pitches,2))
    for idx,pits in enumerate(new_pitches):
        if '_' in pits:
            new_pitches[idx-1][0] += pits[0]
            del new_pitches[idx]
    return new_pitches


def convert_multipitch_num(parts,note2num,idxes=[],mul_pits = []):
    for idx,pitches in enumerate(parts):
        for pits in pitches:
            for i,ps in enumerate(pits):
                if type(ps) is list:
                    for p in ps:
                        del pits[i]
                        if p in note2num.keys():
                            index = note2num.get(p)
                        pits.insert(i,index)
                else:
                    pits[i] == ps
    return parts
    


def make_vector(pitches,new_zeros=[]):
    zeros = np.zeros(130,dtype=int)
    for pitch in pitches:
        if type(pitch) is list or type(pitch) is str:
            pass
    for idx,zero in enumerate(zeros):
        new_zero = pitches[0] if idx == pitches[1] else 0
        new_zeros.append(new_zero)
    
    if len(new_zeros) > 130:
        del new_zeros[:130]
    return new_zeros


def make_multi_vector(sample_pitches,new_zeros = []):
    zeros = np.zeros(130,dtype=int)
    for idx,zero in enumerate(zeros):
        pitch_freq = sample_pitches[0]
        for pitches in sample_pitches:
            if type(pitches) is list:
                for pitch in pitches:
                    new_zero = pitch_freq if idx == pitch else 0
                    new_zeros.append(new_zero)
    if len(new_zeros) > 130:
        del new_zeros[:130]
    
    return new_zeros


def main(pitch_dict,textfile_name):
    pitch2num = make_pitch2num(pitch_dict)
    parts = split_list_with_note(textfile_name)
    times = split_list_with_times(textfile_name)
    
   
    new_pitches = []
    for part in parts:
        pitches = split_multi_pitch(part)
        new_pitch = make_pitch_to_numbers(pitches,pitch2num)
        new_pitches.append(new_pitch)
    multi_pitch_and_nums = convert_multipitch_num(new_pitches,pitch2num)
    new_parts = list(chunked(multi_pitch_and_nums,2))

    pitch_vectors = []
    part_vectors = []
    all_vectors = []
    for pitches in new_parts:
        for pitch in pitches:
            for pit in pitch:
                pitch_vector = make_vector(pit)
                pitch_vectors.append(pitch_vector)
            part_vectors.append(pitch_vectors)
    print(part_vectors)

if __name__ == '__main__':
    dictionary = sys.argv[1]
    textfile_name = sys.argv[2]
    main(dictionary,textfile_name)
