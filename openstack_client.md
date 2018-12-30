from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client
auth = v3.Password(auth_url="http://controller:5000/v3", username="admin", password="password", project_name="CCC", user_domain_id="default", project_domain_id="default")
sess = session.Session(auth=auth)
keystone = client.Client(session=sess)
keystone.projects.list()

from novaclient import client
nova = client.Client(2, username=USERNAME, password=PASSWORD, project_name=“Game Lab”, auth_url=AUTH_URL, user_domain_name=USER_DOMAIN_NAME,session=sess)

nova.servers.list()

>>> nova.instance_action.list(nova.servers.list()[0])
[<InstanceAction action=create, instance_uuid=d89894de-0a46-4281-be3b-0ff26b22b10c, message=None, project_id=68e62f3802fd4799b3917e196fe8f268, request_id=req-9debd98b-b16e-4850-a119-ad432c2aa568, start_time=2018-12-12T18:22:59.000000, user_id=ceffc9076298425192b052717aacc5ae>]

>>> nova.instance_action.list(nova.servers.list()[0])[0].action
u'create'

>>> keystone.projects.list()[1]
<Project description=Dr Khanjari Lab project, domain_id=default, enabled=True, id=04de9f32a9cd4003a2030f7e298baf00, is_domain=False, links={u'self': u'http://controller:5000/v3/projects/04de9f32a9cd4003a2030f7e298baf00'}, name=Dr. Khanjari Lab, parent_id=default, tags=[]>

