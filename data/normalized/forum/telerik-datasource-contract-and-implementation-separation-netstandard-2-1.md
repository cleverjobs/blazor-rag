# telerik.datasource contract and implementation separation (netstandard 2.1)

## Question

**** asked on 29 Jul 2021

The Telerik.DataSource nuget package has been updated to major version 2 with a dependency on netstandard 2.1. This causes issues for older services that are still using the full .net framework. For example, we are moving to a microservice architecture, where microservices are targeting .net core 3.1+, but the monolith the functionality is being cut out of is still using .net framework (and will use it until it dies a horrible fiery death). The communication between the microservices and monolith is based on contract assemblies, that have to target netstandard 2.0 for compatibility. Now, one of these microservices would like to expose a query API for a backoffice UI microservice using the Telerik.DataSource DataSourceRequest/DataEnvelope contract for convenient binding to Telerik widgets. The contract assembly for this communication is however also used by the old monolith to cover functionality not yet cut out to modern microservices. Now, to the question. Is there in the works (or in the stars) a separation of the Telerik.DataSource actual contract package (the aforementioned DataSourceRequest "DTO" structure, targeting netstandard 2.0) and the implementation package (targeting netstandard 2.1)?. I've played around a bit with the source code and it looks feasible from my point of view, just not sure it would be worth the effort on your end. I do imagine though that more customers will run into this issue when migrating? I would be glad to help (with a pull request maybe) if you are interested and think that this would be worthwhile (I do realise this would be a breaking change)...

## Answer

**Radko** answered on 03 Aug 2021

Hi, Using different versions of the DataSource package might work for such a scenario. For example, have the DataSource 2+ used within the .NET Core 3.1+ microservice and an older version, like DataSource 1.3.0 for the project running on .NET Framework. However, you are very likely to incur certain issues which could possibly be resolved with some custom logic by unifying the models. However, this is not something we guarantee will work and is speculation rather than fact. As for a separation of the packages and to support .NET Standard 2.0 in general - currently, we have no plans to support such a use case. Regards, Radko Stanev

### Response

**** commented on 05 Aug 2021

hi, thanks for the reply, that's one of the options that we have considered internally as well... In the end, we decided against it as any changes to the contracts in the 2.# line would most likely not be reflected in the 1.# line as well and that would cause even more issues. Right now we decided to keep the Telerik.DataSource based requests and responses out of our internal contracts assembly, and only provide the shape of the actual data returned (i. e. the actual DTO only, not the telerik wrappers around it). Thanks, Regards, Pavel

### Response

**Radko** commented on 09 Aug 2021

Hello Pavel, Indeed, it is likely this will require ongoing work if/when any changes to the API appear rather than being a one-time effort. Regards, Radko Stanev
