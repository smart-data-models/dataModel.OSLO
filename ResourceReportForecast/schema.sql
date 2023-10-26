/* (Beta) Export of data model ResourceReportForecast of the subject dataModel.OSLO for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ResourceReportForecast_type AS ENUM ('ResourceReportForecast');
CREATE TABLE ResourceReportForecast (ResourceReport.actuator JSON, ResourceReport.location JSON, ResourceReport.meansOfTransport JSON, ResourceReport.number NUMERIC, ResourceReport.reportTime TIMESTAMP, ResourceReport.service JSON, ResourceReport.status JSON, ResourceReport.type JSON, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, type ResourceReportForecast_type, validFrom TIMESTAMP, validTo TIMESTAMP, validity TEXT);