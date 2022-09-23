[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: BicycleParkingStationForecast  
======================================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.OSLO/blob/master/BicycleParkingStationForecast/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Esquema de la estación de estacionamiento de bicicletas que cumple con la especificación del esquema de los centros de transporte de pasajeros**  
versión: 0.1.0  

## Lista de propiedades  

- `InfrastructureElement.geometry`: La geometría correspondiente al elemento de la infraestructura.  - `ParkingFacility.capacity`: Capacidad de una estructura cívica.  - `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type`: Tipo de entidad NGSI. Debe ser BicycleParkingStation  - `validFrom`: Fecha y hora de inicio del periodo de validez.  - `validTo`: Fecha y hora de finalización del periodo de validez.  - `validity`: Incluye el periodo de validez de esta previsión como un intervalo de tiempo ISO8601. También se pueden utilizar dos atributos distintos: `validFrom`, `validTo`.    
Propiedades requeridas  
- `id`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BicycleParkingStationForecast:    
  description: 'Bicycle Parking Station Schema meeting Passenger Transport Hubs AP Schema specification'    
  properties:    
    InfrastructureElement.geometry:    
      description: 'The geometry corresponding to the infrastructure element.'    
      properties:    
        Geometry.wkt:    
          description: "Property. Model:'http://www.opengis.net/ont/geosparql#asWKT'. Geometry expressed in wkt format."    
          properties: {}    
          type: string    
        type:    
          description: "Property. Model: 'http://www.w3.org/ns/locn#Geometry'"    
          enum:    
            - Geometry    
          type: string    
      required:    
        - type    
        - Geometry.wkt    
      type: object    
      x-ngsi:    
        model: "http://www.w3.org/ns/locn#geometry"    
        type: Property    
    ParkingFacility.capacity:    
      description: 'Capacity of a civic structure. '    
      properties:    
        Capacity.total:    
          description: "Property. Model: 'http://schema.mobivoc.org/#totalCapacity'. Indicates the capacity of a resource."    
          type: number    
        type:    
          enum:    
            - Capacity    
          type: string    
      required:    
        - type    
        - Capacity.total    
      type: object    
      x-ngsi:    
        model: "http://schema.mobivoc.org/#capacity"    
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
      anyOf: &bicycleparkingstationforecast_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *bicycleparkingstationforecast_-_properties_-_owner_-_items_-_anyof    
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
      description: 'NGSI Entity type. It has to be BicycleParkingStation'    
      enum:    
        - BicycleParkingStationForecast    
      type: string    
      x-ngsi:    
        type: Property    
    validFrom:    
      description: 'Validity period start date and time.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    validTo:    
      description: 'Validity period end date and time.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    validity:    
      description: 'Includes the validity period for this forecast as a ISO8601 time interval. It can be also used two separate attributes: `validFrom`, `validTo`.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OSLO/blob/master/BicycleParkingStationForecast/LICENSE.md    
  x-model-schema: https://github.com/smart-data-models/dataModel.OSLO/raw/master/BicycleParkingStationForecast/schema.json    
  x-model-tags: GreenMov    
  x-version: 0.1.0    
```  
</details>    
## Ejemplo de carga útil  
#### BicycleParkingStationForecast NGSI-v2 key-values Ejemplo  
A continuación se muestra un ejemplo de BicycleParkingStationForecast en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "https://blue-bike.be/stations/141",  
  "type": "BicycleParkingStation",  
  "ParkingFacility.^capacity": {  
    "type": "Capacity",  
    "Capacity.total": 20  
  },  
  "InfrastructureElement.geometry": {  
    "type": "Geometry",  
    "Geometry.wkt": "POINT(3.313743000000 50.855703000000)"  
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
#### BicycleParkingStationForecast NGSI-v2 normalizado Ejemplo  
A continuación se muestra un ejemplo de BicycleParkingStationForecast en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "https://blue-bike.be/stations/141",  
  "type": "BicycleParkingStation",  
  "ParkingFacility.^capacity": {  
    "type": "StructuredValue",  
    "value": {  
      "type": "Capacity",  
      "Capacity.total": {  
        "type": "Number",  
        "value": 20  
      }  
    }  
  },  
  "InfrastructureElement.geometry": {  
    "type": "StructuredValue",  
    "value": {  
      "type": "Geometry",  
      "Geometry.wkt": {  
        "type": "Property",  
        "value": "POINT(3.313743000000 50.855703000000)"  
      }  
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
#### BicycleParkingStationForecast NGSI-LD key-values Ejemplo  
A continuación se muestra un ejemplo de BicycleParkingStationForecast en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "https://blue-bike.be/stations/141",  
  "type": "BicycleParkingStation",  
  "ParkingFacility.^capacity": {  
    "type": "Capacity",  
    "Capacity.total": 20  
  },  
  "InfrastructureElement.geometry": {  
    "type": "Geometry",  
    "Geometry.wkt": "POINT(3.313743000000 50.855703000000)"  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      3.313743000000,  
      50.855703000000  
    ]  
  },  
  "@context": [  
    "https://brechtvdv.github.io/incubated/dataModel.OSLO.PassengerTransportHubs/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### BicycleParkingStationForecast NGSI-LD normalizado Ejemplo  
A continuación se muestra un ejemplo de BicycleParkingStationForecast en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "https://blue-bike.be/stations/141",  
  "type": "BicycleParkingStation",  
  "ParkingFacility.^capacity": {  
    "type": "Relationship",  
    "object": {  
      "type": "Capacity",  
      "Capacity.total": {  
        "type": "Property",  
        "value": 20  
      }  
    }  
  },  
  "InfrastructureElement.geometry": {  
    "type": "Relationship",  
    "object": {  
      "type": "Geometry",  
      "Geometry.wkt": {  
        "type": "Property",  
        "value": "POINT(3.313743000000 50.855703000000)"  
      }  
    }  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      3.313743000000,  
      50.855703000000  
    ]  
  },  
  "@context": [  
    "https://brechtvdv.github.io/incubated/dataModel.OSLO.PassengerTransportHubs/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
