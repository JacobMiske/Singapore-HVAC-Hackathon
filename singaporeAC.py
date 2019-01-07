# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 10:26:39 2019

@author: Jacob Miske
"""


### General Variables ###
populationSG = 5.612*10**6 #Google result, number of people
householdsSG = 1263.6 #https://www.singstat.gov.sg/find-data/search-by-theme/households/households/latest-data
personsperhousehold = 3.35; homeOwnershipRate = 90.9 #percentage
coolingCapacity = 2500 #Watts per day for standard AC in Singapore, for 35m^2, 60c/day, https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&cad=rja&uact=8&ved=2ahUKEwj3xvm22NrfAhWLV30KHaBcBgcQFjACegQIBxAK&url=https%3A%2F%2Fwww.mitsubishi-les.com%2Fen%2Fproducts%2Fair-conditioners%2Fm-series%2Fenergy-savings.html&usg=AOvVaw0dREbqkMV-xtrcwg3K7Dlr
EperA = 2500/35 #Watts/m^2 of cooled space
livingSpaceAperPerson = 23.969 #square meters per person in Singapore, https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=2ahUKEwiMv9yR2drfAhVTWH0KHZQVDiEQFjABegQIBhAF&url=https%3A%2F%2Fwww.scmp.com%2Fcomment%2Finsight-opinion%2Farticle%2F2084697%2Fhong-kongs-housing-situation-dire-compared-singapores-heres&usg=AOvVaw3QWUEbLNDgtQ14rFD7zXqm
wattsPerPerson = EperA*livingSpaceAperPerson




