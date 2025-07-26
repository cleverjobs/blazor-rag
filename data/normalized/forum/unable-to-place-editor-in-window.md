# Unable to place Editor in Window

## Question

**EliEli** asked on 18 Aug 2020

If an editor is placed in a Window the page will just spin on startup. Any other WindowContent I have tried works fine, it stops as soon as I add the Editor. Is there a different way to do this or is this a bug? <TelerikWindow Class="demo-window" Width="700px" Centered="true" Visible="true" Modal="false" @ref="EditWindow"> <WindowTitle> <strong>Edit</strong> </WindowTitle> <WindowActions> <WindowAction Name="Close" /> </WindowActions> <WindowContent> <TelerikEditor @bind-Value="@Value" Height="880px"> </TelerikEditor> </WindowContent> </TelerikWindow>

## Answer

**Marin Bratanov** answered on 18 Aug 2020

Hello Eli, The editor has, internally, a couple of other Window instances, and this causes this problem to manifest: [https://feedback.telerik.com/blazor/1430180-telerikwindow-hosted-within-a-component-hosted-in-a-telerikwindow-goes-into-infinite-loop-eating-memory.](https://feedback.telerik.com/blazor/1430180-telerikwindow-hosted-within-a-component-hosted-in-a-telerikwindow-goes-into-infinite-loop-eating-memory.) I've added your Vote to it to raise its priority and you can click the Follow button to get email status updates. I've also added a workaround there. Regards, Marin Bratanov
