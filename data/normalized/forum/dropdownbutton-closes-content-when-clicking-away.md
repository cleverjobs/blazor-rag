# DropdownButton closes content when clicking away

## Question

**Sco** asked on 29 Apr 2024

Hello, Is there a way to prevent the DropdownButton content from closing when clicking away from the dropped down content? Thank you, Scott

## Answer

**Hristian Stefanov** answered on 30 Apr 2024

Hi Scott, A feature request for Cancelable OnOpen and OnClose Events has already been submitted on our public feedback portal. Once implemented, it will allow you to conditionally cancel the closing when you detect a click outside of the dropped down content. I voted for it on your behalf and raised its priority. You can also subscribe to receive email notifications for status updates. If any alternative appears in the meantime, I will share it as a comment at the above link. Regards, Hristian Stefanov Progress Telerik

### Response

**Scott Michetti** answered on 30 Apr 2024

Thank you for your response. I will try your recommendation, however, the link you provided in the request has an error loading. I left comments in the future request. Example implementation: [https://blazorrepl.telerik.com/mekbkTPE21kwyMBU05](https://blazorrepl.telerik.com/mekbkTPE21kwyMBU05) throws an error. See attached. Thanks, Scott

### Response

**Scott Michetti** commented on 01 May 2024

After running it a few more times, I got the demo to run. I noticed a strange bug when I add an input to the ItemTemplate. If I click on the DropdownList anywhere but the arrow, the textbox inside the ItemTemplate is not enabled. If I click on the arrow on the right side of the DropdownList , the textbox is enabled. I have a modified version of the sample code you linked above. I hope you have a solution to this. That is all I need to get it to work. Thanks, Scott @* Do not show "Export as" item in the popup *@<style> .custom-popup-class.k-list-ul.k-list-item:nth-child (1) { display: none; } </style> <TelerikDropDownList Data="@Items" OnOpen="OnDropDownListPopupOpen" OnClose="@OnDropDownListPopupClose" ValueField="@nameof(ItemDescriptor.ItemId)" TextField="@nameof(ItemDescriptor.ItemText)" Value="@DropDownListValue" ValueChanged="@( (int selectedValue)=> OnDropDownValueChanged(selectedValue) )" Width="315px"> <DropDownListSettings> <DropDownListPopupSettings Class="custom-popup-class" Height="auto" /> </DropDownListSettings> <ValueTemplate> <div style="padding-right:3px"> </div> @context.ItemText </ValueTemplate> <ItemTemplate> <div style="width: 30%; margin: 0 auto;"> <TelerikPanelBar Data="@Data" @bind -ExpandedItems="@ExpandedItems"> <PanelBarBindings> <PanelBarBinding Level="0"> <ContentTemplate Context="panelBarContext"> <div> <TelerikTextBox @bind -Value="@MyValue" Placeholder="Placeholder..."> </TelerikTextBox> </div> </ContentTemplate> </PanelBarBinding> </PanelBarBindings> </TelerikPanelBar> </div> </ItemTemplate> </TelerikDropDownList> @code { public class TreeItem { public int Id { get; set; } public string Text { get; set; } public bool Disabled { get; set; } public IEnumerable <TreeItem> Items { get; set; } } public IEnumerable <TreeItem> Data { get; set; } public IEnumerable <object> ExpandedItems { get; set; } private void LoadFlatData() { // TODO: Move to hierarchical data List <TreeItem> items=new List <TreeItem> (); items.Add(new TreeItem() { Id=0, Text="My Teammates"}); Data=items; ExpandedItems=new List <object> { items.First() }; } private int DropDownListValue { get; set; } private bool isPopupOpen { get; set; } public string MyValue {get; set; }="test"; protected override void OnInitialized() { LoadFlatData(); //always keep the "Export as" selected DropDownListValue=1; } private void OnDropDownValueChanged(int selectedValue) { //get the selected item but do not update the viewmodel, so the text "Export as" is always visible var selectedItem=Items.FirstOrDefault(x=> x.ItemId==selectedValue); Console.WriteLine($"The user selected export as: {selectedItem.ItemText}"); } private void OnDropDownListPopupOpen(DropDownListOpenEventArgs args) { isPopupOpen=true; } private void OnDropDownListPopupClose(DropDownListCloseEventArgs args) { isPopupOpen=true; // args.IsCancelled=true; } private List <ItemDescriptor> Items { get; set; }=new List <ItemDescriptor> () { new ItemDescriptor(){ ItemId=1, ItemText="Export as", Icon=SvgIcon.Download}, new ItemDescriptor(){ ItemId=2, ItemText="xlsx", Icon=SvgIcon.FileExcel}, }; public class ItemDescriptor { public int ItemId { get; set; } public string ItemText { get; set; } public ISvgIcon Icon { get; set; } } }

### Response

**Hristian Stefanov** commented on 01 May 2024

Hi Scott, Thank you for getting back to me with an update on the situation. Now let me help you adjust the sample to meet your needs. A bug report has already been submitted on our public

### Response

**Scott Michetti** commented on 01 May 2024

Thank you for the quick response Hristian. I was unable to run the code in the REPL. I received this error. " Script tags should not be placed inside components because they cannot be updated dynamically. To fix this, move the script tag to the 'index.html' file or another static location. For more information see [https://go.microsoft.com/fwlink/?linkid=872131](https://go.microsoft.com/fwlink/?linkid=872131) " I did add the code to my project, however the focus is still not working. I confirmed that the javascript code is reached by placing a breakpoint in the removeFocus() function. The await TextBoxRef.FocusAsync(); runs but does not set the focus. Any other suggestions? If I run the code with a breakpoint, the focus does go to the textbox. One other question. I also have a button next to the textbox that pops up a TelerikDialog. The dialog appears behind the DropDownListPopup window.(I set args.isCancelled=true in the OnDropDownListPopupClose event) Is there a way to get that to the front or shrink the window while the dialog is open? Thanks, Scott

### Response

**Hristian Stefanov** commented on 02 May 2024

Hi Scott, Here is a modified version of the example prepared in this REPL link. Please run and test it to see the result. The sample includes a TelerikDialog as well. To make it visible above the DropDownList popup, I reduced the z-index via CSS. Kind Regards, Hristian

### Response

**Scott Michetti** commented on 02 May 2024

Thank you for the quick reply. Your dialog solution is a great idea. The reason I was unable to get the focus on the textbox is because in my project, I have numerous TelerikDropdownList controls on the page, so the document.querySelector(".k-dropdownlist"); was grabbing the wrong element. I modifed your code to the following and it now works. function removeFocus() { var elements=document.querySelectorAll(".k-dropdownlist"); elements.forEach((element)=> { element.blur() }); } Thanks again for all of your help. My project is working as required thanks to you. Scott

### Response

**Hristian Stefanov** commented on 03 May 2024

Hi Scott, Thank you for getting back to me with feedback. I'm glad to hear that your project is working as required now. Kind Regards, Hristian
