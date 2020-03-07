# Heights
First thing we did was narrowing down the size of the table. We began by creating a new text file for each species 
containing only relevant information which includes species ID, total height, status ID,
and inventory year.

In each generated text file, we would look only the live trees. Since the dead tree whose data was collected in the past
would be too trivial to look into. From all the live trees of each speacies, we calculated a maximum, mean, a standard 
deviation, and a median of the total height. 

With the calculated values, we generated a new output file (.csv) which contains the statistics for all the species. 
In each row of the output file, there is also a inventory year of the tallest tree. 

Since we have only looked at the live trees, we found the height of the tallest live tree of each species. 
