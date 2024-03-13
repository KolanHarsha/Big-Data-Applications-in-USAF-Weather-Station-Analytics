from pyspark import SparkContext
import re

def parse_line(line):
    Id = line[4:10]
    height = line[70:75]
    q = line[63]

    if height != "99999" and re.match("[01459]", q):
        return Id.encode('utf-8'), int(height)
    else:
        return Id.encode('utf-8'), None

def main():
    sc = SparkContext(appName='Range_of_skyceiling_height')

    lines = sc.textFile('/home/23student23/input_project/Project_Data/*/*')
    Id_height = lines.map(parse_line)
    filtered_Id_height = Id_height.filter(lambda x: x[1] is not None)
    # calculate max height
    max_height = filtered_Id_height.reduceByKey(lambda a, b: max(a, b))
    # calculate min height
    min_height = filtered_Id_height.reduceByKey(lambda a, b: min(a, b))
    # Join max and min heights by key
    joined_heights = max_height.join(min_height)
    # Calculate the range
    height_range = joined_heights.mapValues(lambda x: x[0] - x[1])

    # Save the result to a file
    height_range.saveAsTextFile('/home/23student23/output_range')

    sc.stop()

if __name__ == "__main__":
    main()
