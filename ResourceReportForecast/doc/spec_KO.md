<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 리소스 보고서 예측    
===============<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.OSLO/blob/master/ResourceReportForecast/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **승객 운송 허브 AP 스키마 사양을 충족하는 리소스 보고서 예측 스키마입니다. 보고서를 요청하는 사람이 정의한 필터를 기반으로 모빌리티 서비스에 연결된 리소스에 대한 예상치를 요약한 것입니다.    
버전: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `ResourceReport.actuator[object]`: 운송 수단의 엔진  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#actuator](https://purl.eu/ns/mobility/passenger-transport-hubs#actuator)	- `ActuatorType.preferredLabel[string]`: 기본 레이블. Enum:'combustionEngine, electric, electricWithSupport, human'  . Model: [ http://www.w3.org/2004/02/skos/core#prefLabel]( http://www.w3.org/2004/02/skos/core#prefLabel)    
	- `type`:       
- `ResourceReport.location[object]`: 리소스의 위치. 자전거 주차 스테이션 또는 차량의 실시간 위치(예: 자유 유동 부품 운송)일 수 있습니다.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#location](https://purl.eu/ns/mobility/passenger-transport-hubs#location)	- `object`:       
	- `type`:       
- `ResourceReport.meansOfTransport[object]`: 리소스의 운송 수단 유형  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#Mobiliteitsdienst.vervoermiddel](https://purl.eu/ns/mobility/passenger-transport-hubs#Mobiliteitsdienst.vervoermiddel)	- `MeansOfTransport.preferredLabel[string]`: 기본 레이블. Enum:'비행기, 자전거, 보트, 버스, 자동차, 에스컬레이터, 리프트, 오토바이, 온풋, 페델렉, 스쿠터, 스케이트보드, 계단, 지하철, 기차, 트램, 러닝머신, 트럭'  . Model: [ http://www.w3.org/2004/02/skos/core#prefLabel]( http://www.w3.org/2004/02/skos/core#prefLabel)    
	- `type`:       
- `ResourceReport.number[number]`: 리소스 수  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#number](https://purl.eu/ns/mobility/passenger-transport-hubs#number)- `ResourceReport.reportTime[date-time]`: 보고서가 유효한 시점  . Model: [http://purl.org/dc/elements/1.1/date](http://purl.org/dc/elements/1.1/date)- `ResourceReport.service[object]`: 리소스 보고서 내에서 사용되는 모빌리티 서비스  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#service](https://purl.eu/ns/mobility/passenger-transport-hubs#service)	- `object`:       
	- `type`:       
- `ResourceReport.status[object]`: 리소스 상태. 예: 예약됨, 비활성, 사용 가능. 리소스를 사용할 수 있는지 여부를 결정합니다.  . Model: [https://purl.eu/ns/mobility/passenger-transport-hubs#status](https://purl.eu/ns/mobility/passenger-transport-hubs#status)	- `ResourceStatus.preferredLabel[string]`: 기본 레이블. Enum:'사용 가능, 삭제됨, 비활성, 사용 중, 재배치됨, 예약됨, 사용 불가능'  . Model: [ http://www.w3.org/2004/02/skos/core#prefLabel]( http://www.w3.org/2004/02/skos/core#prefLabel)    
	- `type`:       
- `ResourceReport.type[object]`: 리소스의 특성  . Model: [http://purl.org/dc/terms/type](http://purl.org/dc/terms/type)	- `ResourceType.preferredLabel[string]`: 기본 레이블. Enum:'충전소, 주차공간, 객실, 좌석, 차량'  . Model: [ http://www.w3.org/2004/02/skos/core#prefLabel]( http://www.w3.org/2004/02/skos/core#prefLabel)    
	- `type`:       
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI 엔티티 유형. ResourceReportForecast여야 합니다.  - `validFrom[date-time]`: 유효 기간 시작 날짜 및 시간  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `validTo[date-time]`: 유효 기간 종료 날짜 및 시간  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `validity[string]`: 이 예측의 유효 기간을 ISO8601 시간 간격으로 포함합니다. 두 개의 별도 속성을 사용할 수도 있습니다: 유효기간`, `유효기간`.  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `ResourceReport.number`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
ResourceReportForecast:      
  description: Resource Report Forecast Schema meeting Passenger Transport Hubs AP Schema specification. A summary of the expectations of the resources connected to mobility services based on defined filters by the person requesting the report.      
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
      description: NGSI Entity type. It has to be ResourceReportForecast      
      enum:      
        - ResourceReportForecast      
      type: string      
      x-ngsi:      
        type: Property      
    validFrom:      
      description: Validity period start date and time      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    validTo:      
      description: Validity period end date and time      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    validity:      
      description: 'Includes the validity period for this forecast as a ISO8601 time interval. It can be also used two separate attributes: `validFrom`, `validTo`'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
  required:      
    - id      
    - type      
    - ResourceReport.number      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.OSLO/blob/master/ResourceReportForecast/LICENSE.md      
  x-model-schema: https://github.com/smart-data-models/dataModel.OSLO/raw/master/ResourceReport/schema.json      
  x-model-tags: GreenMov      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### ResourceReportForecast NGSI-v2 키-값 예시    
다음은 키 값으로 JSON-LD 형식의 리소스 리포트 예측의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "http://example.org/resourcereport/1",  
  "type": "ResourceReportForecast",  
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
  "validFrom": "2022-05-07T06:43:37Z",  
  "validTo": "2022-05-07T07:43:37Z"  
}  
```  
</details>    
#### ResourceReportForecast NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 리소스 보고서 예측의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
  "type": "ResourceReportForecast",  
  "validFrom": {  
    "type": "DateTime",  
    "value": "2022-05-07T06:43:37Z"  
  },  
  "validTo": {  
    "type": "DateTime",  
    "value": "2022-05-07T07:43:37Z"  
  }  
}  
```  
</details>    
#### ResourceReportForecast NGSI-LD 키-값 예시    
다음은 키 값으로 JSON-LD 형식의 리소스 보고서 예측의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "http://example.org/resourcereport/1",  
  "type": "ResourceReportForecast",  
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
  "validFrom": "2022-05-07T06:43:37Z",  
  "validTo": "2022-05-07T07:43:37Z",  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.OSLO/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### ResourceReportForecast NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 리소스 보고서 예측의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
    "validFrom": {  
        "type": "Property",  
        "value": {  
            "@type": "Date-Time",  
            "@value": "2022-05-07T06:43:37Z"  
        }  
    },  
    "validTo": {  
        "type": "Property",  
        "value": {  
            "@type": "Date-Time",  
            "@value": "2022-05-07T07:43:37Z"  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
