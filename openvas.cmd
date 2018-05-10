omp -u admin -w rockjeev8194@ --get-tasks
omp -u admin -w rockjeev8194@ -D '60f69658-502d-4bf6-bb8e-cf1d2777ce49'

with metasploit
===============
openvas_connect <username> <password> <host> 9390
openvas_target_create <name> <hosts> <comment>
openvas_task_create <name> <comment> <config_id> <target_id>
openvas_task_start <id>
openvas_task_list
openvas_task_delete <id> ok


0 - 4 : low
4 - 7 : medium
7 - 10: high 