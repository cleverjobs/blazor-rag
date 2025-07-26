# Additional parameters/logic for an existing base component

## Question

**Pio** asked on 26 Nov 2023

Hi Is there a better way to add an automated permission than replacing an existing component type? How else can I automatically check permissions on the base component "TelerikButton" instead of "MyTelerikButton"? With a large number of thousands of fields, it does not want to fill the Enable/Visible per field. My question is not only about permissions, but also about the ability to extend TelerikButton with its my additional [Parameter] which is not included in the basic set. I would be grateful if you could suggest a better solution. @foreach (var item in ListOfItemNames.Take(200))
{ <div class="row"> <div class="col"> <label for="@item"> @item </label> <MyTelerikButton Id="@item" Form="Device" Icon="SvgIcon.Stop" Title="@item" OnClick="@ButtonAction" ButtonType="ButtonType.Button" /> <MyTelerikTextBox Id="@item" Name="Device" Value="@item"> </MyTelerikTextBox> @* ... <Telerik...> etc *@</div> </div> } My Component public class MyTelerikButton: TelerikButton {

[ CascadingParameter (Name="Privileges" ) ] public required List<Privilege> Privileges { get; set; }=[]; protected override void OnInitialized () { base.OnInitialized(); var buttonName=Form + Id;
Enabled=Privileges.Any(x=>x.Code==buttonName);

}
}

## Answer

**Dimo** answered on 27 Nov 2023

Hi Piotr, Your current approach is valid. The standard way to add more parameters to a component is to create a derived class. Alternatively, you will have to download, modify and rebuild our source code. Looking at your code, you can also move the permission logic up in the component hierarchy and set the Enabled parameter of each component explicitly. But it looks like you don't want to go that way. Regards, Dimo Progress Telerik
