# Has the DataSourceRequest code been modified to handle the OData $Expand parameter?

## Question

**Jst** asked on 14 Dec 2022

I know DataSourceRequest was not able to handle the $Expand in previous versions. Has this been updated to allow the $Expand parameter yet?

## Answer

**Svetoslav Dimitrov** answered on 19 Dec 2022

Hello John, From what I understand the $Expand is used to get nested properties. You should be able to achieve the same result by adding the Include() method before the ToDataSourceResult(). Can you try the Include() method and get back to me if it helps you achieve the desired behavior? Regards, Svetoslav Dimitrov

### Response

**Jstemper** commented on 19 Dec 2022

How does ToDataSourceResult() work when we're accessing the data via OData endpoints? I would love to give it a try but it is unclear how it is to be used.

### Response

**Svetoslav Dimitrov** commented on 22 Dec 2022

Hello John, I am happy to report that after further investigation you should be able to use the $expand parameter as part of your base URL. You must be able to use the $expand parameter with Telerik UI for Blazor version 2.3.0 or later. Can you try adding the $expand and see if you will get the proper result in your service handler?
