## StreamingFast Python Example

This simple program demonstrates how easy it is to stream full block details using StreamingFast gRPC
API:

* Request a token from our authentication API
* Creates a gRPC connection with credentials
* Instantiates a BlockStream client
* Start a stream of blocks
* Prints the blocks received

### Requirements

You will need to have Python3 (>= 3.5+) as well as `virtualenv` and `pip`
`>= 15.0+`.

We use a virtual environment for this example, all dependencies are listed
in the `requirements.txt` at the root of this project.

#### Quickstart

First of all, visit [https://streamingfast.io/](https://streamingfast.io/) to get
a free API key for your project.

First, clone this repository to your work folder:

```bash
git clone https://github.com/streamingfast/example-python.git
cd example-python
```

Setup the virtual environment and pull all dependencies:

```bash
./install_deps.sh
```

Once your environment is setup properly, set up your environment:

```bash
source env/bin/activate
```

Simply run the `main.py` script:

```bash
python3 main.py YOUR_API_KEY_HERE
```

By default it prints light details about the blocks, use the `--full` flag to
print the full block in JSON:

```bash
python3 main.py YOUR_API_KEY_HERE --full
```

**Note** The default Protobuf to JSON will prints the various `bytes` type using `base64` encoding, this is unfortunate as it makes reading it in the JSON harder. If you find a quick option to print it as hexadecimal, open a PR we will be happy to merge it in.

Further details about StreamingFast capabilities can be found on our Golang client at https://github.com/streamingfast/streamingfast-client#query-language.

##### Protobuf

The protocol buffers are already generated, the `generate_proto.sh` is able to regenerate them if needed, it showcases also the command the can be used to generate them back.

The script expects by default that the proto definitions are sibling of this project, looking like:

```
projects
├── example-python
├── proto
└── proto-ethereum
```

To re-generate, simply do:

```bash
./generate_proto.sh
```
