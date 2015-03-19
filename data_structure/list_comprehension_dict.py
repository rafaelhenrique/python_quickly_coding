my_dict_list = []

for i in range(1, 40000):
    # example for event on puppetdb api
    my_dict_list.append({
        u'status': u'success',
        u'configuration-version': u'1426611919',
        u'property': u'ensure',
        u'new-value': u'latest',
        u'resource-title': u'/usr/lib64/python2.6/site-packages/system',
        u'timestamp': u'2015-03-17T17: 05: 26.357Z',
        u'old-value': u'present',
        u'certname': u'host.mydomain',
        u'resource-type': u'Vcsrepo',
        u'run-end-time': u'2015-03-17T17: 05: 24.681Z',
        u'run-start-time': u'2015-03-17T17: 05: 16.673Z',
        u'containment-path': [
            u'Stage[main]',
            u'System: : App',
            u'Vcsrepo[/usr/lib64/python2.6/site-packages/system]'
        ],
        u'file': u'/etc/puppet/modules/system/manifests/app.pp',
        u'report-receive-time': u'2015-03-17T17: 05: 30.847Z',
        u'report': i,
        u'message': u"ensure changed 'present' to 'latest'",
        u'containing-class': u'System: : App',
        u'line': 37
    })

# store report ids on list test
test = [dicio['report'] for dicio in my_dict_list]

# for time measure
from time import time
start = time()

if 39970 in test:
    print('Find!')
else:
    print('Not find!')

if 'abacaxi' in test:
    print('Find!')
else:
    print('Not find!')

if (time() - start < 1):
    print("Time is good: {}".format(time() - start))
else:
    print("Time is not good: {}".format(time() - start))
