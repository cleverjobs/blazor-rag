# Grid grouping not working in Chrome

## Question

**Len** asked on 16 Feb 2021

I have a grid with multiple columns and grouping works fine in full screen mode in both Firefox and Chrome. But when I open my application in Chrome and use the Chrome DevTools to set the window size to that of an iPad for example, I can't drag the columns to the grouping area anymore. So no grouping possible anymore. Is that a known issue? I couldn't find similar threads for this issue with blazor. Thanks in advance!

## Answer

**Marin Bratanov** answered on 16 Feb 2021

Hi Lena, I reproduced an issue with touch devices and I logged it for fixing. You can Follow its status here: [https://feedback.telerik.com/blazor/1507199-dragging-the-column-header-to-group-is-not-possible-on-a-touch-device.](https://feedback.telerik.com/blazor/1507199-dragging-the-column-header-to-group-is-not-possible-on-a-touch-device.) Could you confirm for me whether this is about using touch input versus the mouse, or something else? Does, for example, the same issue exist if you open the grid grouping demo on a mobile phone so you get a real touch device? Do you have another scenario where this issue manifests? Regards, Marin Bratanov

### Response

**Lena** answered on 17 Feb 2021

Hi Marin, the same issue exists if I open this ( [https://demos.telerik.com/blazor-ui/grid/grouping](https://demos.telerik.com/blazor-ui/grid/grouping) ) demo on my android phone. I tried it with following browsers: Samsung Internet, Chrome, Firefox. With Samsung Internet and Chrome I could not drag the column header anywhere. When I started to drag a header, immediately a little ban symbol appears. In Firefox I could actually drag the header a little bit out of its column header box (but still the little ban symbol appearing). But when I tried to drag the column header to the grouping area, the device took that movement as a scroll, so I couldn't reach the grouping area either. I don't have any other scenarios where this issue manifests, so I hope this helps.

### Response

**Lena** answered on 17 Feb 2021

Just figured out: Reordering the grid columns via drag and drop is also not possible on mobile devices. Tested in Chrome, emulated with DevTools, also tested on mobile device with Samsung Internet, Chrome and Firefox.

### Response

**Marin Bratanov** answered on 17 Feb 2021

Indeed, reordering has the same issue on touch devices, you can Track on this page I made on your behalf: [https://feedback.telerik.com/blazor/1507325-dragging-the-column-header-to-reorder-columns-is-not-possible-on-a-touch-device.](https://feedback.telerik.com/blazor/1507325-dragging-the-column-header-to-reorder-columns-is-not-possible-on-a-touch-device.) Thank you for clarifying the scenario for me, it helps to know that this is related to touch devices and not to something else. You will also find your Telerik points updated as a small "thank you" for your reports. Regards, Marin Bratanov

### Response

**Lena** answered on 17 Feb 2021

Great, thanks for the effort!

### Response

**Marin Bratanov** answered on 17 Feb 2021

Thank YOU for reporting these issues, Lena. --Marin
