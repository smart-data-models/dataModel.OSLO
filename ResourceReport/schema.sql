/* (Beta) Export of data model ResourceReport of the subject dataModel.OSLO for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ResourceReport_type AS ENUM ('ResourceReport');
CREATE TABLE ResourceReport (ResourceReport.actuator json, ResourceReport.location json, ResourceReport.meansOfTransport json, ResourceReport.number integer, ResourceReport.reportTime timestamp, ResourceReport.service json, ResourceReport.status json, ResourceReport.type json, address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, id text, location json, name text, owner json, seeAlso json, source text, type ResourceReport_type);