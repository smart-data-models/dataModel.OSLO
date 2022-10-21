<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: ResourceReport  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.OSLO/blob/master/ResourceReport/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Resource Report Schema meeting Passenger Transport Hubs AP Schema specification. A summary of resources connected to mobility services based on defined filters by the person requesting the report.**  
version: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `ResourceReport.actuator[object]`: Engine of the means of transport.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#actuator](https://purl.eu/ns/mobility/passenger-transport-hubs#actuator)- `ResourceReport.location[object]`: Location of the Resource. This could be a bike parking station or the real-time location of the vehicle, e.g. in free-floating part transport.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#location](https://purl.eu/ns/mobility/passenger-transport-hubs#location)- `ResourceReport.meansOfTransport[object]`: The type of means of transport of the Resource.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#Mobiliteitsdienst.vervoermiddel](https://purl.eu/ns/mobility/passenger-transport-hubs#Mobiliteitsdienst.vervoermiddel)- `ResourceReport.number[integer]`: The number of resources.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#number](https://purl.eu/ns/mobility/passenger-transport-hubs#number)- `ResourceReport.reportTime[string]`: Point in time for which the report is valid.  . Model: [http://purl.org/dc/elements/1.1/date](http://purl.org/dc/elements/1.1/date)- `ResourceReport.service[object]`: The MobilityService used within the ResourceReport.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#service](https://purl.eu/ns/mobility/passenger-transport-hubs#service)- `ResourceReport.status[object]`: State of a Resource. E.g. reserved, inactive, available. Determines whether a resource can be used.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#status](https://purl.eu/ns/mobility/passenger-transport-hubs#status)- `ResourceReport.type[object]`: Nature of the Resource.  . Model: [http://purl.org/dc/terms/type](http://purl.org/dc/terms/type)- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated[string]`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified[string]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item.  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type[string]`: NGSI Entity type. It has to be ResourceReport.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `ResourceReport.number`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ResourceReport:    
  description: 'Resource Report Schema meeting Passenger Transport Hubs AP Schema specification. A summary of resources connected to mobility services based on defined filters by the person requesting the report.'    
  properties:    
    ResourceReport.actuator:    
      description: 'Engine of the means of transport.'    
      properties:    
        ActuatorType.preferredLabel:    
          description: "Property. Model: 'http://www.w3.org/2004/02/skos/core#prefLabel'. Preferred label. Enum:'combustionEngine, electric, electricWithSupport, human'"    
          enum:    
            - combustionEngine    
            - electric    
            - electricWithSupport    
            - human    
          type: string    
        type:    
          enum:    
            - ActuatorType    
          type: string    
      required:    
        - type    
        - ActuatorType.preferredLabel    
      type: object    
      x-ngsi:    
        model: "https://purl.eu/ns/mobility/passenger-transport-hubs#actuator"    
        type: Property    
    ResourceReport.location:    
      description: 'Location of the Resource. This could be a bike parking station or the real-time location of the vehicle, e.g. in free-floating part transport.'    
      properties:    
        object:    
          format: uri    
          type: string    
        type:    
          type: string    
      type: object    
      x-ngsi:    
        model: "https://purl.eu/ns/mobility/passenger-transport-hubs#location"    
        type: Property    
    ResourceReport.meansOfTransport:    
      description: 'The type of means of transport of the Resource.'    
      properties:    
        MeansOfTransport.preferredLabel:    
          description: "Property. Model: 'http://www.w3.org/2004/02/skos/core#prefLabel'. Preferred label. Enum:'airplane, bicycle, boat, bus, car, escalator, lift, motorcycle, onFoot, pedelec, scooter, skateboard, step, subway, train, tram, treadmill, truck'"    
          enum:    
            - airplane    
            - bicycle    
            - boat    
            - bus    
            - car    
            - escalator    
            - lift    
            - motorcycle    
            - onFoot    
            - pedelec    
            - scooter    
            - skateboard    
            - step    
            - subway    
            - train    
            - tram    
            - treadmill    
            - truck    
          type: string    
        type:    
          enum:    
            - MeansOfTransport    
          type: string    
      required:    
        - type    
        - MeansOfTransport.preferredLabel    
      type: object    
      x-ngsi:    
        model: "https://purl.eu/ns/mobility/passenger-transport-hubs#Mobiliteitsdienst.vervoermiddel"    
        type: Property    
    ResourceReport.number:    
      description: 'The number of resources.'    
      type: integer    
      x-ngsi:    
        model: "https://purl.eu/ns/mobility/passenger-transport-hubs#number"    
        type: Property    
    ResourceReport.reportTime:    
      description: 'Point in time for which the report is valid.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/elements/1.1/date    
        type: Property    
    ResourceReport.service:    
      description: 'The MobilityService used within the ResourceReport.'    
      properties:    
        object:    
          format: uri    
          type: string    
        type:    
          type: string    
      type: object    
      x-ngsi:    
        model: "https://purl.eu/ns/mobility/passenger-transport-hubs#service"    
        type: Property    
    ResourceReport.status:    
      description: 'State of a Resource. E.g. reserved, inactive, available. Determines whether a resource can be used.'    
      properties:    
        ResourceStatus.preferredLabel:    
          description: "Property. Model: 'http://www.w3.org/2004/02/skos/core#prefLabel'. Preferred label. Enum:'available, deleted, inactive, inUse, relocated, reserved, unavailable'"    
          enum:    
            - available    
            - deleted    
            - inactive    
            - inUse    
            - relocated    
            - reserved    
            - unavailable    
          type: string    
        type:    
          enum:    
            - ResourceStatus    
          type: string    
      required:    
        - type    
        - ResourceStatus.preferredLabel    
      type: object    
      x-ngsi:    
        model: "https://purl.eu/ns/mobility/passenger-transport-hubs#status"    
        type: Property    
    ResourceReport.type:    
      description: 'Nature of the Resource.'    
      properties:    
        ResourceType.preferredLabel:    
          description: "Property. Model: 'http://www.w3.org/2004/02/skos/core#prefLabel'. Preferred label. Enum:'chargingStation, parkingSpace, room, seating, vehicle'"    
          enum:    
            - chargingStation    
            - parkingSpace    
            - room    
            - seating    
            - vehicle    
          type: string    
        type:    
          enum:    
            - ResourceType    
          type: string    
      required:    
        - type    
        - ResourceType.preferredLabel    
      type: object    
      x-ngsi:    
        model: http://purl.org/dc/terms/type    
        type: Property    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &resourcereport_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *resourcereport_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be ResourceReport.'    
      enum:    
        - ResourceReport    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - ResourceReport.number    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OSLO/blob/master/ResourceReport/LICENSE.md    
  x-model-schema: https://github.com/smart-data-models/dataModel.OSLO/raw/master/ResourceReport/schema.json    
  x-model-tags: GreenMov    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### ResourceReport NGSI-v2 key-values Example    
