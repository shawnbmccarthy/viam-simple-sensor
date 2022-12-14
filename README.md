# Viam Simple Sensor
This project shows how to quickly integrate custom sensors into or viam managed 
robots. 

If you need to set up a robot on viam please see the [setup viam](setup_viam.md) readme.

## Installation
```shell
git clone https://github.com/shawnbmccarthy/viam-simple-sensor
cd viam-simple-sensor
./setup_venv.sh
```
This will set up our python virtual environment and install the required packages

## Configure Robots remote resources

The viam server component interface allows us to create custom components which interface 
with the `viam-server` using the viam SDK's. Our example makes use of the [Python SDK](https://python.viam.dev/)
to create custom sensors.



1. log into [app.viam.com](https://app.viam.com)
2. access the robot you configured, and go to the remotes tab

![configure_remotes.png](images%2Fconfigure_remotes.png)

3. give the remote a name, for this example lets use `simple-sensor`, next select `Create Remote`, this will show the next page:

![configure_remotes_2.png](images%2Fconfigure_remotes_2.png)

4. in the `Heading Info` text box enter `localhost:9090`, this is the default binding that [sensor_remotes.py](sensor_remotes.py) is configured for. Now click `Save Config` at the bottom of the page, a confirmation message will appear.

Now that we have created our remote resource, we can start our proces
```shell
# run from viam-simple-sensor
./sensor_remotes.sh -l DEBUG

```
This will start a remote process with `DEBUG` log level. By default, only `WARNING` and above are logged, you should see
the output below:
```shell
2022-12-14 01:08:42,088         INFO    viam.rpc.server (server.py:81)  Serving on localhost:9090   
```

Now go back to [app.viam.com](https://app.viam.com) and select the `Control` tab of your robot and select `Sensors`, 
here we can select `Get All Readings` to see the output

![control_view.png](images%2Fcontrol_view.png)

To see how the code works view: [static_sensor.py](sample_sensors%2Fstatic_sensor.py) and [sensor_remotes.py](sensor_remotes.py)

### script usage
Below are the options that can be used 

```shell
./sensor_remotes.sh -h
usage: sensor_remotes.py [-h] [--host HOST] [--port PORT] [--log {DEBUG,INFO,WARNING,ERROR,FATAL}]

options:
  -h, --help            show this help message and exit
  --host HOST, -n HOST  hostname/ip rpc server will bind to
  --port PORT, -p PORT  port number to store
  --log {DEBUG,INFO,WARNING,ERROR,FATAL}, -l {DEBUG,INFO,WARNING,ERROR,FATAL}
                        log level to use

```
With no options the defaults are:
* host = localhost 
* port = 9090
* log = WARNING

## Further activities
We can also configure our viam server to manage the remote process, ensuring that when viam server is running the remote server
will also run. 

# contact

For any questions, please email me at: [shawn@viam.com](mailto:shawn@viam.com)

# References
1. [viam](https://viam.com)
1. [viam cloud](https://app.viam.com)
1. [viam docs](https://docs.viam.com)
1. [viam python sdk](https://python.viam.dev)
1. [sdk as server](https://docs.viam.com/product-overviews/sdk-as-server/)
1. [subclassing components](https://python.viam.dev/examples/example.html#subclass-a-component)
1. [drive a rover](https://www.viam.com/resources/try-viam)

