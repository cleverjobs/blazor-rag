# transform incoming Grid state to an OData4-compatible string.

## Question

**kha** asked on 24 Oct 2019

hi i was looking for a way in ui for blazor to transform grid state to odata compatible string or something like QueryableExtensions in kendo like this

## Answer

**Marin Bratanov** answered on 25 Oct 2019

Hi Khashayar, The data request of the grid is available in the OnRead event under eventArgs.Request. It's type is DataSourceRequest and it is the same type used in the Telerik UI for ASP.NET MVC and Telerik UI for ASP.NET Core, so that you will be able to reuse existing API endpoints that accept it as a parameter, so you can then extract information from it or use linq expressions to populate it with data. In server-side Blazor apps you should be able to pass it as an argument to a service that can reuse it. The issue with using that in Blazor at the moment is for client-side applications or with endpoints is that the class is not yet serializable. We are working on making it serializable. Is this what you seek? We already have a request for serializing to oData that you can Follow here: [https://feedback.telerik.com/blazor/1406084-expose-odata-string-from-the-grid-request-object.](https://feedback.telerik.com/blazor/1406084-expose-odata-string-from-the-grid-request-object.) If this is not what you want to get, could you provide some more details on the use case and goal? Regards, Marin Bratanov
