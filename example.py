import clihandler as cli


#p = cli.call(name="pip", cmd="pip install imthread imchrome nitin_raaii")
p = cli.call(name="ping", cmd="ping -n 3 127.0.0.1")

print("execution started")

for i, line in enumerate(cli.capture(p)):
    print(line)

    if line.startswith("Ping statistics"):
        cli.kill(p)

print(cli.return_code(p))
