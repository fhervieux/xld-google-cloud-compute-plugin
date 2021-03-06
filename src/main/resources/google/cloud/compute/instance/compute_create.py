#
# Copyright 2018 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from org.jclouds.googlecomputeengine.domain import JCloudGoogleCompute

print("Connecting to google cloud with {0} email".format(deployed.container.clientEmail))
googleCompute = JCloudGoogleCompute(deployed.container.clientEmail, deployed.container.privateKey)

machine = deployed.machine
zone = deployed.zone
image = deployed.image
imageProject = deployed.imageProject
network = deployed.network
subnetwork = deployed.subnetwork
externalAddress = deployed.externalAddress
metadata = deployed.metadata
serviceAccount = deployed.serviceAccount
accessScopes = deployed.accessScopes

instanceName = deployed.instanceName if deployed.instanceName else deployed.name

print("Create new instance {} ...".format(instanceName))
operationSelfLink = googleCompute.createInstance(instanceName, image, imageProject, machine, zone, network, subnetwork, externalAddress, metadata, serviceAccount, accessScopes)
deployed.operationSelfLink = operationSelfLink
