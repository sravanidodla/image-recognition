# image-recognition
1. Use Harris corner detection technique to find the key points of the enclosed image
• Display the original image with all detected points on the image.  
• Display the original image with the strongest 30 points on the image.     
2.  Write a program to perform K-means clustering technique using the points of part 1.  
• Display the original image with the detected clusters on it (use different colors).     
3. Write a program to draw a bounding box for each cluster of the data points of part 2.   
• Display the original image with the bounding boxes on it (use different colors). 

HARRIS CORNER DETECTOR:
Harris Corner Detector is a corner detection operator that is commonly used in computer vision algorithms to extract corners 
and infer features of an image. It was first introduced by Chris Harris and Mike Stephens in 1988 upon the improvement of 
Moravec's corner detector. Compared to the previous one, Harris' corner detector takes the differential of the corner score 
into account with reference to direction directly, instead of using shifting patches for every 45 degree angles, and has been proved 
to be more accurate in distinguishing between edges and corners.[2] Since then, it has been improved and adopted in many algorithms 
to preprocess images for subsequent applications.

k-means clustering algorithm:
k-means is  one of  the simplest unsupervised  learning  algorithms  that  solve  the well  known clustering problem. 
The procedure follows a simple and  easy  way  to classify a given data set  through a certain number of  clusters (assume k clusters) fixed apriori. 
The  main  idea  is to define k centers, one for each cluster. These centers  should  be placed in a cunning  way  because of  different  location  causes different  result. 
So, the better  choice  is  to place them  as  much as possible  far away from each other. The  next  step is to take each point belonging  to a  given data set and associate it 
to the nearest center. When no point  is  pending,  the first step is completed and an early group age  is done. At this point we need to re-calculate k new centroids as barycenter of 
the clusters resulting from the previous step. After we have these k new centroids, a new binding has to be done  between  the same data set points  and  the nearest new center. 
A loop has been generated. As a result of  this loop we  may  notice that the k centers change their location step by step until no more changes  are done or  in  other words centers do 
not move any more. Finally, this  algorithm  aims at  minimizing  an objective function know as squared error function.

