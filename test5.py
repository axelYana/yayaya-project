# Import lib
import pandas as pd
import numpy as np

# Import my lib
from nomenclature import sectors, praexoSectors
from Param import (deals_primaryIndustryGroup, deals_primaryIndustrySector, deals_verticals,
                   deals_dealType, deals_Series,
                   deals_postValuation, deals_dealSize,
                   deals_primaryIndustryCode, deals_hqLocation)

# Find the Primary sector
def findSector(primaryIndustryGroup_value, verticals_value):
    global sector
    path = 'Data/kw.xlsx'
    df_sector = pd.read_excel(path, sheet_name='Feuil1', header=1)
    if primaryIndustryGroup_value == 'Restaurants' or primaryIndustryGroup_value == 'Hotels and Leisure':
        sector = 'Travel, tourism & leisure'
    else: # verticals_value == '\u00a0':
        for i in range(len(df_sector)):
            for industryGroup in sectors[praexoSectors[i]]['pitchbookGroups']:
                if industryGroup == primaryIndustryGroup_value:
                    sector = praexoSectors[i]
    '''else:
        for i in range(len(df_sector)):
            for primaryGroup in sectors[praexoSectors[i]]['pitchbookGroups']:
                for vertical in sectors[praexoSectors[i]]['pitchbookVerticals']:
                    if primaryGroup == primaryIndustryGroup_value and vertical == verticals_value:
                        sector = praexoSectors[i]'''
    return sector


# Determine the emission stage and find all
def getEmissionStage(series, dealType):
    if series != '\u00a0':
        if series in ['Series AA', 'Series A1', 'Series A2', 'Series A3']:
            emission_stage = 'Series A'
        elif series in ['Series BB', 'Series B1', 'Series B2', 'Series B3']:
            emission_stage = 'Series B'
        elif series in ['Series CC', 'Series C1', 'Series C2', 'Series C3']:
            emission_stage = 'Series C'
        elif series in ['Series D1', 'Series D2', 'Series D3']:
            emission_stage = 'Series D'
        else:
            emission_stage = series
    else:
        if dealType == "Later Stage VC":
            emission_stage = 'Series F'
        elif dealType == "Early Stage VC":
            emission_stage = 'Series A'
        else:
            emission_stage = dealType
    return emission_stage


def findInvestors(series, dealType, dealSize):
    investors_accepted = []
    emission_stage = getEmissionStage(series, dealType)
    seriesList = ['Series A', 'Series B', 'Series C', 'Series D', 'Series E', 'Series F', 'Series G', 'Series H',
                  'Series I', 'Series J', 'Series K', 'Corporate', 'IPO', 'PE Growth/Expansion', 'PIPE',
                  'Secondary Transaction - Private']

    if emission_stage == 'Series A' or emission_stage == 'Series B':
        investors_accepted = ['Seed', 'Series A', 'Series B', 'Series C', 'Series D', 'Corporate']
        if dealSize >= float(100.0):
            investors_accepted.extend(['IPO', 'PIPE'])
    elif emission_stage == 'Series C':
        investors_accepted = ['Series A', 'Series B', 'Series C', 'Series D', 'Series E', 'Corporate']
        if dealSize >= 100.0:
            investors_accepted.extend(['IPO', 'PIPE'])
    elif emission_stage == 'Series D':
        for i in seriesList:
            if i != 'Series A':
                investors_accepted.append(i)
    elif emission_stage == 'Series E' or emission_stage == 'Series F':
        for i in seriesList:
            if i != 'Series A' and i != 'Series B':
                investors_accepted.append(i)
    elif emission_stage > 'Series G' or emission_stage == 'PIPE' or emission_stage == 'PE Growth/Expansion':
        for i in seriesList:
            if i != 'Series A' and i != 'Series B' and i != 'Series C':
                investors_accepted.append(i)
    return investors_accepted


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
