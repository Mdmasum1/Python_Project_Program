# A barcode scanner can be configured by scanner a series of barcode in the correct order .
# Barcode configurations are encoded into a single string and store as a blob in the back-end system.
# The client requests in the configuration from the back-end configuration service ,
#  and needs to present the configuration in the correct order.The encoded configuration string
#  is a series of <ordinal-index><configuration>pairs separated by | .
#  The ordinal index value is a 4 digit numeric prefix with zeros.
#  For example, the first configuration will be represented as 0001.
#  The goal are to 1) validate the configuration string and
#   2). provide the configuration client the configuration values
#   in the order required to successfully configure the barcode scanner Validation Conditions:
#    *All configuartion must be seperated by a "|" characater.
#    *Configuration can not skip a number in the ordering .If there are three configuration strings , there must be a 1, 2, 3 index.
#    *Configuration values are alphanumeric and may contain no other characters.
#    *Configuration value length is exactly 10 characters.
#    *Ordinal indices may not repeat .
#    For example , There can not be two occurrences of number "1"
#    *Each configaration value is unique. configuration do not repeat
#    *"0000" is not a valid ordinal index If configuartion is not a valid ,
#    return ["Invlaid Coniguration"]
#    Examples: ##Happy path configuration = "0002f7c22e7904|000176a3a4d214|000305d29f4a4b"
#    #Based on the 'order' value , the expected output of this configuration string is "
#    ##output [ "76a3a4d214", #0001 "f7c22e7904",
#    #0002 "05d29f4a4b", #0003 #invalid configuration
#     #configuration = "0002f7c22e7904|000176a3a4d214|000205d29f4a4b"
#     #configuration string contains two indices for "0002" #Output #["Invalid configuration "]
#     Function description complete the function order_configuration in the editor below:
#     order_configuration has the following parameter(s): str configuration:
#      the encoded configuration string Returns : str configuration[n]: an array of configurations in the correct order

#      Constraints ans Assumptions:
#      *1 <=order <= 9999
#      *1 <= count(configuration) <= 9,999
#      *order values may not be always unique, the same configuration may appear in multiple configuration steps
#      #the below fucntion has to complete def order_configuration(configuration):
#      #write your code here pass if__name__=='__main__': "

# configuration = "0002f7c22e7904|000176a3a4d214|000305d29f4a4b"



def order_configuration(configuration):
    # Split the configuration string by the "|" character
    configs = configuration.split("|")
    
    # Create a dictionary to store the configurations with their ordinal indices
    config_dict = {}
    
    # Iterate over the configurations and validate them
    for config in configs:
        # Check if the configuration has a valid ordinal index
        if len(config) < 4 or not config[:4].isdigit() or config[:4] == "0000":
            return ["Invalid Configuration"]
        
        # Check if the configuration value has the correct length
        if len(config[4:]) != 10:
            return ["Invalid Configuration"]
        
        # Check if the ordinal index is unique
        if config[:4] in config_dict:
            return ["Invalid Configuration"]
        
        # Check if the configuration value is unique
        if config[4:] in config_dict.values():
            return ["Invalid Configuration"]
        
        # Add the configuration to the dictionary
        config_dict[config[:4]] = config[4:]
        
    # Sort the configurations based on their ordinal indices
    sorted_configs = [config_dict[key] for key in sorted(config_dict.keys())]
    
    return sorted_configs

if __name__ == '__main__':
    configuration = "0002f7c22e7904|000176a3a4d214|000305d29f4a4b"
    print(order_configuration(configuration))
