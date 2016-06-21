
#Brandyn Deffinbaugh & James Gray
#Ridge Regression for Phenotype(X) and Genotype(Y) using Sci-Kit Learn
#May 2016

from sklearn import preprocessing
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import Ridge
import numpy as np
import os



def inputParse(file):
   pheno = []
   geno = []
   with open(file) as infile:
       for line in infile:
       	   line = line.strip('\n')
           line = line.replace(' ','\t',6)
           line = line.split('\t')
           genoHold = line[6]
           genoHold = genoHold.split(' ')
           phenoHold = line[5]
           geno.append(genoHold)
           pheno.append(phenoHold)
   return(pheno,geno)


#Transposes the matrix
def transpose(mtx):
   transpose = list(zip(*mtx))
   return transpose

def makeGenoAverages(length,lenInnerGeno):
   genoAvgMake = []
   for i in range(length):
       for x in range(lenInnerGeno):
           genoInner = geno[i][x]
           iterate = 0
           for j in range(len(allGeno)):
               genoMake[iterate]=genoInner.count(genoInner[j])
               iterate +=1
           total = 0
           for j in genoMake:
               total += x
           for j in range(len(genoMake)):
               genoMake[x] = genoMake[j]/total
   return genoMake


def alphaOptimization():
   alphas = np.array([1,0.1,0.01,0.001,0.0001,0.5,0.05,0.2,0.002,0])
   modal = Ridge()
   grid = GridSearchCV(estimator = model, param_grid=dict(alpha=alphas))
   grid.fit()


def RidgeRegression(file):
   pheno,geno = inputParse(file)
   maxGeno = max(geno)
   allGeno = list(set(maxGeno))
   encoder = [i for i in range(len(allGeno))]
   lengthGeno = len(geno)
   length = len(geno)
   lenInnerGeno = len(geno[0])
   genoMake = [0 for x in range(len(allGeno))]
   dictionary = dict(zip(allGeno,encoder))
   for i in range(length):
       for x in range(lenInnerGeno):
           geno[i][x] = dictionary[geno[i][x]]
   print dictionary
   geno = transpose(geno)
   #print geno
   genoAvg = []
   preAverageValues = []
   for snpSet in geno:
    	countA = snpSet.count('A')
    	countB = snpSet.count('B')
    	#count0 = snpSet.count('0')
    	values = (countA,countB) #,count0)
    	preAverageValues.append(values) 
   #print preAverageValues
   for i in preAverageValues:
        genoAvg.append(np.mean(i))
   #print genoAvg
   #print np.mean(genoAvg)
   #print max(genoAvg)
   #print min(genoAvg)
   print len(geno)
   clf = Ridge(alpha=1.0)
   np.reshape(844,280)#np.reshape(geno)
   clf.fit(geno,pheno)
   ridge(alpha=1.0, copy_x = True, fit_intercept = True, max_iter = None, normalize = False, Random_state = None, solver = 'auto', tol = 0.001)
   #print sorted(genoAvg)
   # for SNP in geno:
   # 		for i in SNP:
   # 			if i == 'A'
   # 			countA = geno.count('A')
	  #   	countB = geno.count('B')
	  #   	countC = geno.count('0')
	  #   	values = (countA,countB,countC)
	  #   	preAverageValues.append(values)
   # print geno
   # print preAverageValues	   
   #genoAvgMake = makeGenoAverage(geno,length,lenInnerGeno,genoMake)

RidgeRegression("dongwang.ped")