# ValueChanged Error

## Question

**Jon** asked on 03 Jun 2020

Hi.. What is wrong? When the value changes I need to set values to other textboxes. What is wrong with my 'tags'? When I set @bind-value , I get error that I can't have 2 change events. I also need to bind to FoodType property. thx again! Telerik.Blazor.Components.TelerikDropDownList`2[CKonboard.Data.Models.EventFoodType,System.String] requires a value for the 'ValueExpression' ValueExpression is provided automatically when using 'bind-Value'. at Telerik.Blazor.Components.Common.TelerikSelectBase`2.OnInitializedAsync() at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync() at Telerik.Blazor.Components.Common.TelerikSelectBase`2.SetParametersAsync(ParameterView parameters) <TelerikDropDownList Id="FoodType" ValueChanged="@((string c)=> EventSelected(c))" Value="@Service.FoodType" Data="@Lookups.EventFoodTypes()" TextField="EvtType" DefaultText="-Select First Event Food Type" ValueField="EvtType" PopupWidth="200px" Width="200px" PopupHeight="130PX" Class="ddl-no-bg">

## Answer

**Marin Bratanov** answered on 03 Jun 2020

Hi Jonathan, You can read more about the error and its solutions in this article: [https://docs.telerik.com/blazor-ui/knowledge-base/requires-valueexpression](https://docs.telerik.com/blazor-ui/knowledge-base/requires-valueexpression) When using the <Parameter>Changed event, you can use @bind-<Parameter>, that's how the framework operates. Regards, Marin Bratanov
