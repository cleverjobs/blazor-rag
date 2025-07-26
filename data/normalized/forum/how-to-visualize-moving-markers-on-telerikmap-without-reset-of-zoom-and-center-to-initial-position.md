# How to visualize moving markers on TelerikMap, without reset of Zoom and Center to initial position.

## Question

**Pla** asked on 15 Aug 2023

Hello, I would like to visualize moving objects on the map using Marker Layer on TelerikMap. The problem I have is that each refresh on the map resets the Center and Zoom parameters of the map to initial position. If I omit the Center and Zoom parameters of TelerikMap and initially manually zoom to my desired position - all works as expected. The user can move his view point on any place and observe the passing markers without reset to the starting view point. How can I set only initial zoom and center? <TelerikMap Height="300px" Center="@_center" Zoom="_zoom" @ref="_map"> <MapLayers> <MapLayer Type="@MapLayersType.Tile" Attribution="@Attribution" Subdomains="@Subdomains" UrlTemplate="@UrlTemplate"> </MapLayer> <MapLayer Type="MapLayersType.Marker" Data="@_positions" LocationField="@nameof(DeviceOnMap.LatLng)" TitleField="@nameof(DeviceOnMap.Imei)" /> </MapLayers> </TelerikMap> private async Task _moveTargets(CancellationToken token)
{ foreach ( var report in reports)
{ double [] position=new double [] { report.Location.Coordinate.Y, report.Location.Coordinate.X }; var device=_positions.Find(x=> x.Imei==report.Device.Imei); if (device !=null )
{
device.LatLng=position;
} else {
_positions.Add( new () { Imei=report.Device.Imei, LatLng=position });
} await InvokeAsync(StateHasChanged); await Task.Delay( 200, token);
}
}

## Answer

**Plamen** answered on 16 Aug 2023

The solution to the problem was to bind Zoom and Center to nullable types and set them to null when the movement of the markers starts. The map view point is no longer fixed to the initial center _center=null;
_zoom=null;

### Response

**Hristian Stefanov** commented on 17 Aug 2023

Hi Plamen, I'm happy to see you quickly found the solution on your own. Should another issue crop up with the zoom and center, let me know. Kind Regards, Hristian
