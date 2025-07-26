# Chart axis labels, auto rotate or auto reduce # of labels

## Question

**Han** asked on 31 May 2023

Hi All In order to keep axis labels readable when a chart is resized, one can change the rotation Angle, or simply reduce the # of labels using the Step property. I do have a nifty routine for this, But, In order to do this my method would have to know the dimensions (e.g. width/heigth in px) of the targeted chart area. How can I obtain these dimensions? Regards, Hans

## Answer

**Nadezhda Tacheva** answered on 05 Jun 2023

Hi Hans, The approach here will depend on how one tracks the resizing of the Chart. In general, the Chart itself cannot be automatically resized, so a common approach is to wrap it in a container and track the resizing of this container to resize the Chart. In this case, if the Chart occupies 100% of the container, you can use the width and height of the wrapper to know the dimensions of the Chart. Here is an example with a Splitter tracking the resizing of the pane to resize the Chart and get its dimensions: [https://blazorrepl.telerik.com/mRagYzkt14RNolJ306.](https://blazorrepl.telerik.com/mRagYzkt14RNolJ306.) I hope you will find that useful. Please let us know if any other questions appear. Regards, Nadezhda Tacheva

### Response

**Hans** commented on 05 Jun 2023

Thanks for the answer, it is definitely a good pointer in the right direction. My charts are placed on a TileLayoutItem, and while there is an OnResize event for TileLayout, this event it does only provide the ID of the tile. I guess need to create a "IParentPaneSizeResolver.ResolveSize(string ID, out var width, out var height)" to resolve this then. It is a pity these (runtime) info's are not directly available from the chart component itself. Something similar to the TileLayout.GetState() but then TelerikChart,GetState() would already be just fine. Regards - Hans

### Response

**Nadezhda Tacheva** commented on 08 Jun 2023

Hi Hans, Please see my comments on the relevant points as follows: TileLayout Resize You are correct, the OnResize event indeed provides only the ID of the Tile. We do, however, have plans to enhance that in a future version of the product: TileLayoutItem Width/ColSpan on resize. I added your vote there and you can follow the item to get status updates. In the meantime, a possible option is to track the Tilelayout state OnResize. Chart state Some components indeed have a state - for example, TileLayout, Grid and more. The state of the component generally includes information for features that can be changed by the user. For the TileLayout, such features are order, rowspan and colspan. The purpose of the state is to give you, the developer, information about the changes the user made on the component state. As the Chart itself cannot be resized by the user, having a state with its size is not really applicable. I hope this provides more clarity on the matter.
