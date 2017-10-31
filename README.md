# Smart Energy Meters
API for viewing Energy Meter readings in IIT Delhi from an automatic data acquisition system constructed using a Raspberry Pi.
This Django server was hosted on a Virtual Machine allotted on the cloud.
Meter readings were extracted using minicom and Python.
They were sent to the VM in csv format, where they were sorted into a SQL database.
The energy data was then served in JSON format and finally viewed as a graph using HighchartsJS plugin.
Here is the code

