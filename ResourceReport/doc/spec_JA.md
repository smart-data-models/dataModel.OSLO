<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティです：リソースレポート（ResourceReport  
================================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.OSLO/blob/master/ResourceReport/LICENSE.md)  
[文書が自動的に生成されます](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です：**Resource Report Schema meeting Passenger Transport Hubs AP Schema specification.レポートを要求する人が定義したフィルターに基づき、モビリティサービスに接続されたリソースを要約したもの**。  
バージョン：0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性に型がない場合は、複数の型や異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `ResourceReport.actuator[object]`: 移動手段のエンジン。  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#actuator](https://purl.eu/ns/mobility/passenger-transport-hubs#actuator)- `ResourceReport.location[object]`: リソースの位置。これは、駐輪場であったり、フリーフローティングの部品輸送などにおける車両のリアルタイムの位置であったりする。  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#location](https://purl.eu/ns/mobility/passenger-transport-hubs#location)- `ResourceReport.meansOfTransport[object]`: 本資料の輸送手段の種類。  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#Mobiliteitsdienst.vervoermiddel](https://purl.eu/ns/mobility/passenger-transport-hubs#Mobiliteitsdienst.vervoermiddel)- `ResourceReport.number[number]`: リソースの数です。  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#number](https://purl.eu/ns/mobility/passenger-transport-hubs#number)- `ResourceReport.reportTime[string]`: レポートが有効である時点。  . Model: [http://purl.org/dc/elements/1.1/date](http://purl.org/dc/elements/1.1/date)- `ResourceReport.service[object]`: ResourceReport内で使用されるMobilityService。  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#service](https://purl.eu/ns/mobility/passenger-transport-hubs#service)- `ResourceReport.status[object]`: リソースの状態。例：予約済み、非アクティブ、利用可能。リソースが使用可能かどうかを決定する。  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#status](https://purl.eu/ns/mobility/passenger-transport-hubs#status)- `ResourceReport.type[object]`: リソースの性質  . Model: [http://purl.org/dc/terms/type](http://purl.org/dc/terms/type)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: このアイテムの別称  - `areaServed[string]`: サービスまたは提供されるアイテムが提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `id[*]`: エンティティの一意な識別子  - `location[*]`: アイテムへの Geojson 参照。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon のいずれかである。  - `name[string]`: この項目の名称です。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリストです。  - `seeAlso[*]`: アイテムに関する追加リソースを指す URI のリスト。  - `source[string]`: エンティティデータの元のソースをURLとして与える一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type[string]`: NGSI Entityタイプ。ResourceReportでなければならない。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `ResourceReport.number`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
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
## ペイロードの例  
#### ResourceReport NGSI-v2 キー値例  
ResourceReportをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### ResourceReport NGSI-v2 正規化例  
正規化されたJSON-LD形式のResourceReportの例を示す。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### ResourceReport NGSI-LD キー値例  
ResourceReportをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### ResourceReport NGSI-LD 正規化例  
JSON-LD形式のResourceReportを正規化した例を示します。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
