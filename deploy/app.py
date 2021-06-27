#!/usr/bin/env python3

from aws_cdk import core

from edith.frontend import FrontendStack
from edith.networking import NetworkingAndDBStack

app = core.App()
FrontendStack(app, "edith-frontend")
NetworkingAndDBStack(app, "edith-networking-db")

app.synth()
