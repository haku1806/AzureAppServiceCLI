
subName = input("Subscription name Azure: ")
groupName = input("Resource group Azure: ")

with open('domain.txt', 'r') as f:
    with open('scriptdomain.txt', 'w') as fo:
        fo.write(f"az account set --subscription '{subName}'\n\n")
        for i in f.readlines():
            fo.write("az appservice domain create -g {} --hostname {} --contact-info=@'contact.json' --accept-terms\n".format(groupName, i.strip('\n')))
