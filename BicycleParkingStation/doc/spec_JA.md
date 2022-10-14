[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティBicycleParkingStation  
===========================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.OSLO/blob/master/BicycleParkingStation/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**旅客輸送機関のAPスキーマ仕様に準拠した駐輪場スキーマ**。  
バージョン: 0.0.1  

## プロパティ一覧  

- `InfrastructureElement.geometry`: インフラストラクチャ要素に対応するジオメトリ。  - `ParkingFacility.^capacity`: 市民団体としての能力  - `address`: 郵送先住所  - `alternateName`: この項目の別称  - `areaServed`: サービスまたは提供品が提供される地理的な地域  - `dataProvider`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description`: このアイテムの説明  - `id`: エンティティの一意な識別子  - `location`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name`: このアイテムの名称です。  - `owner`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリスト  - `seeAlso`: 項目に関する追加リソースを指すURIのリスト。  - `source`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type`: NGSI Entity タイプ。BicycleParkingStationでなければならない。    
必要なプロパティ  
- `InfrastructureElement.geometry`  - `ParkingFacility.^capacity`  - `id`  - `location`  - `type`  ## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BicycleParkingStation:    
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
    ParkingFacility.^capacity:    
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
      anyOf: &bicycleparkingstation_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *bicycleparkingstation_-_properties_-_owner_-_items_-_anyof    
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
        - BicycleParkingStation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - ParkingFacility.^capacity    
    - InfrastructureElement.geometry    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.OSLO/blob/master/BicycleParkingStation/LICENSE.md    
  x-model-schema: https://github.com/smart-data-models/incubated/dataModel.OSLO.PassengerTransportHubs/raw/master/BicycleParkingStationPTH-AP/schema.json    
  x-model-tags: GreenMov    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### BicycleParkingStation NGSI-v2 key-value の例。  
BicycleParkingStationをJSON-LD形式でkey-valuesにした例である。これは、`options=keyValues`を使用した場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### BicycleParkingStation NGSI-v2 正規化例  
以下は、BicycleParkingStation を JSON-LD 形式で正規化した例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### BicycleParkingStation NGSI-LD key-value Example  
BicycleParkingStationをJSON-LD形式でkey-valuesにした例です。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータが返される。  
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
#### BicycleParkingStation NGSI-LD 正規化例  
BicycleParkingStation を JSON-LD 形式で正規化した例を示す。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
