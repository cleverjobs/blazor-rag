# Serialize/DeSerialize DataSourceRequest and DataSourceResult

## Question

**Adr** asked on 05 May 2021

Hi, I am using the CSLA framework with Blazor WebAssembly and am trying to send the Telerik.DataSource.DataSourceRequest from the Blazor Client using a Telerik Blazor Grid through to the CSLA DataPortal API endpoint on the Blazor Server. Unfortunately the CSLA framework is unable to successfully serialize and de-serialize the Telerik.DataSource.DataSourceRequest object as is. I tried creating a CSLA compatible wrapper so that i could use the built-in CSLA serialization, unfortunately i have hit an issue in the fact that CSLA only supports serialization of primative types (int, float, string, datetime, etc). My discussion ( [https://github.com/MarimerLLC/csla/discussions/2268](https://github.com/MarimerLLC/csla/discussions/2268) ) on the CSLA repo suggests that I may need to serialize to a string or byte[] array. The option I'm left with is to manually serialize the entire Telerik.DataSource.DataSourceRequest object as either a string or byte[] array by using either System.Text.Json or Newtonsoft.Json. Then when the string or byte[] array is received by the CSLA DataPortal API endpoint I can manually de-serialize the parameter as a Telerik.DataSource.DataSourceRequest object. Looking at the Telerik docs it appears that the Telerik.DataSource.DataSourceRequest object supports System.Text.Json out of the box but if I want to use Newtonsoft.Json then i might have to do some custom serialization, therefore my preference would be to use System.Text.Json. How can I use System.Text.Json to serialize and de-serialize the Telerik.DataSource.DataSourceRequest object manually as my mode of transport to the CSLA DataPortal API endpoint doesn't use the native Blazor System.Text.Json serializer?

## Answer

**Adrian** answered on 06 May 2021

I have managed to acchieve successfully serializing and de-serializing the Telerik.DataSource.DataSourceRequest object using the 2 extension methods below: public static DataSourceRequestWrapper ToDataSourceRequestWrapper ( this Telerik.DataSource.DataSourceRequest dataSourceRequest ) { var jsonUtf8Bytes=JsonSerializer.SerializeToUtf8Bytes(dataSourceRequest); return new () {DataSourceRequestAsJson=jsonUtf8Bytes};
} public static Telerik.DataSource. DataSourceRequest ToDataSourceRequest ( this DataSourceRequestWrapper dataSourceRequestWrapper ) { var readOnlySpan=new ReadOnlySpan<byte>(dataSourceRequestWrapper.DataSourceRequestAsJson); var dataSourceRequest=JsonSerializer.Deserialize<Telerik.DataSource.DataSourceRequest>(readOnlySpan); return dataSourceRequest;
}

### Response

**Marin Bratanov** answered on 06 May 2021

Hello Adrian, You can find sample projects here: [https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server](https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server) Regards, Marin Bratanov Progress Telerik
