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

# References
1. [viam](https://viam.com)
1. [viam cloud](https://app.viam.com)
1. [viam docs](https://docs.viam.com)
1. [viam python sdk](https://python.viam.dev)
1. [sdk as server](https://docs.viam.com/product-overviews/sdk-as-server/)
1. [subclassing components](https://python.viam.dev/examples/example.html#subclass-a-component)
1. [drive a rover](https://www.viam.com/resources/try-viam)

