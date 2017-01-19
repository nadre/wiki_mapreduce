# Wiki Map Reduce

Mapper and reducer for a hadoop streaming mapreduce job.

Takes wiki.ldjson files as input. Needed attributes are title, text and id.

## Local Testing

```
cat wiki.ldjson | mapper.py | sort -k1,1 | reducer.py
```