__author__ = 'cromox'

import requests


url1 = "https://app.swaggerhub.com/apis/cromox"

#req = requests.get(url1)
#
#print(req.headers)
# print(req.content)
# username rosli / org cromox / pswd (international-il)

cuba1url = "https://virtserver.swaggerhub.com/cromox/cuba1/1.0.0"

#req1 = requests.get(cuba1url)
#
#print(req1.headers)
# print(req1.content)

req2 = requests.get(cuba1url + "/inventory")

print(req2.headers)
# print(req2.content)
print(req2.json())

#
#'''
#swagger: '2.0'
#info:
#  description: This is a simple API
#  version: 1.0.0
#  title: Simple Inventory API
#  # put the contact info for your development or API team
#  contact:
#    email: you@your-company.com
#
#  license:
#    name: Apache 2.0
#    url: http://www.apache.org/licenses/LICENSE-2.0.html
#
## tags are used for organizing operations
#tags:
#- name: admins
#  description: Secured Admin-only calls
#- name: developers
#  description: Operations available to regular developers
#
#paths:
#  /inventory:
#    get:
#      tags:
#      - developers
#      summary: searches inventory
#      operationId: searchInventory
#      description: |
#        By passing in the appropriate options, you can search for
#        available inventory in the system
#      produces:
#      - application/json
#      parameters:
#      - in: query
#        name: searchString
#        description: pass an optional search string for looking up inventory
#        required: false
#        type: string
#      - in: query
#        name: skip
#        description: number of records to skip for pagination
#        type: integer
#        format: int32
#        minimum: 0
#      - in: query
#        name: limit
#        description: maximum number of records to return
#        type: integer
#        format: int32
#        minimum: 0
#        maximum: 50
#      responses:
#        200:
#          description: search results matching criteria
#          schema:
#            type: array
#            items:
#              $ref: '#/definitions/InventoryItem'
#        400:
#          description: bad input parameter
#    post:
#      tags:
#      - admins
#      summary: adds an inventory item
#      operationId: addInventory
#      description: Adds an item to the system
#      consumes:
#      - application/json
#      produces:
#      - application/json
#      parameters:
#      - in: body
#        name: inventoryItem
#        description: Inventory item to add
#        schema:
#          $ref: '#/definitions/InventoryItem'
#      responses:
#        201:
#          description: item created
#        400:
#          description: invalid input, object invalid
#        409:
#          description: an existing item already exists
#definitions:
#  InventoryItem:
#    type: object
#    required:
#    - id
#    - name
#    - manufacturer
#    - releaseDate
#    properties:
#      id:
#        type: string
#        format: uuid
#        example: d290f1ee-6c54-4b01-90e6-d701748f0851
#      name:
#        type: string
#        example: Widget Adapter
#      releaseDate:
#        type: string
#        format: int32
#        example: 2016-08-29T09:12:33.001Z
#      manufacturer:
#        $ref: '#/definitions/Manufacturer'
#  Manufacturer:
#    required:
#    - name
#    properties:
#      name:
#        type: string
#        example: ACME Corporation
#      homePage:
#        type: string
#        format: url
#        example:  https://www.acme-corp.com
#      phone:
#        type: string
#        example: 408-867-5309
## Added by API Auto Mocking Plugin
#host: virtserver.swaggerhub.com
#basePath: /cromox/cuba1/1.0.0
#schemes:
# - https
# '''
#
#inventorypostbody = '{  \
#  "id": "d290f1ee-6c54-4b01-90e6-d701748f0851",  \
#  "name": "Widget Adapter",  \
#  "releaseDate": {},  \
#  "manufacturer": {   \
#    "name": "ACME Corporation",   \
#    "homePage": "https://www.acme-corp.com",   \
#    "phone": "408-867-5309"  \
#  }   \
#}'
## content-type = application/json
#
#print(inventorypostbody)

# curl -X POST "https://virtserver.swaggerhub.com/cromox/cuba1/1.0.0/inventory"
# -H "accept: application/json" -H "Content-Type: application/json"
# -d "{ \"id\": \"c290f1aa-6c54-4b01-90c6-b701748c0851\", \"name\": \"Widget Adapter\", \"manufacturer\": { \"name\": \"CROMOX Corporation\", \"homePage\": \"https://www.cromox.co.uk\", \"phone\": \"07777111666\" } }"

# CLI bash
#
# curl -k -v
# -H "Content-Type: application/json"
# -H "accept: application/json"
# -X POST https://virtserver.swaggerhub.com/cromox/cuba1/1.0.0/inventory
# -T tmppost1.json

#$ jq . tmppost1.json
#{
#  "id": "c290f1aa-6c54-4b01-90c6-b701748c0851",
#  "name": "Widget Adapter",
#  "releaseDate": {},
#  "manufacturer": {
#    "name": "CROMOX Corporation",
#    "homePage": "https://www.cromox.co.uk",
#    "phone": "07777111666"
#  }
#}



