# Shared

The contents of this package is to help create and distribute shared code between the server, client, and external test tools. Most importantly, it is where the packet definitions live.

The shared packet definitions live in `packets.proto`. Once edited, you should run the `generate_packets.py` file to generate the code needed to use these packets and copy them to the right places.