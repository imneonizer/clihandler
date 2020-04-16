## CLI Handler

Let's face this, there are certain bash scripts, executables or cli commands which are awesome to use but we want them to be a part of our python code.

For example lets say we use ``ping -n 5 127.0.0.1`` this will work great on terminal but if we want to execute this command via python code and want to get it's output simultaneously in real time, than that's a pretty difficult task.

````bash
pip install clihandler
````

And here we go, we can execute commands directly from our python codes.

### Example

````python
import clihandler as cli

p = cli.call(name="ping", cmd="ping -n 10 127.0.0.1")

for line in cli.capture(p):
    print(line)

print(cli.return_code(p))
````

This will execute the command in background and we can iterate over the output via a for loop.

And what's more interesting is while iterating over the output in real-time if we want to interrupt the command execution logically based on output we can do that too.

If the command executed successfully it will give ``return_code = 0``.

```python
.
.
for line in cli.capture(p):
    print(line)
    if line.startswith("Ping statistics"):
    	cli.kill(p)
```

Since we are killing the command execution in between logically, this will give ``return_code = 130``, and incase the command is failed to execute, it will give ``return_code = 1``.

> return codes are stored inside the object as long as no other call is made with the same name
>
> incase you wanna delete all the traces of subprocess call, use: cli.reset(p)

One good thing about clihandler is, if you execute the same call command multiple time with the same name, while previous execution wasn't completed it will not interrupt the previous command execution rather return the same result.

By default ``cli.call(name=<something>, cmd=<something>)`` returns the name of the subprocess but if you want to access the actual subprocess object spawned by python then you can do that using: ``cli.get(<name>)``.

To see all the processes spawned by cli handler which are still running in background: ``cli.list_process()``