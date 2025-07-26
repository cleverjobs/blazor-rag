# Invalid operation exception on Telerik Form control

## Question

**bim** asked on 16 Apr 2025

Hello all, I am getting the following error upon running deployed blazor app on IIS. When running it from local VS 2022 there are no issues. blazor.web.js:1 [2025-04-16T16:55:34.549Z] Error: System.InvalidOperationException: Unable to set property 'columns' on object of type 'Telerik.Blazor.Components.TelerikForm'. The error was: Unable to cast object of type 'System.String' to type 'System.Int32'.
---> System.InvalidCastException: Unable to cast object of type 'System.String' to type 'System.Int32'.
at Microsoft.AspNetCore.Components.Reflection.PropertySetter.CallPropertySetter[TTarget,TValue](Action`2 setter, Object target, Object value)
at Microsoft.AspNetCore.Components.Reflection.ComponentProperties.<SetProperties>g__SetProperty|3_0(Object target, PropertySetter writer, String parameterName, Object value)
--- End of inner exception stack trace ---
at Microsoft.AspNetCore.Components.Reflection.ComponentProperties.<SetProperties>g__SetProperty|3_0(Object target, PropertySetter writer, String parameterName, Object value)
at Microsoft.AspNetCore.Components.Reflection.ComponentProperties.SetProperties(ParameterView& parameters, Object target)
at Microsoft.AspNetCore.Components.ComponentBase.SetParametersAsync(ParameterView parameters)
at Telerik.Blazor.Components.TelerikForm.SetParametersAsync(ParameterView parameters)
at Microsoft.AspNetCore.Components.Rendering.ComponentState.SupplyCombinedParameters(ParameterView directAndCascadingParameters) <TelerikForm Columns="3" ColumnSpacing="35px" Model="@FormModel"> <FormItems> <!-- Dropdown 1 --> <FormItem> <Template> <div>Dropdown 1</div> <TelerikComboBox Width="350px" Data="@Dropdown1Options" TextField="Text" ValueField="Value" @bind-Value="@FormModel.Dropdown1Value" ShowClearButton="true" Filterable="true" Placeholder="Select"> </TelerikComboBox> </Template> </FormItem> <!-- TextField 1 --> <FormItem> <Template> <div>TextField 1</div> <TelerikTextBox Width="350px" @bind-Value="@FormModel.TextField1" /> </Template> </FormItem> <!-- TextField 2 --> <FormItem> <Template> <div>TextField 2</div> <TelerikTextBox Width="350px" @bind-Value="@FormModel.TextField2" /> </Template> </FormItem> <!-- Dropdown 2 --> <FormItem> <Template> <div>Dropdown 2</div> <TelerikComboBox Width="350px" Data="@Dropdown2Options" TextField="Text" ValueField="Value" @bind-Value="@FormModel.Dropdown2Value" ShowClearButton="true" Filterable="true" Placeholder="Select"> </TelerikComboBox> </Template> </FormItem> <!-- Dropdown 3 --> <FormItem ColSpan="2"> <Template> <div>Dropdown 3</div> <TelerikComboBox Width="350px" Data="@Dropdown3Options" TextField="Text" ValueField="Value" @bind-Value="@FormModel.Dropdown3Value" ShowClearButton="true" Filterable="true" Placeholder="Select"> </TelerikComboBox> </Template> </FormItem> <!-- Dropdown 4 --> <FormItem> <Template> <div>Dropdown 4</div> <TelerikComboBox Width="350px" Data="@Dropdown4Options" TextField="Text" ValueField="Value" @bind-Value="@FormModel.Dropdown4Value" ShowClearButton="true" Filterable="true" Placeholder="Select"> </TelerikComboBox> </Template> </FormItem> <!-- Dropdown 5 --> <FormItem> <Template> <div>Dropdown 5</div> <TelerikComboBox Width="350px" Data="@Dropdown5Options" TextField="Text" ValueField="Value" @bind-Value="@FormModel.Dropdown5Value" ShowClearButton="true" Filterable="true" Placeholder="Select"> </TelerikComboBox> </Template> </FormItem> <!-- Dropdown 6 --> <FormItem> <Template> <div>Dropdown 6

### Response

**Anislav** commented on 17 Apr 2025

Could you extract a sample that reproduces the issue and share it via: [https://blazorrepl.telerik.com/?](https://blazorrepl.telerik.com/?)
