# Using the odata "expand" with DataSourceRequest?

## Question

**Jst** asked on 22 Jun 2021

Is it possible via the DataSourceRequest to generate the string to bring back sub objects and even sub sub objects? It does not seem to fit in the FilterDescriptor.

## Answer

**Stamo Gochev** answered on 25 Jun 2021

Hi, $expand (with filters) is part of the enhancements of OData v4 standard and is not targeted by the current version of the "ToODataString()" method (as well as other things like $search). However, you can modify the string returned from "ToODataString()" to include it, e.g.: var baseUrl="...odata/products?"; // results in something similar to "$filter=(CategoryId%20eq%202)"; var filterPart=args.Request.ToODataString(); // results in something similar to "$expand=Category($filter=(CategoryId%20eq%202)" var odatUrl=$" {baseUrl}?$expand=Category( { filterPart } ); The above idea can be modified to fit the exact project requirements. Regards, Stamo Gochev
