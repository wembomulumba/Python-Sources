#FDemonstrating the difference between turples and list
#Author : Wembo Otepa Mulumba

#List examples
import sys
import timeit
print(dir(sys))

list_eg = (1,2,3,"a","b","b", True,  3.141)
turple_eg = (1,2,3,"a","b","b", True,  3.141)

print("list size = ", sys.getsizeof(list_eg))
print("list size = ", sys.getsizeof(turple_eg))

#Lists          Tuples
#Add Data       cannot be
#Remove Data    Immutable
#Change Data    Made Quickly
