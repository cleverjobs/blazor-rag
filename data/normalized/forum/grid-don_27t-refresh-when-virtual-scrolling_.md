# Grid don't refresh when Virtual Scrolling!

## Question

**wuwu** asked on 08 Jun 2020

when running the Demo,If you scroll down too fast,Grid control don't refresh,even wait a long time but if scroll back little ,then it can refresh.

## Answer

**Svetoslav Dimitrov** answered on 08 Jun 2020

Hi Wu, As attached file, you can see a project that has a Grid with Virtual Scrolling enabled. If this project works for you, you can compare it to your own and if the issue is reproducible, you can make changes to that project and send it back to us for further investigation. That being said, if you are exploring our live demos there can be some issues caused by latency because of the distance between you and our servers (our demos are running on Server-side hosting model). Regards, Svetoslav Dimitrov

### Response

**wu** answered on 08 Jun 2020

Don't modify,the bug appear in your project,but very random. Use the wheel to quickly scroll five to six pages, then stop and may appear,just maybe!

### Response

**wu** answered on 08 Jun 2020

Here's a video,Suffix: mkv

### Response

**Svetoslav Dimitrov** answered on 09 Jun 2020

Hello Wu, On the screenshots I see that the rows you have are about 100px tall, while the settings on our demo and in the sample I sent set 60px height. This is critical for this feature and the grid settings must match the display. You can read more about this here: [https://docs.telerik.com/blazor-ui/components/grid/virtual-scrolling#notes.](https://docs.telerik.com/blazor-ui/components/grid/virtual-scrolling#notes.) Regards, Svetoslav Dimitrov

### Response

**wu** answered on 09 Jun 2020

The actual browser zoom scaling and screen DPI is controlled by the user, then I can understand that this mode is limited, in fact,the use range is not large.
