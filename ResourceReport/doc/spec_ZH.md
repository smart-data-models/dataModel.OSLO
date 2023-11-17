<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：资源报告    
=======<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.OSLO/blob/master/ResourceReport/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：符合客运枢纽 AP 模式规范的**资源报告模式。根据报告请求人定义的筛选条件，对与移动服务连接的资源进行汇总。    
版本： 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `ResourceReport.actuator[object]`: 运输工具的发动机  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#actuator](https://purl.eu/ns/mobility/passenger-transport-hubs#actuator)	- `ActuatorType.preferredLabel[string]`: 首选标签。枚举：'内燃机、电动、带支持的电动、人类'。  . Model: [ http://www.w3.org/2004/02/skos/core#prefLabel]( http://www.w3.org/2004/02/skos/core#prefLabel)    
- `ResourceReport.location[object]`: 资源位置。这可以是一个自行车停放站，也可以是车辆的实时位置，例如，在自由浮动的部分交通工具中  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#location](https://purl.eu/ns/mobility/passenger-transport-hubs#location)	- `object`:       
- `ResourceReport.meansOfTransport[object]`: 资源的运输工具类型  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#Mobiliteitsdienst.vervoermiddel](https://purl.eu/ns/mobility/passenger-transport-hubs#Mobiliteitsdienst.vervoermiddel)	- `MeansOfTransport.preferredLabel[string]`: 首选标签。枚举：'飞机、自行车、船、公共汽车、汽车、自动扶梯、电梯、摩托车、脚踏车、踏板车、滑板、台阶、地铁、火车、电车、跑步机、卡车'。  . Model: [ http://www.w3.org/2004/02/skos/core#prefLabel]( http://www.w3.org/2004/02/skos/core#prefLabel)    
- `ResourceReport.number[number]`: 资源数量  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#number](https://purl.eu/ns/mobility/passenger-transport-hubs#number)- `ResourceReport.reportTime[date-time]`: 报告有效的时间点  . Model: [http://purl.org/dc/elements/1.1/date](http://purl.org/dc/elements/1.1/date)- `ResourceReport.service[object]`: 资源报告中使用的移动服务  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#service](https://purl.eu/ns/mobility/passenger-transport-hubs#service)	- `object`:       
- `ResourceReport.status[object]`: 资源的状态。例如，保留、非活动、可用。确定是否可以使用资源  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#status](https://purl.eu/ns/mobility/passenger-transport-hubs#status)	- `ResourceStatus.preferredLabel[string]`: 首选标签。枚举：'可用、已删除、非活动、使用中、已重新定位、保留、不可用'。  . Model: [ http://www.w3.org/2004/02/skos/core#prefLabel]( http://www.w3.org/2004/02/skos/core#prefLabel)    
- `ResourceReport.type[object]`: 资源性质  . Model: [http://purl.org/dc/terms/type](http://purl.org/dc/terms/type)	- `ResourceType.preferredLabel[string]`: 首选标签。枚举：'充电站、停车空间、房间、座位、车辆'。  . Model: [ http://www.w3.org/2004/02/skos/core#prefLabel]( http://www.w3.org/2004/02/skos/core#prefLabel)    
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: NGSI 实体类型。必须是 ResourceReport  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `ResourceReport.number`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
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
## 有效载荷示例    
#### ResourceReport NGSI-v2 key-values 示例    
下面是一个以 JSON-LD 格式作为键值的资源报告示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### 资源报告 NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 ResourceReport 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### ResourceReport NGSI-LD key-values 示例    
下面是一个以 JSON-LD 格式作为键值的资源报告示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
#### 资源报告 NGSI-LD 标准化示例    
下面是一个规范化 JSON-LD 格式的 ResourceReport 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
