# Telerik.Blazor.Components.TelerikWindow does not have a property matching the name 'Centered'

## Question

**She** asked on 14 Jul 2025

When building the application in Release configuration and navigating to the page containing the ReportViewer component, the following error is thrown: “Telerik.Blazor.Components.TelerikWindow does not have a property matching the name ‘Centered’.” at Microsoft.AspNetCore.Components.Reflection.ComponentProperties.ThrowForUnknownIncomingParameterName(Type targetType, String parameterName) at Microsoft.AspNetCore.Components.Reflection.ComponentProperties.SetProperties(ParameterView& parameters, Object target) at Microsoft.AspNetCore.Components.ParameterView.SetParameterProperties(Object target) at Microsoft.AspNetCore.Components.ComponentBase.SetParametersAsync(ParameterView parameters) at Telerik.Blazor.Components.TelerikWindow.SetParametersAsync(ParameterView parameters) at Microsoft.AspNetCore.Components.Rendering.ComponentState.SupplyCombinedParameters(ParameterView directAndCascadingParameters) This problem does not occur in Debug mode and was not present in earlier builds. The affected page uses both the ReportViewer component and the SendEmailDialogSettings. For reference, the project is targeting .NET 8.0 and depends on: • Telerik.UI.for.Blazor (v9.1.0) • Telerik.ReportViewer.BlazorNative (v19.1.25.521) The page: <TelerikTabStrip TabPosition="TabPosition.Top" TabAlignment="TabStripTabAlignment.Start"> <TabStripTab Title="Sink"> <ReportViewer ServiceType="@ReportViewerServiceType.REST" ServiceUrl="@ReportServerUrl" @bind-ReportSource="@ReportSourceOrganisations" @bind-ScaleMode="@ScaleMode" @bind-ViewMode="@ViewMode" @bind-ParametersAreaVisible="@ParametersAreaVisible" @bind-DocumentMapVisible="@DocumentMapVisible" @bind-Scale="@Scale" PageMode="@PageMode.ContinuousScroll" PrintMode="@PrintMode.AutoSelect" KeepClientAlive="true" EnableSendEmail="true" Height="900px" Width="100%"> <ReportViewerSettings> <SendEmailDialogSettings From="@From" To="@Emails" Cc="@CarbonCopyEmail" Subject="@Subject" Format="XLSX" Body="<br/> <br/> Best regards, </br>"> </SendEmailDialogSettings> </ReportViewerSettings> </ReportViewer> </TabStripTab> </TelerikTabStrip>

## Answer

**Hristian Stefanov** answered on 14 Jul 2025

Hi Sherzod, The error occurs because the Centered parameter was removed from the TelerikWindow component starting with Telerik UI for Blazor v9.0.0. Here are the breaking changes notes from that release: Breaking Changes Notes 9.0.0. In short, the Centered parameter did not work after the initial Window display. Removing the parameter actually made the component setup and management simpler. Otherwise, the app should also reset Top and Left explicitly when setting Centered="true" programmatically. To center the Window, simply set the Top and Left parameter values to an empty string at any time. Regards, Hristian Stefanov Progress Telerik

### Response

**Sherzod** commented on 14 Jul 2025

Thank you for your response. It appears that the error originates from the email-dispatch window, to which I have no direct access and cannot alter its internal properties. As a result, I am uncertain how to apply the @bind-Left and @bind-Top attributes to this component.

### Response

**Mario** commented on 17 Jul 2025

Hello, I am also experiencing the issue that has already been reported: When building the application in Release configuration and navigating to the page containing the ReportViewer component, the following error is thrown: “Telerik.Blazor.Components.TelerikWindow does not have a property matching the name ‘Centered’.”
at Microsoft.AspNetCore.Components.Reflection.ComponentProperties.ThrowForUnknownIncomingParameterName(Type targetType, String parameterName) at Microsoft.AspNetCore.Components.Reflection.ComponentProperties.SetProperties(ParameterView& parameters, Object target) at Microsoft.AspNetCore.Components.ParameterView.SetParameterProperties(Object target) at Microsoft.AspNetCore.Components.ComponentBase.SetParametersAsync(ParameterView parameters) at Telerik.Blazor.Components.TelerikWindow.SetParametersAsync(ParameterView parameters) at Microsoft.AspNetCore.Components.Rendering.ComponentState.SupplyCombinedParameters(ParameterView directAndCascadingParameters) My project is using: Telerik.UI.for.Blazor (v9.1.0) Telerik.ReportViewer.BlazorNative (v19.1.25.716) I am attaching a zip file where the error can be reproduced by simply running the project. I have also deleted the bin and obj folders and cleared NuGet caches, but I haven't been able to resolve the problem. Is there any guide or further assistance you can provide to help me with this?

### Response

**Hristian Stefanov** commented on 18 Jul 2025

Hi Mario, Based on the provided information on your case, I can confirm that the issue occurs because Telerik.ReportViewer.BlazorNative v19.1.25.521 depends on Telerik UI for Blazor v7.1.0 (as per their latest release ). This means you cannot reference v9.1.0 in your application, as ReportViewer.BlazorNative has not yet been updated to depend on the newer version. Notably, in v9.1.0 the Centered parameter was removed as part of the breaking changes, which is contributing to the error. In summary: until Telerik.ReportViewer.BlazorNative is updated to target Blazor v9.1.0, you should downgrade your Telerik UI for Blazor version to v7.1.0 to maintain compatibility. Best, Hristian

### Response

**Sherzod** answered on 14 Jul 2025

After removing the bin and obj folders and rebuilding the solution, the issue was resolved.
