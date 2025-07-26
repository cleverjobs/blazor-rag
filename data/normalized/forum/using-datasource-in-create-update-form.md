# Using DataSource in Create/Update form?

## Question

**Jst** asked on 11 Jan 2023

Is it possible to use the DataSource library to create or update a record via an Odata Endpoint? Any sample or example code?

## Answer

**Dimo** answered on 16 Jan 2023

Hello John, I confirm this is outside the scope of the Telerik.DataSource package. We provide a ToODataString () method, which is an extension method for the DataSourceRequest. It translates the DataSourceRequest properties to a URL query string, and it resides in Telerik.Blazor. The DataSourceRequest object exists in the OnRead event argument. This object is related only to read operations and does not exist in the create/update events of our components. I believe you don't need OData functionality from us for editing, because there are no custom properties from us to translate. You only serialize the data item before sending it to the OData endpoint. Regards, Dimo
