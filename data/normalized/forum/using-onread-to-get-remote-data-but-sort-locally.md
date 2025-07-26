# Using OnRead to get remote data but sort locally

## Question

**Way** asked on 19 May 2021

I am using OnRead to get remote data but sometimes I want to sort locally (all the data is loaded). Is there a way to do that?

## Answer

**Marin Bratanov** answered on 20 May 2021

Hello Wayne, You do not need to use OnRead for this. You can just fetch all the data from your endpoint and pass it to the grid Data. Then, the grid will take care of all operations such as sorting and filtering (event including grouping) for you without you writing a single line of code. Nevertheless, if you do want to use OnRead for some reason (which would be the need to customize some behavior), you can easily use the .ToDataSourceResult() extension method we offer: [https://docs.telerik.com/blazor-ui/components/grid/manual-operations#telerik-todatasourceresultrequest.](https://docs.telerik.com/blazor-ui/components/grid/manual-operations#telerik-todatasourceresultrequest.) Regards, Marin Bratanov Progress Telerik

### Response

**Wayne Hiller** commented on 20 May 2021

The reason I am using the OnRead is this is a generic listing component where most of the time not all of the data is loaded from the server. I just happened to have one or two cases where all the data is read. I decided to just do the sorting on the server side.

### Response

**Marin Bratanov** commented on 20 May 2021

I think that you can still handle the OnRead event and if you have the local data - use .ToDataSourceResult() in the local app, and if not - send it to the server for processing. You could encapsulate all that logic in a service that always returns the same to the grid (see the serialization sample) and do the rest of the logic in the service.
