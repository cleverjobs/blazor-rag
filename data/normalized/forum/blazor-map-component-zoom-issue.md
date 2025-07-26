# Blazor Map component zoom issue

## Question

**Jac** asked on 30 Oct 2023

I've got a strange issue with zooming via mouse scroll. After every change in marker and center (I need both of them, so I didn't test it separately) the zoom is running faster and faster, but only when using mouse scroll. Am I doing something wrong or it's a bug? You can test it with the code below and clicking the Random button on top a few times and than trying to mouse scroll. It's not a critical issue but quite annoyance. Using `MapRef.Refresh()` instead of `StateHasChanged()`seems to not fix the issue. <TelerikButton OnClick="()=> Random()">Random</TelerikButton>

<TelerikMap Center="@Center" Zoom="17">
<MapLayers>
<MapLayer Type="@MapLayersType.Marker" Data="@MarkerData1" LocationField="@nameof(MarkerModel.LatLng)" TitleField="@nameof(MarkerModel.Title)" Shape="MapMarkersShape.Pin">
</MapLayer>

<MapLayer Type="@MapLayersType.Tile" Attribution="@Attribution" Subdomains="@Subdomains" UrlTemplate="@UrlTemplate">
</MapLayer>
</MapLayers>
</TelerikMap>

@code { public string [] Subdomains { get; set; }=new string [] { "a", "b", "c" }; public string UrlTemplate { get; set; }="[https://#=subdomain](https://#=subdomain) #.tile.openstreetmap.org/#=zoom #/#=x #/#=y #.png"; public string Attribution { get; set; }="&copy; <a href='[https://osm.org/copyright'>OpenStreetMap](https://osm.org/copyright'>OpenStreetMap) contributors</a>"; public double [] Center { get; set; }=new double [] { 60.268107, 97.744821 }; public List<MarkerModel> MarkerData1 { get; set; }=new List<MarkerModel>()
{ new MarkerModel()
{
LatLng=new double [] { 60.268107, 97.744821 },
Title="Austin, TX" }
}; public void Random () { var marker=MarkerData1.First();
Random random=new Random(); var lat=random.NextDouble() * 90; var lng=random.NextDouble() * 90;
marker.LatLng=new double [] { lat, lng };

Center=new double [] { lat, lng };
StateHasChanged();
} public class MarkerModel { public double [] LatLng { get; set; } public string Title { get; set; }
}
}

## Answer

**Hristian Stefanov** answered on 02 Nov 2023

Hi Jacek, I confirm that the issue at hand is related to a known bug in the scrolling behavior. This issue has already been reported publicly under the title: ' Unify the zoom action behavior when using the plus button and mouse wheel '. I voted there on your behalf and raised the priority. Once the fix is implemented, it will address the scenario you've encountered. To stay updated on its progress, you also have the option to subscribe to the item and receive email notifications for status updates. Regards, Hristian Stefanov Progress Telerik

### Response

**Maxime** commented on 11 Jan 2024

Hello, I have the same problem. I have voted for the feature and hope it will be planned soon. Regards, Maxime Lavergne

### Response

**Michal** commented on 23 Jun 2024

We are at 2024... hotfix if you have ONLY ONE map at page. - "ugly!!", but at least something. Until it will be fixed at Telerik-blazor.js.... <script> var xlisteners=[]; //var gmapref=document.querySelector(".k-map") !! null var f=EventTarget. prototype. addEventListener; EventTarget. prototype. addEventListener=function ( type, fn, capture ) { //this.f=f; if (type=="wheel" && this. className. includes ( "k-map" )) { if (xlisteners. length> 0 ) { /*alert('skip...' + xlisteners.length);*/ return; } //DO NOTHING this. f=f;
xlisteners. push (fn); //for later cleanup use... this. f (type, fn, capture); //alert('added...' + xlisteners.length); } else { this. f=f; this. f (type, fn, capture);
}

} //jf you want it call from code like: await JS.InvokeVoidAsync("mcleanup", "abcdefg"); function mcleanup ( mid ) { if (xlisteners. length> 1 ) { var element=document. querySelector ( ".k-map" ); for ( let i=1; i <xlisteners. length; i++) { console. log (i, xlisteners[i]);
element. removeEventListener ( "wheel", xlisteners[i], { passive: true });
} //xlisteners.forEach((it)=> { element.removeEventListener("wheel", it, { passive: true }); console.log(it); }); xlisteners. splice ( 1 ); alert ( 'removed...' );
}
}

### Response

**Hristian Stefanov** commented on 24 Jun 2024

Hi Michal, Thank you for sharing a workaround until the bug is resolved, so other developers can benefit from it. I confirm that the item is now planned for our next release in August. Kind Regards, Hristian
