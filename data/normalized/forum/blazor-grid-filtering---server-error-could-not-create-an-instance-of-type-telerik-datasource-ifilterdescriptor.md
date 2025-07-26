# Blazor Grid Filtering - Server Error Could not create an instance of type Telerik.DataSource.IFilterDescriptor

## Question

**Chr** asked on 05 Jun 2020

Hello - I've been really enjoying my time with the Telerik Blazor Grid component, but I'm running into trouble with the filtering functionality. This is using a Blazor Web Assembly Client with a ASP.NET Core 3 backend. When my client requests data from the API without a filter, I get appropriate responses as expected. Paging works great, everything is good. As soon as I try any off-the-shelf filter, I get an error response from the server with the message : Could not create an instance of type Telerik.DataSource.IFilterDescriptor. Type is an interface or abstract class and cannot be instantiated. It looks like this is some sort of deserialization error that is being run into when the server is trying to parse my DataSourceRequest. It gets parsed fine without a filter, but as soon as I try to filter, I get the above message. Has anyone else seen and tackled this problem? Thanks much! - Chris

## Answer

**Marin Bratanov** answered on 08 Jun 2020

Hello Chris, With the default case, you must provide all the data in the view model so there will be no further calls to the api endpoint. If you have a lot of data and that's not feasible, you should use OnRead to implement custom filtering on the server: basics about the OnRead event: [https://docs.telerik.com/blazor-ui/components/grid/manual-operations](https://docs.telerik.com/blazor-ui/components/grid/manual-operations) examples of easy usage of custom filtering on the sever: [https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server/WasmApp](https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server/WasmApp) - provides more details and examples on how serialization and deserialization can work. If comparing against these does not help you move forward, please modify either sample project to showcase the issue and send it back to me so I can take a look. If the changes are more than a couple of lines, you could open a support ticket where you can attach zip archives. Regards, Marin Bratanov

### Response

**Jens Bo** answered on 10 Jun 2020

Hello Marin, I get the same error message when using grid filters in a Blazor WASM project setup somewhat like BlazingCoffee by Ed Charbeneau. In my case I have found that the error only arises when using NewtonSoft as opposed to using System.Text.JSon. I can reproduce the error by adding "services.AddMvc().AddNewtonsoftJson(x=> x.SerializerSettings.ReferenceLoopHandling=Newtonsoft.Json.ReferenceLoopHandling.Ignore).AddJsonOptions(o=> o.JsonSerializerOptions.PropertyNamingPolicy=null);" to the BlazingCoffee Startup configuration and then running the Sales page. If you can verify that the error is linked to using NewtonSoft (which I am bound to because of the referencelookhandling), could you advice on configuring the SerializerSettings or options to avoid the error? Or any other means of avoiding the error? Best regards, Jens Bo

### Response

**Marin Bratanov** answered on 12 Jun 2020

Hi Jens, This seems to work fine for me when I add it to the server project in this sample: [https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server/WasmApp.](https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server/WasmApp.) In the sample I am linking it is serialized and deserialized explicitly with System.Text.Json while in that app it is used directly (see here and here for example, and that maybe goes through Netwonsoft which breaks things on your end). We target the built-in serializer (System.Text.Json) when working on our DataSourceRequest object and targetting both is impossible without custom serializers that the app must provide according to its own serialization settings and needs. We made an example of this here: [https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server/CustomSerializer](https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server/CustomSerializer) Regards, Marin Bratanov

### Response

**Jens Bo** answered on 12 Jun 2020

Thanks for the advice. I implemented a CustomSerializer for the filters and it seems to work perfect. /Jens Bo

### Response

**Chris** answered on 12 Jun 2020

Thanks for the updates! I ended up implementing my own Model Binder, and my own class that inherits from DataSourceRequest. My custom class defines Filters as IList<FilterDescriptor> instead of IList<IFilterDescriptor>. Then my custom class deserializes OK, and I can convert it into a DataSourceRequest within the Model Binder, and everything works out OK. If it really is just a matter of changing our Json utility, that would have of course been easier, so hopefully that simple step works for others!

### Response

**Marin Bratanov** answered on 12 Jun 2020

Thank you for sharing this with everyone, Chris. To add some context and a few things that may be useful: The FilterDescriptor class can work only for FilterRow filtering, the FilterMenu uses CompositeFilterDescriptor, you can check the custom converter in our sample for an example. The approach of using a custom wrapper over the DataSourceResult is valid - we do something similar with the DataEnvelope class. The reason why that is needed is because the DataSourceResult uses interfaces for the return types to be flexible, but it looks like the framework can't serialize those, so a concrete implementation is needed for serialization over JSON. So, with this in mind, it is up to you to choose the JSON utility - we work with the standard one, but your app can do whatever it needs to. The Grid (and other components) ultimately need you to get the data in the view-model - you have total freedom on the "how". Regards, Marin Bratanov

### Response

**Jordy** answered on 18 May 2022

Going off of your solution, I Wrote a wrapper around the DataSourceRequest with a custom modelbinder, but didn't define any variables. [ ModelBinder(BinderType=typeof(DataSourceModelBinder)) ] public class DataSourceRequestWrapper: DataSourceRequest {
} My custom modelbinder just uses the system.text.json deserializer to deserialize the wrapper and this seems to work for us. public class DataSourceModelBinder: IModelBinder { public async Task BindModelAsync ( ModelBindingContext bindingContext ) { if (bindingContext==null )
{ throw new ArgumentNullException( nameof (bindingContext));
} if (bindingContext.ModelType==typeof (DataSourceRequestWrapper))
{ var bodyStream=bindingContext.HttpContext.Request.Body; var request=await JsonSerializer.DeserializeAsync<DataSourceRequestWrapper>(bodyStream);

bindingContext.Result=ModelBindingResult.Success(request);
}
}
} I hope this helps someone else that stumbles on this problem. If anyone else finds a better way, please don't hesitate to correct me.

### Response

**Marin Bratanov** commented on 18 May 2022

Thanks for sharing, Jordy! I converted your post to an Answer for better visibility. If the default options linked in the sample projects in mine don't help (say, are not suitable or you are using some other approach), that sounds like a valid way to get the object creation working.
