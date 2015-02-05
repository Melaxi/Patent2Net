# -*- coding: utf-8 -*-
"""
Created on Wed Feb 04 12:13:51 2015

@author: Mériem
"""

"""module biblioP2N contenant les fonctions pour la création du réseau Gephi"""


def ExtraitMinDate(noeud):
        if noeud.has_key('time'):
            for i in noeud['time']:
                mini = 3000
                if i[1] < mini:
                    mini = i[1]
        else:
            mini = dateDujour
        return mini
    
def getStatus2(noeud, listeBrevet):
        for Brev in listeBrevet:
            if Brev['label'] == noeud:
                return Brev['portee']
        return ''
def getStatus(noeud, listeBrevet):
        for Brev in listeBrevet:
            if Brev['label'] == noeud:
                if isinstance(Brev['status'], list):
                    if len(Brev['status']) == 1:
                        if isinstance(Brev['status'][0], list):
                            if len(Brev['status'][0]) == 1:
                                return Brev['status'][0][0]
                            else:
                                return Brev['status'][0] #have to deal with list and attributes....}
                        else:
                            return Brev['status'][0]
                    else:
                        Brev['status'][0]
                return Brev['status']
        return 'NA'
def getClassif(noeud, listeBrevet):
        for Brev in listeBrevet:
            if Brev['label'] == noeud:
                return Brev['classification']
        return 'NA'
    
def getCitations(noeud, listeBrevet):
        for Brev in listeBrevet:
            if Brev['label'] == noeud:
                if Brev.has_key('citations'):
                    return Brev['citations']
                else:
                    return 0
        return 0
    
def getFamilyLenght(noeud, listeBrevet):
        for Brev in listeBrevet:
            if Brev['label'] == noeud:
                if Brev.has_key('family lenght'):
                    return Brev['family lenght']
                else:
                    return 0
        return 0
        
def getPrior(noeud, listeBrevet):
        for Brev in listeBrevet:
            if Brev['label'] == noeud:
                return Brev['prior']
        return ''
    
def getActiveIndicator(noeud, listeBrevet):
        for Brev in listeBrevet:
            if Brev['label'] == noeud:
                return Brev['priority-active-indicator']
        return 0
    
def getRepresentative(noeud, listeBrevet):
        for Brev in listeBrevet:
            if Brev['label'] == noeud:
                return Brev['representative']
        return 0
    
