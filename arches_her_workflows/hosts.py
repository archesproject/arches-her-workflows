import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(
        re.sub(r"_", r"-", r"arches_her_workflows"),
        "arches_her_workflows.urls",
        name="arches_her_workflows",
    ),
)
