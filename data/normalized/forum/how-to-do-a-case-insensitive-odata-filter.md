# How to do a case-insensitive OData filter

## Question

**dca** asked on 20 Feb 2020

I am using the DataSourceRequest.ToODataString() but the resulting request to my OData is case sensitive. I have seen examples of the $filter clause that uses the OData tolower method to give case-insensitive search. For example, the following calls to me ASP.NET Core 3.1 / Microsoft.AspNetCore.Odata v7.3.0 API all return the same result set; [https://myapi/v1/accounts?$filter=contains(tolower(AccountName),tolower('eng'))&$top=2&$skip=0&$count=true](https://myapi/v1/accounts?$filter=contains(tolower(AccountName),tolower('eng'))&$top=2&$skip=0&$count=true) [https://myapi/v1/accounts?$filter=contains(tolower(AccountName),tolower('Eng'))&$top=2&$skip=0&$count=true](https://myapi/v1/accounts?$filter=contains(tolower(AccountName),tolower('Eng'))&$top=2&$skip=0&$count=true) [https://myapi/v1/accounts?$filter=contains(tolower(AccountName),tolower('eNg'))&$top=2&$skip=0&$count=true](https://myapi/v1/accounts?$filter=contains(tolower(AccountName),tolower('eNg'))&$top=2&$skip=0&$count=true) Is there a way to modify your DataSourceRequest.ToODataString to support this type of client site modification so I can use it to do case-insensitive filters?

## Answer

**Marin Bratanov** answered on 21 Feb 2020

Hello, Would either of these approaches work for your case right now: using DataSourceRequest.ToODataString().ToLowerInvariant() enabling case-insensitivity on the OData resolver itselft: [https://github.com/OData/WebApi/issues/812](https://github.com/OData/WebApi/issues/812) inserting the tolower() call by modifying the string before it gets to the OData service, something like this: [https://www.codeproject.com/Articles/1227943/Case-Insensitive-Search-Filter-in-OData-ASP-NET-Co](https://www.codeproject.com/Articles/1227943/Case-Insensitive-Search-Filter-in-OData-ASP-NET-Co) I am asking because at this point we don't have such a feature, but it looks like that heavily depends on the backend and database so using string operations might be the more flexible approach, and may let you use that right now as opposed to waiting for an implementation. Regards, Marin Bratanov
