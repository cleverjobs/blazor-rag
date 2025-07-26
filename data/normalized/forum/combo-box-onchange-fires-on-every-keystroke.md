# Combo Box OnChange() fires on every keystroke

## Question

**Chr** asked on 24 Aug 2023

I have a Blazor form with five cascading combo boxes. The method to load the next combo box is called by the OnChange() event. I've put in breakpoints and seen it hit that method every keystroke and I can't figure out why. Its also refreshing the page on each keystroke. On each keystroke, the page refreshes, the OnChange method is called and then the page refreshes again. I understand why it does after, because there was a change. But its the before that is confusing me. Here is an example of the combo boxes. <div class="ms-section-header"> Change Details </div> <input type="text" hidden="true" @bind="ChangeDetails.ChangeDetailId" /> <div> <TelerikFloatingLabel Text="Level 1"> <TelerikComboBox @ref=cbl1 Class="justification" AllowCustom="true" Data="@L1" ClearButton="false" TextField="Name" ValueField="TaxonomyId" @bind-Value=@L1Value OnChange="@(()=> GetNextLevel(L1Value, 1))"> </TelerikComboBox> </TelerikFloatingLabel> </div> @if (!String.IsNullOrEmpty(L1Value))
{ <div> <TelerikFloatingLabel Text="Level 2"> <TelerikComboBox @ref=cbl2 Class="justification" AllowCustom="true" Data="@L2" ClearButton="false" TextField="Name" ValueField="TaxonomyId" @bind-Value=@L2Value OnChange="@(()=> GetNextLevel(L2Value, 2))"> </TelerikComboBox> </TelerikFloatingLabel> </div> } I attached a file that contains the whole page HTML and at the bottom is the OnChange method.

### Response

**Nadezhda Tacheva** commented on 29 Aug 2023

Hi Chris, The described behavior is indeed incorrect - OnChange should not fire on every keystroke. It should be raised as a confirmation of the selection - when the user selects an item with a mouse click, presses Enter in the input or blurs the input. At this stage, I cannot think of a reason for what is forcing this behavior. The code you have shared is not actually runnable, so I was not able to test it. Therefore, I tried replicating the scenario in a runnable sample in order to observe the behavior. When testing typing in the ComboBox input, however, OnChange is not hit on every keystroke. It behaves as expected on my end. You can find the code here: [https://blazorrepl.telerik.com/QdOCwtvw34b7kZoE47.](https://blazorrepl.telerik.com/QdOCwtvw34b7kZoE47.) Please revise it and let me know if I am missing something. When looking at your sample, it is not clear to me why the ComboBox instances in the form are not bound to fields in the model but to separate variables. It will be useful if you can share some more details here. For reference, you can check the value binding in the sample I shared. To move forward with the investigation, I will need a runnable reproduction. Can you please modify the sample I shared to showcase the exact behavior you are experiencing? You can generate a new snippet in the REPL tool or create an empty sample app using the Telerik Visual Studio Wizard. Thank you in advance for your cooperation!

### Response

**Chris** commented on 29 Aug 2023

so...this is embarrassing. I can't replicate it now, even in my original code. Obviously it was something in my code that I fixed inadvertently. Thanks for looking into this.

### Response

**Nadezhda Tacheva** commented on 31 Aug 2023

Hi Chris, Thanks for getting back to me! I am glad to find out that the issue no longer occurs. Should you face any other troubles, please do not hesitate to reach out.
