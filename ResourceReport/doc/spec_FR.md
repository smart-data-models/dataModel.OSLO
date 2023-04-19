<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Rapport sur les ressources  
===================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.OSLO/blob/master/ResourceReport/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Resource Report Schema meeting Passenger Transport Hubs AP Schema specification. Un résumé des ressources connectées aux services de mobilité sur la base de filtres définis par la personne qui demande le rapport**.  
version : 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `ResourceReport.actuator[object]`: Moteur du moyen de transport.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#actuator](https://purl.eu/ns/mobility/passenger-transport-hubs#actuator)- `ResourceReport.location[object]`: Emplacement de la ressource. Il peut s'agir d'une station de stationnement pour vélos ou de la localisation en temps réel du véhicule, par exemple dans le cas d'un transport de pièces en free-floating.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#location](https://purl.eu/ns/mobility/passenger-transport-hubs#location)- `ResourceReport.meansOfTransport[object]`: Le type de moyen de transport de la ressource.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#Mobiliteitsdienst.vervoermiddel](https://purl.eu/ns/mobility/passenger-transport-hubs#Mobiliteitsdienst.vervoermiddel)- `ResourceReport.number[number]`: Le nombre de ressources.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#number](https://purl.eu/ns/mobility/passenger-transport-hubs#number)- `ResourceReport.reportTime[string]`: Point dans le temps pour lequel le rapport est valide.  . Model: [http://purl.org/dc/elements/1.1/date](http://purl.org/dc/elements/1.1/date)- `ResourceReport.service[object]`: Le MobilityService utilisé dans le ResourceReport.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#service](https://purl.eu/ns/mobility/passenger-transport-hubs#service)- `ResourceReport.status[object]`: État d'une ressource. Par exemple, réservée, inactive, disponible. Détermine si une ressource peut être utilisée.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#status](https://purl.eu/ns/mobility/passenger-transport-hubs#status)- `ResourceReport.type[object]`: Nature de la ressource.  . Model: [http://purl.org/dc/terms/type](http://purl.org/dc/terms/type)- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Date de création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage.  - `dateModified[string]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage.  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type d'entité NGSI. Il doit s'agir de ResourceReport.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `ResourceReport.number`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ResourceReport:    
  description: Resource Report Schema meeting Passenger Transport Hubs AP Schema specification. A summary of resources connected to mobility services based on defined filters by the person requesting the report.    
  properties:    
    ResourceReport.actuator:    
      description: "Property. Model:'https://purl.eu/ns/mobility/passenger-transport-hubs#actuator'. Engine of the means of transport."    
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
      description: "Property. Model:'https://purl.eu/ns/mobility/passenger-transport-hubs#location'. Location of the Resource. This could be a bike parking station or the real-time location of the vehicle, e.g. in free-floating part transport."    
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
      description: "Property. Model:'https://purl.eu/ns/mobility/passenger-transport-hubs#Mobiliteitsdienst.vervoermiddel'. The type of means of transport of the Resource."    
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
      description: "Property. Model:'https://purl.eu/ns/mobility/passenger-transport-hubs#number'. The number of resources."    
      type: number    
      x-ngsi:    
        model: "https://purl.eu/ns/mobility/passenger-transport-hubs#number"    
        type: Property    
    ResourceReport.reportTime:    
      description: 'Property. Model:''http://purl.org/dc/elements/1.1/date''. Point in time for which the report is valid.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://purl.org/dc/elements/1.1/date    
        type: Property    
    ResourceReport.service:    
      description: "Property. Model:'https://purl.eu/ns/mobility/passenger-transport-hubs#service'. The MobilityService used within the ResourceReport."    
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
      description: "Property. Model:'https://purl.eu/ns/mobility/passenger-transport-hubs#status'. State of a Resource. E.g. reserved, inactive, available. Determines whether a resource can be used."    
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
      description: 'Property. Model:''http://purl.org/dc/terms/type''. Nature of the Resource.'    
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
      description: The mailing address    
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
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
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
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
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
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
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
      anyOf: &resourcereport_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
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
        - description: GeoProperty. Geojson reference to the item. LineString    
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
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *resourcereport_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. NGSI Entity type. It has to be ResourceReport.    
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
## Exemples de charges utiles  
#### ResourceReport Valeurs clés de l'INS-v2 Exemple  
Voici un exemple de ResourceReport au format JSON-LD en tant que valeurs clés. Il est compatible avec la NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
      3.313743000000,  
      50.855703000000  
    ]  
  }  
}  
```  
</details>  
#### ResourceReport NGSI-v2 normalisé Exemple  
Voici un exemple de ResourceReport au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### ResourceReport Valeurs clés NGSI-LD Exemple  
Voici un exemple de ResourceReport au format JSON-LD en tant que valeurs clés. Ce format est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### ResourceReport NGSI-LD normalisé Exemple  
Voici un exemple de ResourceReport au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
