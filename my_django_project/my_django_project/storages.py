from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = "b0030724dcbs"
    account_key = "BtbCdiYL2rZWe7sh5w2QoMQtL0Lol5QvQg7AHl6xluLrfvpNPz1CGsR/B8hL5FAsvf2NAnc9qpSE+AStYr5X1Q=="
    azure_container = "media"
    expiration_secs = None    
    
class AzureStaticStorage(AzureStorage):
    account_name = "b0030724dcbs"   
    account_key = "DefaultEndpointsProtocol=https;AccountName=b0030724dcbs;AccountKey=BtbCdiYL2rZWe7sh5w2QoMQtL0Lol5QvQg7AHl6xluLrfvpNPz1CGsR/B8hL5FAsvf2NAnc9qpSE+AStYr5X1Q==;EndpointSuffix=core.windows.net"
    azure_container = "static"
    expiration_secs = None 