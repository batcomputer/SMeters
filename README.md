## Smart Energy Meters
API for viewing Energy Meter readings in IIT Delhi from a data acquisition system constructed using a Raspberry Pi on a Nippen EM-34DS Energy Meter.
This Django server was hosted on a Virtual Machine allotted on the cloud.
Meter readings were extracted using minicom and Python on the Pi.
They were sent to the VM in csv format, where they were sorted into a SQL database.
The energy data was served in JSON format and finally viewed as a graph using the HighchartsJS plugin.

### Hardware Requirements
Raspberry Pi 3 and RS485 to USB converter

### Software Requirements
1.Minicom
2.Screen
3.Python 3
4.MySQL
5.Django

### Procedure
1.Check if the port is open for transmitting data in the energy meter. Set id to 485 on the meter's display to allow communication.
2.Install minicom and set Baud Rate to 9600, Databits to 8 ,Stopbits to 1 and Parity to none.

