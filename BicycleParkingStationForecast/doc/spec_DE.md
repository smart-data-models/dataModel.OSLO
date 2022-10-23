<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: BicycleParkingStationForecast  
======================================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.OSLO/blob/master/BicycleParkingStationForecast/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Fahrradparkplatz-Schema gemäß der Spezifikation für Personenverkehrsknotenpunkte AP-Schema**  
Version: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `InfrastructureElement.geometry[object]`: Die Geometrie, die dem Infrastrukturelement entspricht.  . Model: [http://www.w3.org/ns/locn#geometry](http://www.w3.org/ns/locn#geometry)- `ParkingFacility.capacity[object]`: Kapazität einer zivilen Struktur.  . Model: [http://schema.mobivoc.org/#capacity](http://schema.mobivoc.org/#capacity)- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `type[string]`: NGSI-Entitätstyp. Es muss BicycleParkingStation sein  - `validFrom[string]`: Datum und Uhrzeit des Beginns des Gültigkeitszeitraums.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `validTo[string]`: Datum und Uhrzeit des Endes des Gültigkeitszeitraums.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `validity[string]`: Enthält den Gültigkeitszeitraum für diese Prognose als ISO8601-Zeitintervall. Es können auch zwei getrennte Attribute verwendet werden: GültigVon", "GültigBis".  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### BicycleParkingStationForecast NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen BicycleParkingStationForecast im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### BicycleParkingStationForecast NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen BicycleParkingStationForecast im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### BicycleParkingStationForecast NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen BicycleParkingStationForecast im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
#### BicycleParkingStationForecast NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen BicycleParkingStationForecast im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "https://blue-bike.be/stations/141",  
    "type": "BicycleParkingStation",  
    "ParkingFacility.capacity": {  
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
            3.313743,  
            50.855703  
        ]  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
