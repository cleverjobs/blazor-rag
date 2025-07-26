# Error when trying to render the wizard

## Question

**BobBob** asked on 20 Jul 2021

I have a wizard that is defined like this: <TelerikWizard @bind-Value="step" Height="100%" Width="100%"> <WizardSteps> <WizardStep Label="Information" OnChange="OnWizardStepChange"> <Content> </Content> </WizardStep> @if (showMapping)
{ <WizardStep Label="Column Mapping" OnChange="OnWizardStepChange"> <Content> </Content> </WizardStep> }
@if (showPreview)
{ <WizardStep Label="Preview" OnChange="OnWizardStepChange"> <Content> </Content> </WizardStep> } <WizardStep Label="Validation" OnChange="OnWizardStepChange"> <Content> </Content> </WizardStep> </WizardSteps> <WizardButtons> @{
var index=context;
int lastStep=3;
if (!showMapping) { lastStep -=1; }
if (!showPreview) { lastStep -=1; }

if (index> 0)
{ <TelerikButton ButtonType="ButtonType.Button" OnClick="@(()=> step -=1)"> Previous </TelerikButton> }

if (index <lastStep)
{ <TelerikButton ButtonType="ButtonType.Button" OnClick="@(()=> step +=1)"> Next </TelerikButton> }

if (index==lastStep)
{ <TelerikButton ButtonType="ButtonType.Button" OnClick="@CreateImport"> Import </TelerikButton> }
} </WizardButtons> </TelerikWizard> When I try to load the page, the Wizard is giving me the following error: [12:06:18 WRN] Unhandled exception rendering component: Value cannot be null. (Parameter 'format')
System.ArgumentNullException: Value cannot be null. (Parameter 'format')
at System.String.FormatHelper(IFormatProvider provider, String format, ParamsArray args)
at System.String.Format(String format, Object arg0, Object arg1)
at Telerik.Blazor.Components.TelerikWizard.get_PagerMessage()
at Telerik.Blazor.Components.TelerikWizard.BuildRenderTree(RenderTreeBuilder __builder)
at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.RenderInExistingBatch(RenderQueueEntry renderQueueEntry)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.ProcessRenderQueue() I cannot figure out what I am doing wrong?

## Answer

**Bob** answered on 20 Jul 2021

I figured out the problem. I am using localization and did not update my messages.resx with the newest file which is required when using the Wizard Control. Thanks.

### Response

**Petr** commented on 30 Aug 2021

Hi bob, u update messages.resx from [https://github.com/telerik/blazor-ui/blob/master/common/localization/ClientLocalizationResx/Shared/Resources/TelerikMessages.resx?](https://github.com/telerik/blazor-ui/blob/master/common/localization/ClientLocalizationResx/Shared/Resources/TelerikMessages.resx?)

### Response

**Dimo** commented on 01 Sep 2021

@Petr - there are two places to get updated localization files. One is maintained by us and one is maintained by the community. The Resources folder of our demo site. The demo site is part of the UI for Blazor installation: /demos/TelerikBlazorDemos/Resources/ [https://github.com/telerik/blazor-ui-messages](https://github.com/telerik/blazor-ui-messages)

### Response

**Thomas** answered on 12 Jan 2022

Hello, can you explain more about how to resolve this issue? I have the same problem but I don't know about how to resolve it Thanks

### Response

**Dimo** commented on 12 Jan 2022

@Thomas - Go to [https://www.telerik.com/account/downloads](https://www.telerik.com/account/downloads) Go to UI for Blazor and download the full MSI or ZIP installer. Run the MSI installer or extract the ZIP contents. Update your app localization files with the help of TelerikMessages.resx and TelerikMessages.designer.cs from [ installation folder ]/demos/TelerikBlazorDemos/Resources/

### Response

**Thomas** commented on 12 Jan 2022

Hi @Dimo, thanks a lot for your help. I will try to do that
