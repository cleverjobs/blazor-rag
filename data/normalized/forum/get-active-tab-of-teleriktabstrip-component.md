# Get active-tab of TelerikTabStrip-component

## Question

**Ger** asked on 03 May 2019

Dear Telerik, thank you for the wonderful Blazor controls. I have a question about the Tab-Control. I need to know the active tab in the code behind. I tried to acces the Title-property in the 'Telerik.Blazor.Components.TabStrip.TelerikTabStrip' - REF. But the Title-propery in de ActiveTab class is private and thus not accesible. Is there a way to know the active Tab in de code behind ? Regards, Gert

## Answer

**Marin Bratanov** answered on 03 May 2019

Hello Gert, Indeed, at the moment, the property is not exposed. I am logging this for improvement and you can track it by clicking the Follow button in the following page (I've already added your vote): [https://feedback.telerik.com/blazor/1407593-expose-current-tab-title.](https://feedback.telerik.com/blazor/1407593-expose-current-tab-title.) You will also find your Telerik points updated for bringing this up. Regards, Marin Bratanov

### Response

**Gert** answered on 07 May 2019

But would it be possible to add following feature also ? - Select/Activate a certain Tab programmatically Thx, Gert

### Response

**Marin Bratanov** answered on 07 May 2019

Hello Gert, This is already possible, here's an example: @using Telerik.Blazor.Components.TabStrip @using Telerik.Blazor.Components.Button <TelerikTabStrip ref="@myTabStrip"> <TelerikTab Title="First"> First tab content. <br /> <TelerikButton OnClick="@SelectSecondTab">Select the second tab</TelerikButton> </TelerikTab> <TelerikTab Title="Second" ref="@chosenTab"> Secont tab content. </TelerikTab> <TelerikTab Title="Third"> Third tab content. </TelerikTab> </TelerikTabStrip> @functions { Telerik.Blazor.Components.TabStrip.TelerikTabStrip myTabStrip; Telerik.Blazor.Components.TabStrip.TelerikTab chosenTab; void SelectSecondTab() { myTabStrip.SetActiveTab(chosenTab); } } Regards, Marin Bratanov
