# E444-F2024-PRA5

The boxplot illustrates the distribution of latency (in milliseconds) for each test case. Key elements of the plot include:

**Box**: The box represents the interquartile range (IQR), which contains the middle 50% of the latency data. The lower and upper edges of the box correspond to the 25th and 75th percentiles, respectively.

**Median**: The horizontal line inside the box indicates the median (50th percentile) latency, representing the central tendency of the data.

**Whiskers**: The lines extending from the top and bottom of the box are called whiskers. They represent the range of data within 1.5 times the IQR from the upper and lower quartiles. The whiskers show the spread of the latency values, excluding extreme outliers.

**Outliers**: The circles outside the whiskers are outliers—latency measurements that fall outside the range of typical values. These outliers indicate unusually high or low latencies compared to the rest of the data.

## boxplot
![alt text](results/boxplot/latency_boxplot.png)

## boxplot shrinked

since the max values for each test would be greater than 1000, while the rest would usually be less than 150, i add a shrink version like zoom-in the boxplot
![alt text](results/boxplot/latency_boxplot_shrink.png)
