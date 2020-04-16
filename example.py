import clihandler as cli

p = cli.call(name="ping", cmd="ping -n 10 127.0.0.1")

for i, line in enumerate(cli.capture(p)):
    print(line)
