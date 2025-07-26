# Editor in Window

## Question

**RobRob** asked on 01 Sep 2020

Is it possible to use an editor in a window? The following seems to hang the application when opening the window: @page "/test" <div class="container-fluid"> <TelerikWindow Left="3rem" Top="2rem" Visible="@Visible"> <WindowTitle>Test</WindowTitle> <WindowActions><WindowAction Name="Close" @onclick="@(()=> Visible=false)" /></WindowActions> <WindowContent> <TelerikEditor @bind-Value="Body" Width="650px" Height="400px"></TelerikEditor> </WindowContent> </TelerikWindow> <TelerikButton ButtonType="@ButtonType.Button" OnClick="@(()=> Visible=true)">Editor</TelerikButton> </div> @code{ private string Body { get; set; } private bool Visible { get; set; } }

## Answer

**Marin Bratanov** answered on 01 Sep 2020

Hello Rob, This issue is caused by this bug, and you can find a workaround in my post from 18 Aug 2020: [https://feedback.telerik.com/blazor/1430180-telerikwindow-hosted-within-a-component-hosted-in-a-telerikwindow-goes-into-infinite-loop-eating-memory.](https://feedback.telerik.com/blazor/1430180-telerikwindow-hosted-within-a-component-hosted-in-a-telerikwindow-goes-into-infinite-loop-eating-memory.) I've added your Vote to it to raise its priority and you can Follow it for email status notifications. Regards, Marin Bratanov

### Response

**Rob** answered on 01 Sep 2020

Ok, thanks for that Marin!

### Response

**Simon** answered on 01 Feb 2021

Hi, I had this issue too, but I've just re-tested in 2.21.1 and all seems to work fine. Tested for both Modal and non-modal windows. Can Admin confirm it's fixed please? Simon

### Response

**Marin Bratanov** answered on 01 Feb 2021

Hello Simon, This is fixed, and the best way to track and confirm such statuses is through the
