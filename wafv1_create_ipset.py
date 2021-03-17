import boto3

your_list = ['1.1.1.1/32','1.1.1.2/32']

client_waf = boto3.client('waf')

def get_change_token():
    return client_waf.get_change_token()['ChangeToken']

#Create IP Set


ip_set_name = str(input('IP_Set Name: '))


response_create_ipset = client_waf.create_ip_set(
    Name=ip_set_name,
    ChangeToken=get_change_token()
)

ip_set_id = response_create_ipset['IPSet']['IPSetId']



#Add to IP Set

ip_update = []

for x in your_list:
    ip_loop={
            'Action': 'INSERT',
            'IPSetDescriptor': {
                'Type': 'IPV4',
                'Value': x
            }}
    ip_update.append(ip_loop)


response_update_ipset = client_waf.update_ip_set(
        IPSetId=ip_set_id,
        ChangeToken=get_change_token(),
        Updates=ip_update
    )
