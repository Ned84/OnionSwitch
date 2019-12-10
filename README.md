# OnionSwitch

Interface to easily change the Tor Exit node Destination.

    StrictNodes 0|1

    If StrictNodes is set to 1, Tor will treat the ExcludeNodes option as a requirement to follow for all the circuits you generate, even if doing so will break functionality for you. If StrictNodes is set to 0, Tor will still try to avoid nodes in the ExcludeNodes list, but it will err on the side of avoiding unexpected errors. Specifically, StrictNodes 0 tells Tor that it is okay to use an excluded node when it is necessary to perform relay reachability self-tests, connect to a hidden service, provide a hidden service to a client, fulfill a .exit request, upload directory information, or download directory information. (Default: 0)