Here is an example of a ResourceReport in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "http://example.org/resourcereport/1",  
  "type": "ResourceReport",  
  "ResourceReport.actuator": {  
    "type": "ActuatorType",  
    "ActuatorType.preferredLabel": "human"  
  },  
  "ResourceReport.location": "https://blue-bike.be/stations/141",  
  "ResourceReport.meansOfTransport": {  
    "type": "MeansOfTransport",  
    "MeansOfTransport.preferredLabel": "bicycle"  
  },  
  "ResourceReport.number": 5,  
  "ResourceReport.service": "https://blue-bike.be/#me",  
  "ResourceReport.status": {  
    "type": "ResourceStatus",  
    "ResourceStatus.preferredLabel": "available"  
  },  
  "ResourceReport.type": {  
    "type": "ResourceType",  
    "ResourceType.preferredLabel": "vehicle"  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      3.313743000000,  
      50.855703000000  
    ]  
  }  
}  
```  
</details>  
#### ResourceReport NGSI-v2 normalized Example    
Here is an example of a ResourceReport in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "http://example.org/resourcereport/1",  
  "type": "ResourceReport",  
  "ResourceReport.actuator": {  
    "type": "StructuredValue",  
    "value": {  
        "type": "ActuatorType",  
        "ActuatorType.preferredLabel": "human"  
    }  
  },  
  "ResourceReport.location": {  
    "type": "URL",  
    "value": "https://blue-bike.be/stations/141"  
  },  
  "ResourceReport.meansOfTransport": {  
    "type": "StructuredValue",  
    "value": {  
        "type": "MeansOfTransport",  
        "MeansOfTransport.preferredLabel": "bicycle"  
    }  
  },  
  "ResourceReport.number": {  
    "type": "Number",  
    "value": 5  
  },  
  "ResourceReport.service": {  
    "type": "URL",  
    "value": "https://blue-bike.be/#me"  
  },  
  "ResourceReport.status": {  
    "type": "StructuredValue",  
    "value": {  
        "type": "ResourceStatus",  
        "ResourceStatus.preferredLabel": "available"  
    }  
  },  
  "ResourceReport.type": {  
    "type": "StructuredValue",  
    "value": {  
        "type": "ResourceType",  
        "ResourceType.preferredLabel": "vehicle"  
    }  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        3.313743000000,  
        50.855703000000  
      ]  
    }  
  }  
}  
```  
</details>  
#### ResourceReport NGSI-LD key-values Example    
Here is an example of a ResourceReport in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "http://example.org/resourcereport/1",  
    "type": "ResourceReport",  
    "ResourceReport.actuator": {  
        "type": "ActuatorType",  
        "ActuatorType.preferredLabel": "human"  
    },  
    "ResourceReport.location": "https://blue-bike.be/stations/141",  
    "ResourceReport.meansOfTransport": {  
        "type": "MeansOfTransport",  
        "MeansOfTransport.preferredLabel": "bicycle"  
    },  
    "ResourceReport.number": 5,  
    "ResourceReport.service": "https://blue-bike.be/#me",  
    "ResourceReport.status": {  
        "type": "ResourceStatus",  
        "ResourceStatus.preferredLabel": "available"  
    },  
    "ResourceReport.type": {  
        "type": "ResourceType",  
        "ResourceType.preferredLabel": "vehicle"  
    },  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            3.313743,  
            50.855703  
        ]  
    },  
    "@context": [  
        "https://brechtvdv.github.io/incubated/dataModel.OSLO.PassengerTransportHubs/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OSLO/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### ResourceReport NGSI-LD normalized Example    
Here is an example of a ResourceReport in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "http://example.org/resourcereport/1",  
    "type": "ResourceReport",  
    "ResourceReport.actuator": {  
        "type": "Relationship",  
        "object": {  
            "type": "ActuatorType",  
            "ActuatorType.preferredLabel": "human"  
        }  
    },  
    "ResourceReport.location": {  
        "type": "Relationship",  
        "object": "https://blue-bike.be/stations/141"  
    },  
    "ResourceReport.meansOfTransport": {  
        "type": "Relationship",  
        "object": {  
            "type": "MeansOfTransport",  
            "MeansOfTransport.preferredLabel": "bicycle"  
        }  
    },  
    "ResourceReport.number": {  
        "type": "Property",  
        "value": 5  
    },  
    "ResourceReport.service": {  
        "type": "Relationship",  
        "object": "https://blue-bike.be/#me"  
    },  
    "ResourceReport.status": {  
        "type": "Relationship",  
        "object": {  
            "type": "ResourceStatus",  
            "ResourceStatus.preferredLabel": "available"  
        }  
    },  
    "ResourceReport.type": {  
        "type": "Relationship",  
        "object": {  
            "type": "ResourceType",  
            "ResourceType.preferredLabel": "vehicle"  
        }  
    },  
    "location": {  
        "type": "Geoproperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                3.313743,  
                50.855703  
            ]  
        }  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OSLO/master/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
