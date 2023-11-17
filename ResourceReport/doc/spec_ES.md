<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: ResourceReport    
=======================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.OSLO/blob/master/ResourceReport/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Especificación del esquema del informe de recursos que cumple la especificación del esquema AP de los centros de transporte de pasajeros. Un resumen de los recursos conectados a los servicios de movilidad basado en filtros definidos por la persona que solicita el informe.**    
versión: 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `ResourceReport.actuator[object]`: Motor del medio de transporte  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#actuator](https://purl.eu/ns/mobility/passenger-transport-hubs#actuator)	- `ActuatorType.preferredLabel[string]`: Etiqueta preferida. Enum:'combustionEngine, electric, electricWithSupport, human'  . Model: [ http://www.w3.org/2004/02/skos/core#prefLabel]( http://www.w3.org/2004/02/skos/core#prefLabel)    
- `ResourceReport.location[object]`: Ubicación del recurso. Puede tratarse de una estación de aparcamiento de bicicletas o de la ubicación en tiempo real del vehículo, por ejemplo, en el transporte de piezas flotantes.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#location](https://purl.eu/ns/mobility/passenger-transport-hubs#location)	- `object`:       
- `ResourceReport.meansOfTransport[object]`: El tipo de medio de transporte del Recurso  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#Mobiliteitsdienst.vervoermiddel](https://purl.eu/ns/mobility/passenger-transport-hubs#Mobiliteitsdienst.vervoermiddel)	- `MeansOfTransport.preferredLabel[string]`: Etiqueta preferida. Enum:'avión, bicicleta, barco, autobús, coche, escalera mecánica, ascensor, motocicleta, onFoot, pedelec, scooter, monopatín, step, metro, tren, tranvía, cinta de correr, camión'  . Model: [ http://www.w3.org/2004/02/skos/core#prefLabel]( http://www.w3.org/2004/02/skos/core#prefLabel)    
- `ResourceReport.number[number]`: El número de recursos  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#number](https://purl.eu/ns/mobility/passenger-transport-hubs#number)- `ResourceReport.reportTime[date-time]`: Momento para el que es válido el informe  . Model: [http://purl.org/dc/elements/1.1/date](http://purl.org/dc/elements/1.1/date)- `ResourceReport.service[object]`: El MobilityService utilizado en el ResourceReport  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#service](https://purl.eu/ns/mobility/passenger-transport-hubs#service)	- `object`:       
- `ResourceReport.status[object]`: Estado de un recurso. Por ejemplo, reservado, inactivo, disponible. Determina si un recurso puede utilizarse  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#status](https://purl.eu/ns/mobility/passenger-transport-hubs#status)	- `ResourceStatus.preferredLabel[string]`: Etiqueta preferida. Enum:'disponible, eliminado, inactivo, enUso, reubicado, reservado, no disponible'  . Model: [ http://www.w3.org/2004/02/skos/core#prefLabel]( http://www.w3.org/2004/02/skos/core#prefLabel)    
- `ResourceReport.type[object]`: Naturaleza del recurso  . Model: [http://purl.org/dc/terms/type](http://purl.org/dc/terms/type)	- `ResourceType.preferredLabel[string]`: Etiqueta preferida. Enum:'chargingStation, parkingSpace, room, seating, vehicle'  . Model: [ http://www.w3.org/2004/02/skos/core#prefLabel]( http://www.w3.org/2004/02/skos/core#prefLabel)    
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local      
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Tipo de entidad NGSI. Tiene que ser ResourceReport  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `ResourceReport.number`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
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
## Ejemplo de carga útil    
#### ResourceReport NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de un ResourceReport en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
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
      3.313743,  
      50.855703  
    ]  
  }  
}  
```  
</details>    
#### ResourceReport NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de un ResourceReport en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "ResourceReport.actuator": {  
    "type": "StructuredValue",  
    "value": {  
      "ActuatorType.preferredLabel": "human",  
      "type": "ActuatorType"  
    }  
  },  
  "ResourceReport.location": {  
    "type": "StructuredValue",  
    "value": {  
      "object": "https://blue-bike.be/stations/141"  
    }  
  },  
  "ResourceReport.meansOfTransport": {  
    "type": "StructuredValue",  
    "value": {  
      "MeansOfTransport.preferredLabel": "bicycle",  
      "type": "MeansOfTransport"  
    }  
  },  
  "ResourceReport.number": {  
    "type": "Number",  
    "value": 5  
  },  
  "ResourceReport.service": {  
    "type": "StructuredValue",  
    "value": {  
      "object": "https://blue-bike.be/#me"  
    }  
  },  
  "ResourceReport.status": {  
    "type": "StructuredValue",  
    "value": {  
      "ResourceStatus.preferredLabel": "available",  
      "type": "ResourceStatus"  
    }  
  },  
  "ResourceReport.type": {  
    "type": "StructuredValue",  
    "value": {  
      "ResourceType.preferredLabel": "vehicle",  
      "type": "ResourceType"  
    }  
  },  
  "id": "http://example.org/resourcereport/1",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "coordinates": [  
        3.313743,  
        50.855703  
      ],  
      "type": "Point"  
    }  
  },  
  "type": "ResourceReport"  
}  
```  
</details>    
#### ResourceReport NGSI-LD key-values Ejemplo    
He aquí un ejemplo de un ResourceReport en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
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
      3.313743,  
      50.855703  
    ]  
  },  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.OSLO/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### ResourceReport NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de un ResourceReport en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
