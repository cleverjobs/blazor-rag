# More info on Maps and Layers

## Question

**RobRob** asked on 12 Mar 2024

My requirements: Ability for user to add shapes (rectangle, square, circle) or image to a map. Ability for the user to move that shape around on a map (drag and drop). Ability for the user to save all the placed shape geolocations. Ability to read the saved shape geolocations and place them on the map. I did a little research on your Map control and it does seem to support layers and a specific layer type called "shape". However, when I look at the code sample I don't see any way to define the shape (circle, rectangle, etc.) nor provide dimensions for the shape (L X W) nor have a bitmap/image as a shape? I also didn't see any drag and drop support? Could I get answers to these questions and/or point me to documentation that supports my requirements? Cheers, Rob.

## Answer

**Dimo** answered on 13 Mar 2024

Hello Rob, Indeed, the listed requirements are currently not supported. I am sorry if this forces you to look for another third-party component. In addition - We have a feature request about drawing shapes on the Map, but it covers API for drawing by the application, and not by the user. The Shape layer works with GeoJSON data. The linked specification describes how to define shapes like points, polygons, etc. Regards, Dimo Progress Telerik

### Response

**Rob** commented on 13 Mar 2024

Thanks for the response Dimo. To clarify, the shapes will be predefined, the user will not draw or create the shapes, they will select predefined shapes and place them on a map. Look at the GeoJSON data it seems this might work: { "type": "Feature", "geometry": { "type": "Polygon", "coordinates": [
[
[ 100.0, 0.0 ],
[ 101.0, 0.0 ],
[ 101.0, 1.0 ],
[ 100.0, 1.0 ],
[ 100.0, 0.0 ]
]
]
} But it sounds like you don't support drag/move of these shapes and placement on the map? Do you have any recommendations for alternate controls/tools that might work with Blazor and easy to implement? We currently operate Blazor server-side but I guess we can do hybrid if needed. I'm not a fan of JS (in fact I hate it) but that said, if we have to use JS then so be it.

### Response

**Dimo** commented on 13 Mar 2024

If shape dragging is not a strict must, then a lot easier option is to select a shape from outside the Map and then click on the Map to place it - the component will tell you where the user clicked. Otherwise, a custom drag and drop implementation will require you to infer Map coordinates from JavaScript pointer events, which will be quite an adventure, to put it mildly.
