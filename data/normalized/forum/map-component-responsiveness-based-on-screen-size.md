# Map Component: Responsiveness based on screen size

## Question

**Eri** asked on 07 Jul 2023

Is it possible to make the Map component responsive based on screen size? For example if I just want a "static" map of the continental United States (no panning or additional zooming), is it possible to automatically refresh the map as I resize the browser window? It would be nice to automatically re-center to the same visual location I was previously and have it resize accordingly.

## Answer

**Hristian Stefanov** answered on 11 Jul 2023

Hi Eric, As far as I understand, it appears that you need a responsive Map that adapts to changes in the browser's width and height. To achieve this functionality, you can utilize the MediaQuery component. By incorporating a media query, you can track the current screen size and dynamically adjust the width and height of the Map accordingly. Furthermore, it is important to set the "Center" parameter of the Map to ensure that the initial position is maintained even during screen resizing. To assist you further, I have prepared an example below. It showcases a MediaQuery implementation that alters the Map size based on the screen width. I encourage you to run and test it by reducing the screen width to under "700px" to observe the resulting behavior: <TelerikMediaQuery Media="(max-width: 700px)" OnChange="@MediaQueryChange"> </TelerikMediaQuery> @if (!MapDynamicRefresh)
{ <TelerikMap Height="@MapHeight" Center="@CenterMap" Width="@MapWidth"> <MapLayers> <MapLayer Type="@MapLayersType.Tile" Attribution="@Attribution" Subdomains="@Subdomains" UrlTemplate="@UrlTemplate"> </MapLayer> </MapLayers> </TelerikMap> }

@code {
public string MapHeight { get; set; }="600px";
public string MapWidth { get; set; }="800px";
public bool MapDynamicRefresh { get; set; }

public double[] CenterMap { get; set; }=new double[] { 30.268107, -97.744821 };

private async Task MediaQueryChange(bool matches)
{
if (matches)
{
MapWidth="400px";
MapDynamicRefresh=true;
await Task.Delay(5);
MapDynamicRefresh=false;
}
else
{
MapWidth="800px";
MapDynamicRefresh=true;
await Task.Delay(5);
MapDynamicRefresh=false;
}
}

public string[] Subdomains { get; set; }=new string[] { "a", "b", "c" };
public string UrlTemplate { get; set; }="[https://#=subdomain](https://#=subdomain) #.tile.openstreetmap.org/#=zoom #/#=x #/#=y #.png";
public string Attribution { get; set; }=" &copy; <a href='[https://osm.org/copyright'>](https://osm.org/copyright'>) OpenStreetMap contributors </a> ";
} Please feel free to experiment with this example and let me know if you encounter any difficulties or have any additional questions. Regards, Hristian Stefanov
