import configparser

config = configparser.ConfigParser()
config['API'] = {'key': input("what is your api key: ")}

# Save the configuration to a file
with open('config.ini', 'w') as config_file:
    config.write(config_file)
