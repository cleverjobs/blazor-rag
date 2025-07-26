# Binding Kendo UI Map component marker data

## Question

**Ren** asked on 25 Mar 2021

Hi, UI for Blazor does not have a native Map component. I have managed to include a Kendo UI for jQuery Map component in my Blazor WASM project but now want to bind the markers to data provided by the Blazor page hosting the component. Is this possible? If so how, if not what are the alternatives? Regards

## Answer

**Marin Bratanov** answered on 25 Mar 2021

Hi Renier, The easiest option is to use remote marker binding and return the necessary JSON from an endpoint, like in this demo: [https://demos.telerik.com/kendo-ui/map/remote-markers.](https://demos.telerik.com/kendo-ui/map/remote-markers.) You can get the JSON by serializing your models that describe the markers from the action. Another approach would be to serialize those markers from the blazor component and pass them along in the JS Interop call. You can see a sample collection of markers in this demo (there is only one but it shows the structure): [https://demos.telerik.com/kendo-ui/map/index.](https://demos.telerik.com/kendo-ui/map/index.) If you already have that collection in the blazor component this can be simply another argument to the JS function. You can also Follow the creation of a Map component for Blazor here: [https://feedback.telerik.com/blazor/1430932-mapview-for-blazor.](https://feedback.telerik.com/blazor/1430932-mapview-for-blazor.) I believe you have already found it, and I am adding the link for anyone else who might see this post. Regards, Marin Bratanov

### Response

**Renier Pretorius** answered on 25 Mar 2021

Hi Marin, Thanks for the feedback. I was thinking of adding the the markers through the JS Interop call. My challenge is that I come from WPF/Silverlight and have not done any javascript so figuring out how to do it is a bit of effort, but should get there eventually. I cannot believe that there are only 30 votes for the map component. The possibilities especially in LoB applications are huge. I really hope others join the call for it. Regards Renier

### Response

**Marin Bratanov** answered on 25 Mar 2021

Hi Renier, Just passing the collection of models to the JS Interop will have the framework serialize them. If there isn't anything special in those models, that will work out of the box. For example, let's take this simple script that loops over a collection it receives as an argument: function consumeMarkers ( markers ) { for (i=0; i <markers.length; i++)
{ console.dir(markers[i]);
}
} To give it that argument, we only need to pass it to the .NET method: @inject IJSRuntime _js

<button @onclick="@SendToJs">send to js</button>

@code{ async Task SendToJs ( ) {
List<MyMarker> markers=new List<MyMarker>()
{ new MyMarker
{
id=1,
name="first",
coords=new double [] { 1.234, 5.678 }
}, new MyMarker
{
id=2,
name="second",
coords=new double [] { 9.876, 4.567 }
},
}; await _js.InvokeVoidAsync( "consumeMarkers", markers ); } public class MyMarker { public int id { get; set; } public string name { get; set; } public double [] coords { get; set; }
}
} We are monitoring the popularity of feature requests on the portal and we do act accordingly. If you sort by popularity you will see that the majority of the most popular things have been implemented. There is some delay around PDFs because WebAssembly still struggles a little with the performance that's needed for that to work as users would expect it. Regards, Marin Bratanov

### Response

**Renier Pretorius** answered on 25 Mar 2021

Brilliant thanks! I will give it a go. For anyone reading this that is not a

### Response

**Marin Bratanov** answered on 25 Mar 2021

Thank you so much for the kind words, Renier, and for your loyalty! Regards, Marin Bratanov
