# Automatic Package Tracking For DHL 
# How To Use 
First, get an API: This is where the API is, you must make an account, and the Shipment Tracking - Unified API is recommended as it is what was used originally: https://developer.dhl.com/ 
Second, change the code on line 8 to your own API key. 
Finally, run the code, type the tracking numbers and it will retrieve the information. Then when it is done it will either tell you to try some of the numbers manually if they fail. To get the data go to the .csv file. One reason for failure may be due to too many requests to your API. One thing to note is that the base API has a 250 requests per day cap and one at 1 request per 5 seconds. You can request an upgrade in your app to get more requests. 
# Why and When to Use 
This was made to be used when people must track many packages at once. The main use case is for organizations selling items to track and get data on the consumer packages. 
# How It Works 
This simple code will call the DHL API using your API key. Some sections will check for a problem and then wait for the API to cool down due to the capped rate of calls to the API. Once it gets the information it will write to a csv. 
# Documentation 
This is the main Documentation for Shipment Tracking - Unified API that this was based on: https://developer.dhl.com/api-reference/shipment-tracking#get-started-section/
