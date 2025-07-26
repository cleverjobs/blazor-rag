# nullable dto gets selected

## Question

**kha** asked on 03 Feb 2020

Hello, i found an issue in TelerikDropDownList when you bind TelerikDropDownList value to a nullable property after data is loaded it selects the first one as the value but when property is not nullable and its bound to value of TelerikDropDownList when data is read it wont select any value which seems reverse and also i might not want to select anything at all and let user leave this property empty since its nullable and also it would be good to have DefaultText for TelerikDropDownList but i cant use it seems unknown to TelerikDropDownList

## Answer

**Marin Bratanov** answered on 03 Feb 2020

Hi Khashayar, The DropDownList already has a DefaultText parameter: [https://docs.telerik.com/blazor-ui/components/dropdownlist/overview#examples](https://docs.telerik.com/blazor-ui/components/dropdownlist/overview#examples) It also shows correct behavior when the Value has the default value for its type (null for the string - which is nullable, and 0 for the integer). Could you start out from that sample and see if you are facing any issues? If yes, please post here a simple runnable modification of that snippet so I can take a look. Regards, Marin Bratanov

### Response

**khashayar** answered on 03 Feb 2020

actually i cant use DefaultText instead there is DefaultItem which i have no use for it DefaultText is like an unknown property for DropDown and this is the error Error: System.InvalidOperationException: Object of type 'Telerik.Blazor.Components.TelerikDropDownList`2 .... does not have a property matching the name 'DefaultText'. and for the issue <EditForm OnSubmit="Save" Model="FormData"> <TelerikDropDownList Data="@NamesList" TextField="FirstName" ValueField="Id" @bind-Value="@FormData.MyNameId"> </TelerikDropDownList> <TelerikDropDownList Data="@NamesList" TextField="FirstName" ValueField="Id" @bind-Value="@FormData.MyNullableNameId"> </TelerikDropDownList> <TelerikButton ButtonType="@ButtonType.Submit">submit</TelerikButton> </EditForm> @code { public FormModel FormData=new FormModel(); List<Names> NamesList=(Enumerable.Range(1, 20).Select(x=> new Names { Id=Guid.NewGuid(), FirstName="jon" + Guid.NewGuid() })).ToList(); public class Names { public Guid Id { get; set; } public string FirstName { get; set; } } public class FormModel { public Guid MyNameId { get; set; } public Guid? MyNullableNameId { get; set; } } void Save() { } } try the code above and hit submit button without choosing any value you will see the nullable property gets filled while not nullable property is 0

### Response

**Marin Bratanov** answered on 03 Feb 2020

Hi Khashayar, Please upgrade to the latest version (2.7.0 at the moment) and try this again [https://docs.telerik.com/blazor-ui/upgrade/overview](https://docs.telerik.com/blazor-ui/upgrade/overview) If an issue persists after following the current documentation (using DefaultText and validation ), with the latest version, let me know. Regards, Marin Bratanov

### Response

**khashayar** answered on 03 Feb 2020

thanks my problem is solved
