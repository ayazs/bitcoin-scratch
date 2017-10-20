from bitcoin.rpc import RawProxy

# Create a connection to a Bitcoin Core node
p = RawProxy()

# Run getinfo command
info = p.getinfo()

# Retrieve the blocks element
print(info['blocks'])
