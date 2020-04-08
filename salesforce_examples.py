from simple_salesforce import Salesforce


def main():
    sf = Salesforce(username='username_goes_here', password='password', security_token='token')
    response = sf.query("SELECT Id, Name FROM Contact WHERE FirstName = 'Edmond'")
    print(response)


if __name__ == '__main__':
    main()
