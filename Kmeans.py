import matplotlib.pyplot as plt 
import random 
from math import *

 
class Point:
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def  __str__(self):
		return "("+str(self.x)+","+str(self.y)+")"



class KMeans:

	def __init__(self,K):
		self.K=K
		self.clusters=[]
		self.centroids=[]
		for i in range(K):
			self.clusters.append([])

	def initialize(self,Kpoints):

		for p in Kpoints:
			self.centroids.append(p)

	def Distance(self,p1,p2):
		return sqrt( pow((p1.x-p2.x),2)+pow( (p1.y-p2.y),2))

	def update(self,ans_cluster,p):

		centroid=self.centroids[ans_cluster]

		centroid.x = ( centroid.x + p.x) /2
		print(centroid.x)
		centroid.y = (centroid.y + p.y) /2
		print(centroid.y)

		self.centroids[ans_cluster]= centroid



	def addPoint(self,p):

		min_dist=100000000.0
		ans_cluster=-1
		for i  in range(self.K):

			pdist=self.Distance(self.centroids[i],p)

			if ( pdist < min_dist):

				min_dist=pdist
				ans_cluster=i

		self.clusters[ans_cluster].append(p)

		self.update(ans_cluster,p)


	def predict(self,newpoint):

		min_dist=10000000.0
		ans_cluster=-1

		for i in range(self.K):

			pdist=self.Distance(self.centroids[i],newpoint);

			if(pdist < min_dist):

				min_dist=pdist
				ans_cluster=i

		return ans_cluster+1


	def insert_Data(self,datapoints):

		inpoints=[]
		for i in range(self.K):
			inpoints.append(datapoints[i])

		self.initialize(inpoints)

		for i in range(self.K):
			datapoints.pop(0)

		for p in datapoints:
			self.addPoint(p)



	def optimize(self):
		for i in range(self.K):

			change_indices=[]
			final_clusters=[]

			for j in range(len(self.clusters[i])):

				p=self.clusters[i][j]

				present_distance=self.Distance(self.centroids[i],p)
				final_cluster=i


				for k in range(self.K):

					next_distacne=self.Distance(self.centroids[k],p)

					if( present_distance> next_distacne):
						present_distance=next_distacne
						final_cluster=k


				if( final_cluster!= i):
					change_indices.append(j)
					final_clusters.append(final_cluster)

			for l  in range(len(change_indices)):
				p=self.clusters[i][change_indices[l]]
				self.clusters[final_clusters[l]].append(p)

			cnt=0

			for indx in change_indices:
				self.clusters[i].pop(indx-cnt)
				cnt+=1

				





	def Graph(self):

		i=0
		colors=["blue","green","red","yellow","orange","cyan"] 
		for cluster in self.clusters:

			xpoints=[p.x  for p in cluster]
			ypoints=[p.y for p in cluster]

			plt.scatter(xpoints,ypoints,s=15,c=colors[i],label="cluster %s"%(str(i+1)))
			i+=1

		
		plt.show()




datapoints=[Point(0,0) for i in range(0,100)]    #creating 100 points 
   
for i in range(0,100): 

	#100  random points 

	x=random.randint(1,50)
	y=random.randint(1,50)

	if i > 49:
		x+=50
		y+=50

	datapoints[i].x=x
	datapoints[i].y=y




Testing=KMeans(2) # creating object to the alogrithm with 3 clusters 

Testing.insert_Data(datapoints)  #insertng all data 



Testing.optimize()  # apply optimization

Testing.Graph()  # check graph 




