<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

============
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `ResourceReport.actuator[object]`: 운송 수단의 엔진  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#actuator](https://purl.eu/ns/mobility/passenger-transport-hubs#actuator)
	- `type`:     
- `ResourceReport.location[object]`: 리소스의 위치. 자전거 주차 스테이션 또는 차량의 실시간 위치(예: 자유 유동 부품 운송)일 수 있습니다.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#location](https://purl.eu/ns/mobility/passenger-transport-hubs#location)
	- `type`:     
- `ResourceReport.meansOfTransport[object]`: 리소스의 운송 수단 유형  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#Mobiliteitsdienst.vervoermiddel](https://purl.eu/ns/mobility/passenger-transport-hubs#Mobiliteitsdienst.vervoermiddel)
	- `type`:     
- `ResourceReport.number[number]`: 리소스 수  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#number](https://purl.eu/ns/mobility/passenger-transport-hubs#number)
	- `type`:     
- `ResourceReport.status[object]`: 리소스 상태. 예: 예약됨, 비활성, 사용 가능. 리소스를 사용할 수 있는지 여부를 결정합니다.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#status](https://purl.eu/ns/mobility/passenger-transport-hubs#status)
	- `type`:     
- `ResourceReport.type[object]`: 리소스의 특성  . Model: [http://purl.org/dc/terms/type](http://purl.org/dc/terms/type)
	- `type`:     
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  
<!-- 35-RequiredProperties -->

- `ResourceReport.number`  
<!-- 40-RequiredProperties -->
<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

ResourceReport:    
  description: Resource Report Schema meeting Passenger Transport Hubs AP Schema specification. A summary of resources connected to mobility services based on defined filters by the person requesting the report.    
  properties:    
    ResourceReport.actuator:    
      description: Engine of the means of transport    
      properties:    
        ActuatorType.preferredLabel:    
          description: 'Preferred label. Enum:''combustionEngine, electric, electricWithSupport, human'''    
          enum:    
            - combustionEngine    
            - electric    
            - electricWithSupport    
            - human    
          type: string    
          x-ngsi:    
            model: " http://www.w3.org/2004/02/skos/core#prefLabel"    
            type: Property    
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
      description: 'Location of the Resource. This could be a bike parking station or the real-time location of the vehicle, e.g. in free-floating part transport'    
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
      description: The type of means of transport of the Resource    
      properties:    
        MeansOfTransport.preferredLabel:    
          description: 'Preferred label. Enum:''airplane, bicycle, boat, bus, car, escalator, lift, motorcycle, onFoot, pedelec, scooter, skateboard, step, subway, train, tram, treadmill, truck'''    
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
          x-ngsi:    
            model: " http://www.w3.org/2004/02/skos/core#prefLabel"    
            type: Property    
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
      description: The number of resources    
      type: number    
      x-ngsi:    
        model: "https://purl.eu/ns/mobility/passenger-transport-hubs#number"    
        type: Property    
    ResourceReport.reportTime:    
      description: Point in time for which the report is valid    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/elements/1.1/date    
        type: Property    
    ResourceReport.service:    
      description: The MobilityService used within the ResourceReport    
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
      description: 'State of a Resource. E.g. reserved, inactive, available. Determines whether a resource can be used'    
      properties:    
        ResourceStatus.preferredLabel:    
          description: 'Preferred label. Enum:''available, deleted, inactive, inUse, relocated, reserved, unavailable'''    
          enum:    
            - available    
            - deleted    
            - inactive    
            - inUse    
            - relocated    
            - reserved    
            - unavailable    
          type: string    
          x-ngsi:    
            model: " http://www.w3.org/2004/02/skos/core#prefLabel"    
            type: Property    
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
      description: Nature of the Resource    
      properties:    
        ResourceType.preferredLabel:    
          description: 'Preferred label. Enum:''chargingStation, parkingSpace, room, seating, vehicle'''    
          enum:    
            - chargingStation    
            - parkingSpace    
            - room    
            - seating    
            - vehicle    
          type: string    
          x-ngsi:    
            model: " http://www.w3.org/2004/02/skos/core#prefLabel"    
            type: Property    
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
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be ResourceReport    
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



<details><summary><strong>show/hide example</strong></summary>    


  "id": "http://example.org/resourcereport/1",  
  "type": "ResourceReport",  
  "ResourceReport.actuator": {  
    "type": "ActuatorType",  
    "ActuatorType.preferredLabel": "human"  
  },  
  "ResourceReport.location": {  
    "object": "https://blue-bike.be/stations/141"  
  },  
  "ResourceReport.meansOfTransport": {  
    "type": "MeansOfTransport",  
    "MeansOfTransport.preferredLabel": "bicycle"  
  },  
  "ResourceReport.number": 5,  
  "ResourceReport.service": {  
    "object": "https://blue-bike.be/#me"  
  },  
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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


  "id": "http://example.org/resourcereport/1",  
  "type": "ResourceReport",  
  "ResourceReport.actuator": {  
    "type": "ActuatorType",  
    "ActuatorType.preferredLabel": "human"  
  },  
  "ResourceReport.location": {  
    "object": "https://blue-bike.be/stations/141"  
  },  
  "ResourceReport.meansOfTransport": {  
    "type": "MeansOfTransport",  
    "MeansOfTransport.preferredLabel": "bicycle"  
  },  
  "ResourceReport.number": 5,  
  "ResourceReport.service": {  
    "object": "https://blue-bike.be/#me"  
  },  
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
  },  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.OSLO/master/context.jsonld"  
  ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "http://example.org/resourcereport/1",  
    "type": "ResourceReport",  
    "ResourceReport.actuator": {  
        "type": "Property",  
        "value": {  
            "type": "ActuatorType",  
            "ActuatorType.preferredLabel": "human"  
        }  
    },  
    "ResourceReport.location": {  
        "type": "Property",  
        "value": "https://blue-bike.be/stations/141"  
    },  
    "ResourceReport.meansOfTransport": {  
        "type": "Property",  
        "value": {  
            "type": "MeansOfTransport",  
            "MeansOfTransport.preferredLabel": "bicycle"  
        }  
    },  
    "ResourceReport.number": {  
        "type": "Property",  
        "value": 5  
    },  
    "ResourceReport.service": {  
        "type": "Property",  
        "value": "https://blue-bike.be/#me"  
    },  
    "ResourceReport.status": {  
        "type": "Property",  
        "value": {  
            "type": "ResourceStatus",  
            "ResourceStatus.preferredLabel": "available"  
        }  
    },  
    "ResourceReport.type": {  
        "type": "Property",  
        "value": {  
            "type": "ResourceType",  
            "ResourceType.preferredLabel": "vehicle"  
        }  
    },  
    "location": {  
        "type": "GeoProperty",  
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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
