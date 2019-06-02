import d6tflow
import d6tflow.pipes

import cfg, tasks

d6tflow.pipes.init('top10-mistakes-stats', local_pipe=True) # save flow output to local pipe directory
pipe = d6tflow.pipes.get_pipe()
pipe.delete_files_local(confirm=False, delete_all=True) # start clean

# run tasks
d6tflow.run(tasks.ModelOutliers()) # output automatically saved in pipe directory
d6tflow.run(tasks.ModelTS())
d6tflow.run(tasks.OLSvsRF())

# push output
do_push = True
if do_push:
    d6tflow.pipes.init('top10-mistakes-stats', reset=True) # connect to remote pipe
    pipe = d6tflow.pipes.get_pipe()
    pipe.delete_files_remote(confirm=False) # start clean
    pipe.pull(cached=False)
    pipe.push()
