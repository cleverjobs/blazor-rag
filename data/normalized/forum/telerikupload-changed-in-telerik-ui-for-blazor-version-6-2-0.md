# TelerikUpload changed in Telerik.UI.for.Blazor version 6.2.0 ??

## Question

**Kur** asked on 30 Aug 2024

hi. I just now updated through NuGet to 6.0.2 and started seeing this message on the TelerikUpload component. How should I resolve this? I am uploading large files Thanks Unable to set property 'MaxFileSize' on object of type 'Telerik.Blazor.Components.TelerikUpload'. The error was: Specified cast is not valid. System.InvalidOperationException: Unable to set property 'MaxFileSize'

## Answer

**Dimo** answered on 30 Aug 2024

Hello Kurt, Starting from version 6.1.0, the MinFileSize and MaxFileSize parameters of the Upload and the FileSelect are of type long. Previously they were of type int. This change allows uploading larger files than before. Telerik UI for Blazor - release notes for 6.1.0 int is a subset of long, so we didn't expect casting-related problems due to the type change. What exactly are you trying to do? Regards, Dimo

### Response

**Kurt** commented on 30 Aug 2024

Hi. This is what I had that was working prior to the update. It was an integer value but ... <TelerikUpload SaveUrl="@SaveUrl" RemoveUrl="@RemoveUrl" OnProgress="@OnProgress" AllowedExtensions="@( new List<string>() { ".xls", ".xlsx", ".xlsm", ".xlsb" } )" OnSelect="@OnSelectHandler" OnSuccess="@OnSuccessHandler" OnCancel="@OnCancelHandler" OnRemove="@OnRemoveHandler" AutoUpload="true" Multiple="true" MaxFileSize="2097152" OnUpload="@OnUploadHandler" OnError="@OnUploadError"> </TelerikUpload> crit: Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100] Unhandled exception rendering component: Unable to set property 'MaxFileSize' on object of type 'Telerik.Blazor.Components.TelerikUpload'. The error was: Specified cast is not valid. System.InvalidOperationException: Unable to set property 'MaxFileSize' on object of type 'Telerik.Blazor.Components.TelerikUpload'. The error was: Specified cast is not valid. ---> System.InvalidCastException: Specified cast is not valid. at System.Nullable`1[[System.Int32, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].Unbox(Object o) at Microsoft.AspNetCore.Components.Reflection.PropertySetter.CallPropertySetter[TelerikUpload,Nullable`1](Action`2 setter, Object target, Object value) at Microsoft.AspNetCore.Components.Reflection.PropertySetter.SetValue(Object target, Object value) at Microsoft.AspNetCore.Components.Reflection.ComponentProperties.<SetProperties>g__SetProperty|3_0(Object target, PropertySetter writer, String parameterName, Object value) --- End of inner exception stack trace --- at Microsoft.AspNetCore.Components.Reflection.ComponentProperties.<SetProperties>g__SetProperty|3_0(Object target, PropertySetter writer, String parameterName, Object value) at Microsoft.AspNetCore.Components.Reflection.ComponentProperties.SetProperties(ParameterView& parameters, Object target) at Microsoft.AspNetCore.Components.ParameterView.SetParameterProperties(Object target) at Microsoft.AspNetCore.Components.ComponentBase.SetParametersAsync(ParameterView parameters) at Telerik.Blazor.Components.TelerikUpload.SetParametersAsync(ParameterView parameters) at Microsoft.AspNetCore.Components.Rendering.ComponentState.SupplyCombinedParameters(ParameterView directAndCascadingParameters)

### Response

**Dimo** commented on 02 Sep 2024

@Kurt - I confirm that the provided Upload declaration works on my side as is. In such cases, I try the following: Close Visual Studio Delete all bin and obj folders from the solution. Restart Visual Studio and rebuild the app. If this is a WebAssembly app, clear the browser cache.
