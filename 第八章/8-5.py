def describe_city(city_name = 'Reykjavik',country_belogs = 'Iceland'):
    '''
    描述城市属性的函数
    '''
    print(city_name.title()+" is in "+country_belogs.title())


describe_city()
describe_city('Beijing','China')
describe_city(city_name='Beijing', country_belogs='China')
