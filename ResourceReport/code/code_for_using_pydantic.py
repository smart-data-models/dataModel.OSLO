from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class ActuatorTypePreferredLabel(Enum):
    combustionEngine = 'combustionEngine'
    electric = 'electric'
    electricWithSupport = 'electricWithSupport'
    human = 'human'


class Type(Enum):
    ActuatorType = 'ActuatorType'


class ResourceReportActuator(BaseModel):
    ActuatorType_preferredLabel: ActuatorTypePreferredLabel = Field(
        ...,
        alias='ActuatorType.preferredLabel',
        description="Preferred label. Enum:'combustionEngine, electric, electricWithSupport, human'",
    )
    type: Type


class ResourceReportLocation(BaseModel):
    object: Optional[AnyUrl] = None
    type: Optional[str] = None


class MeansOfTransportPreferredLabel(Enum):
    airplane = 'airplane'
    bicycle = 'bicycle'
    boat = 'boat'
    bus = 'bus'
    car = 'car'
    escalator = 'escalator'
    lift = 'lift'
    motorcycle = 'motorcycle'
    onFoot = 'onFoot'
    pedelec = 'pedelec'
    scooter = 'scooter'
    skateboard = 'skateboard'
    step = 'step'
    subway = 'subway'
    train = 'train'
    tram = 'tram'
    treadmill = 'treadmill'
    truck = 'truck'


class Type1(Enum):
    MeansOfTransport = 'MeansOfTransport'


class ResourceReportMeansOfTransport(BaseModel):
    MeansOfTransport_preferredLabel: MeansOfTransportPreferredLabel = Field(
        ...,
        alias='MeansOfTransport.preferredLabel',
        description="Preferred label. Enum:'airplane, bicycle, boat, bus, car, escalator, lift, motorcycle, onFoot, pedelec, scooter, skateboard, step, subway, train, tram, treadmill, truck'",
    )
    type: Type1


class ResourceReportService(BaseModel):
    object: Optional[AnyUrl] = None
    type: Optional[str] = None


class ResourceStatusPreferredLabel(Enum):
    available = 'available'
    deleted = 'deleted'
    inactive = 'inactive'
    inUse = 'inUse'
    relocated = 'relocated'
    reserved = 'reserved'
    unavailable = 'unavailable'


class Type2(Enum):
    ResourceStatus = 'ResourceStatus'


class ResourceReportStatus(BaseModel):
    ResourceStatus_preferredLabel: ResourceStatusPreferredLabel = Field(
        ...,
        alias='ResourceStatus.preferredLabel',
        description="Preferred label. Enum:'available, deleted, inactive, inUse, relocated, reserved, unavailable'",
    )
    type: Type2


class ResourceTypePreferredLabel(Enum):
    chargingStation = 'chargingStation'
    parkingSpace = 'parkingSpace'
    room = 'room'
    seating = 'seating'
    vehicle = 'vehicle'


class Type3(Enum):
    ResourceType = 'ResourceType'


class ResourceReportType(BaseModel):
    ResourceType_preferredLabel: ResourceTypePreferredLabel = Field(
        ...,
        alias='ResourceType.preferredLabel',
        description="Preferred label. Enum:'chargingStation, parkingSpace, room, seating, vehicle'",
    )
    type: Type3


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Type4(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type4


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type5(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type5


class Type6(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type6


class Type7(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type7


class Type8(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type8


class Type9(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type9


class Type10(Enum):
    ResourceReport = 'ResourceReport'


class ResourceReport(BaseModel):
    ResourceReport_actuator: Optional[ResourceReportActuator] = Field(
        None,
        alias='ResourceReport.actuator',
        description='Engine of the means of transport',
    )
    ResourceReport_location: Optional[ResourceReportLocation] = Field(
        None,
        alias='ResourceReport.location',
        description='Location of the Resource. This could be a bike parking station or the real-time location of the vehicle, e.g. in free-floating part transport',
    )
    ResourceReport_meansOfTransport: Optional[ResourceReportMeansOfTransport] = Field(
        None,
        alias='ResourceReport.meansOfTransport',
        description='The type of means of transport of the Resource',
    )
    ResourceReport_number: Optional[float] = Field(
        None, alias='ResourceReport.number', description='The number of resources'
    )
    ResourceReport_reportTime: Optional[AwareDatetime] = Field(
        None,
        alias='ResourceReport.reportTime',
        description='Point in time for which the report is valid',
    )
    ResourceReport_service: Optional[ResourceReportService] = Field(
        None,
        alias='ResourceReport.service',
        description='The MobilityService used within the ResourceReport',
    )
    ResourceReport_status: Optional[ResourceReportStatus] = Field(
        None,
        alias='ResourceReport.status',
        description='State of a Resource. E.g. reserved, inactive, available. Determines whether a resource can be used',
    )
    ResourceReport_type: Optional[ResourceReportType] = Field(
        None, alias='ResourceReport.type', description='Nature of the Resource'
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type10] = Field(
        None, description='NGSI Entity type. It has to be ResourceReport'
    )
