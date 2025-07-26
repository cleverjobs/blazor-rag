# Custom image as map

## Question

**Ale** asked on 22 May 2024

Hi Team, is it possible to use a custom image inside the map control to place markers on? Next to the world map, we would like to provide some detailed information for buildings and use the building layout to place markers inside rooms. Thank you very much in advance! Alex

## Answer

**Nadezhda Tacheva** answered on 19 Jun 2024

Hi Alexander, I will address the relevant points separately, so we can cover all of them: Display image in the Map The Map does not support displaying one whole image. Its Tile layer expects to receive a set of tiles that correspond to the specific zoom level, x and y coordinates. This is why these values should be included in the UrlTemplate, so the Map knows where to position the corresponding tile. We do not have such an example as this targets a completely custom scenario. You may try to customize the default behavior of the Tile layer but I cannot guarantee yuo can get the exact desired result. My suggestion was to divide your image into small pieces - separate images that build up the whole picture. The reason for that is to use them as tiles, so you can mimic the default Map behavior. For reference, you may check how the tiles here form the whole Map: If you check the tile image links, you may notice how they contain the zoom level and the coordinates. Zoomable=false not working I noticed you have submitted a ticket on this matter, where I just responded. I suggest keeping the discussion there, so we do not mix the topics. Change the color of the marker The simplest option that comes to my mind is to use CSS to modify the color of the markers. You may target the <span class="k-svg-i-map-marker-target"> element. If you need to set different colors for the markers, you may utilize the CSS selectors based on the marker title like so: [https://blazorrepl.telerik.com/GoOqlZbv15D9A30s16.](https://blazorrepl.telerik.com/GoOqlZbv15D9A30s16.) Regards, Nadezhda Tacheva Progress Telerik

### Response

**Alexander** commented on 19 Jun 2024

Hi Nadezhda, thank you very much for your detailled explanation. I haven't thought about looking into the browsers dev tools to have a look what is actually shown inside the map component. Splitting my image into seperate tiles should be possible, I will try mimic a tile provider for my custom layouts. Do you think it is worth a try to put the possibilty to use a custom image for the map component as a feature request? Maybe playing some markers onto custom images is also interesting for other customers. Also thank you very much for your example how to change the marker colors. Best regards, Alexander Schneider

### Response

**Alexander** commented on 24 Jun 2024

Hi Nadezhda, I just want to share my solution, maybe others are also interested: Map Center is set to 0,0 Zoom=4, so that enough tiles are visible on the component Zoomable and Pannable=false, Zoom and Pan buttons hidden with CSS Split every custom image into 4x4 subimages (256x256 pixels each, resize custom image to 1024x1024 pixels if necessary), add coordinates to each image name, e.g.: customimage_6_6.png UrlTemplate=CustomImageName + "_#=x #"+ "_#=y #.png" Visible tile coordinates at zoom=4 are 5,6 ... 5,9 6,6 ... 6,9 ... 10,6 ... 10,9 5,6 to 5,9 and 10,6 to 10,9 are just empty images to avoid missing image errors at the edges 6,6 to 9,9 are the sub images. Best regards, Alexander Schneider

### Response

**Nadezhda Tacheva** commented on 24 Jun 2024

Hi Alexander, Thank you for sharing your solution! In the meantime, I thought of another option that may be easier when using a static Map (without the panning and zooming functionalities). You may use CSS to target the wrapping element of the component and set your image as a background image. Here is a basic example: [https://blazorrepl.telerik.com/couUGSEs29beYlLW07.](https://blazorrepl.telerik.com/couUGSEs29beYlLW07.) I regret that I did not come up with that earlier but I decided to still share it in case you find it useful.

### Response

**Alexander** commented on 24 Jun 2024

Hi Nadezhda, this is indeed way easier than what I did. Also this makes my feature request for using custim images inside the map component obsolete. Thank you very much for this solution! Best regards, Alexander Schneider

### Response

**Nadezhda Tacheva** commented on 27 Jun 2024

Great! Thank you for the follow-up, Alexander! I am happy I was able to help and provide an easier alternative.

### Response

**Nadezhda Tacheva** answered on 27 May 2024

Hello Alexander, The layer that works with images in the Map component is called Tile layer. It works by rendering images (tiles) that display the actual map. These images are requested from third-party services from a URL configured in the component. The main idea is that the URL will be generated based on the urlTemplate and the zoom/x/z values. With that in mind, based on the passed zoom/x/y values from the Map, the tile provider must return the images for that particular coordinates for that particular zoom. To display a custom image in the Map, you may implement a custom solution. You can consider creating your own data provider to use in the Map. For example, you can divide the whole image (building layout) in smaller pieces (images) that will be served as tiles. You can save these tile images in a folder somewhere and expose a local or remote URL to obtain them. If you need to also use custom marker images, you can do that through the Marker layer template. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Alexander** commented on 27 May 2024

Hello Nadezhda, thank you very much for your help, I will try to set up my own data provider. Best regards, Alexander Schneider

### Response

**Alexander** answered on 14 Jun 2024

Hello Nadezhda, I was able to add a custom image to the tile layer, but even with zoom set to '0', the image is repeated multiple times on the map component. As URL template I am just directing to the local resources in wwwroot, like "images/mycustomimage.png". Do I have to put variables for zoom and coordinates into the URL template or do you have an example of how to configure the component to show the image just once? I have also set zoomable to 'false' (which does not seem to work by the way), because I just want to show one single tile with one single image. Best regards, Alexander Schneider

### Response

**Alexander** commented on 17 Jun 2024

And is there also a simple way to just change the color of the marker? Thank you very much! Best regards, Alexander Schneide
