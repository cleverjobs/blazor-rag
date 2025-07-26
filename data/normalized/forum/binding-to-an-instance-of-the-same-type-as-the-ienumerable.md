# Binding to an instance of the same type as the IEnumerable

## Question

**Nic** asked on 14 Nov 2019

Hi, I guess this is a feature request! It would be good if I could set the bind-value to a property of the same type as the type of the IEnumerable used to populate the list. At the moment I'm not sure if this is possible as it seems to insist on a ValueField, but I don't want to bind to a field I want to bind to the whole class. So instead of this: <TelerikDropDownList Data="@NavSets" TItem="UiNavSet" TValue="Guid" Width="200px" TextField="DisplayName" ValueField="Id" @bind-Value="@CurrentNavSetId" PopupHeight="100" /> @{ [Parameter] public List<UiNavSet> NavSets { get; set; } private Guid _currentNavSetId; Guid CurrentNavSetId { get=> _currentNavSetId; set { if (_currentNavSetId !=value) { _currentNavSetId=value; ChangeNavSet(_currentNavSetId); } } } } I want to do this: <TelerikDropDownList Data="@NavSets" TItem="UiNavSet" TValue="UiNavSet" Width="200px" TextField="DisplayName" ValueField="?????" @bind-Value="@CurrentNavSet" PopupHeight="100" /> @{ [Parameter] public List<UiNavSet> NavSets { get; set; } public UiNavSet CurrentNavSet { get; set; } // Bind to this } I'm not sure if this achievable, or what to put in ValueField?? Thanks.

## Answer

**Marin Bratanov** answered on 18 Nov 2019

Hi Nick, You can do this with primitive types: [https://docs.telerik.com/blazor-ui/components/dropdownlist/data-bind#primitive-types.](https://docs.telerik.com/blazor-ui/components/dropdownlist/data-bind#primitive-types.) If you want to choose an entire model directly, you can use single row selection in a grid: [https://docs.telerik.com/blazor-ui/components/grid/selection/single.](https://docs.telerik.com/blazor-ui/components/grid/selection/single.) Alternatively, you can use the ValueChanged event to update a field in the view model based on the selected Value from the dropdownlist: [https://docs.telerik.com/blazor-ui/components/dropdownlist/events.](https://docs.telerik.com/blazor-ui/components/dropdownlist/events.) For example, if you have a List<MyModels>, a simple .Where() call will give you the item. In such a case, in the ValueField you will put the identifier of the UiNavSet class, and you can set the CurrentNavSet parameter in ValueChanged. The dropdownlist itself is a relatively simple input that will not work with entire models, because that will carry weight and requirements that will be difficult to implement. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 21 Nov 2019

A quick follow up for some more context I missed last time Another major reason why we bind to primitive types for the Value is so that validation can work out-of-the-box. Otherwise it would have to be some entirely custom solution that would, once again, be very difficult to integrate into a ready-made component. Regards, Marin Bratanov

### Response

**Nick** answered on 22 Nov 2019

Hi Marin, thanks again. I haven't really played with the validation, so I'm not quite sure why using a primitive type is important? I has assumed that you used primitive type because they are easily comparable, so you can find the record. If that is the case could we not also use classes which have implemented Equals or IComparable? Thanks, Nick.

### Response

**Marin Bratanov** answered on 22 Nov 2019

Hello Nick, It might be, but even if it were, it would introduce a lot of complexity and requirements that would just be confusing. In any case, the code you'd have to write to provide for such binding would be more than the lookup you need to do now. Regards, Marin Bratanov
