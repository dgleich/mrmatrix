#!/bin/bash

# hadooprun.sh
# run a program for all files given in an input
# usage:
#   ./hadooprun.sh command hadoop-glob suffix [options]
# will run
#   command <file>
# for each <file> in the hadoop glob
# and store the output to
# <file>.suffix
#
# options include
#   -v   verbose

mydir=`dirname "$0"`
mydir=`cd "$mydir"; pwd`
cd $mydir

# find Hadoop
HADOOP_DIR=/usr/lib/hadoop
HADOOP_STREAMING_JAR=`find $HADOOP_DIR/ | grep hadoop-streaming`

COMMAND=$1
# clear the $1 option
shift $(( 1 ))

FILES=$1
# clear the $1 option
shift $(( 1 ))

SUFFIX=#1
# clear the $1 option
shift $(( 1 ))

while getopts ":v" opt; do
  case $opt in
    v)
      VERBOSE=1
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

FILELIST=`hadoop fs -ls $FILES | awk '{print $8}'`

echo "Files to process:"
echo $FILELIST

FILELISTFILE=tmp/filelist.txt
FILELISTOUTPUT=tmp/filelist-results.txt
echo $FILELIST > hadoop fs -put - $FILELISTFILE

before="$(date +%s)"
hadoop jar $STREAMING_JAR -input $FILELISTFILE -output $FILELISTOUTPUT \
  -jobconf mapreduce.job.name=hadooprunner \
  -io text \
  -outputformat 'org.apache.hadoop.mapred.TextOutputFormat' \
  -inputformat 'org.apache.hadoop.mapred.NLineInputFormat' \
  -file $mydir/hadooprunner.sh \
  -file $COMMAND \
  -mapper "bash ./hadooprunner.sh"
