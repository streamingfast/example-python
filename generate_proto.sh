#!/bin/bash
# Copyright 2021 dfuse Platform Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Protobuf definitions
PROTO=${1:-"$ROOT/proto"}

function main() {
  checks

  set -e
  cd "$ROOT" &> /dev/null

  echo "Generating Protobuf bindings via 'buf'"
  buf generate buf.build/streamingfast/firehose
  buf generate buf.build/streamingfast/firehose-ethereum

  echo "Done"
}

function checks() {
  result=`buf --version 2>&1 | grep -Eo 1\.[1-2][0-9\.]+`
  if [[ "$result" == "" ]]; then
    echo "Your version of 'buf' (at `which buf`) is not recent enough. To fix your problem, "
    echo "update 'buf' CLI to latest version:"
    echo ""
    echo "  https://buf.build/docs/installation"
    echo ""
    echo "If everything is working as expected, the command:"
    echo ""
    echo "  buf --version"
    echo ""
    echo "Should print 'v1.18.0'"
    exit 1
  fi
}

main "$@"
