# Info about DataSourceRequest.Page and DataSourceRequest.Skip attributes

## Question

**Cla** asked on 16 May 2024

Hi, i need to design a class to handle pagination in my api endpoints, so i have a question about 2 properties of DataSourceRequest. Page: I assume it's used only in pagination to set the page number. Skip: I assume it's used only on virtual pagination to define the records to skip. I think this 2 properties as mutual exclusive (if used Page, Skip is ignored, if used Skip, Page is ignored). Is this true or there are situations where are both used? and if one exclude the other... why you have not handled the pagination only with Skip / Take properties (assumed who Take correspond to PageSize in classic pagination, Page can be calculated as ( Skip / Take ) + 1)? i need this answers because if this properties are multual exclusive i assume i can design my pagination class with only 2 properties ( Skip / Take ) instead of 3 ( Page / PageSize / Skip ) as done in DataSourceRequest object. Thanks Thanks

## Answer

**Nansi** answered on 21 May 2024

Hello Claudio, You are correct and we do not mix virtualization with paging, as they are alternatives to the same feature. However, some use cases may not require virtualization and thus the Skip won't be applicable. In this case, you cannot calculate the Page. If you need assistance with the implementation of the logic, I can recommend our Professional Services. Regards, Nansi Progress Telerik
