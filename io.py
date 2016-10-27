#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Copyright © 2016 gabbar1947 <gabbar1947@Rathores-MBP>
# Distributed under terms of the MIT license.

import numpy as np
import json
from pprint import pprint
import os

def create_image_lists(image_dir, testing_percentage, validation_percentage):

    #if not gfile.Exists(image_dir):
    #    print("Image directory '" + image_dir + "' not found.")
    #    return None
    
    with open('dt_pd_ntop30.json') as data_file:    
            data = json.load(data_file)
    
    Name = []
    Features = []

    for vect in (data.values()):
        Pth = os.path.join(image_dir, vect[u'file_name']);
        Name.append(Pth)
        Features.append(vect[u'dt_pd'])

    INP={}

    for i in range(len(Name)):
        INP[Name[i]] = Features[i]


    print(INP);

create_image_lists('joyneel/',98,23);
